from bmtk.builder import NetworkBuilder
from bmtk.utils.reports.spike_trains import PoissonSpikeGenerator
from bmtk.utils.sim_setup import build_env_bionet
import numpy as np
import sys
import synapses
import random

seed = 967
random.seed(seed)
np.random.seed(seed)

synapses.load()
syn = synapses.syn_params_dicts()

net = NetworkBuilder("biophysical")

net.add_nodes(N=1, pop_name='PyrC',
              mem_potential='e',
              model_type='biophysical',
              model_template='hoc:feng_typeC',
              morphology=None)

net.add_nodes(N=1, pop_name='OLM',
              mem_potential='e',
              model_type='biophysical',
              model_template='hoc:basket',
              morphology=None)

backgroundPN = NetworkBuilder('bg_pn')
backgroundPN.add_nodes(N=1,
                   pop_name='tON',
                   potential='exc',
                   model_type='virtual')

backgroundOLM = NetworkBuilder('bg_olm')
backgroundOLM.add_nodes(N=1,
                   pop_name='tON',
                   potential='exc',
                   model_type='virtual')


conn = net.add_edges(source=net.nodes(pop_name='OLM'), target=net.nodes(pop_name='PyrC'),
              connection_rule=1,
              syn_weight=1.0,
              delay=0.1,
              distance_range=[-10000, 10000],
              dynamics_params='SOM2PN.json',
              model_template=syn['SOM2PN.json']['level_of_detail'])

conn.add_properties(['sec_id', 'sec_x'], rule=(0, 0.5), dtypes=[np.int32, np.float]) # places syn on apic at 0.9


conn = net.add_edges(source=backgroundPN.nodes(), target=net.nodes(pop_name=['PyrC']),
              connection_rule=1,
              syn_weight=1.0,
              delay=0.1,
              distance_range=[-10000, 10000],
              dynamics_params='tone2PN.json',
              model_template=syn['tone2PN.json']['level_of_detail'])
conn.add_properties(['sec_id', 'sec_x'], rule=(2, 0.9), dtypes=[np.int32, np.float]) # places syn on apic at 0.9

net.add_edges(source=backgroundOLM.nodes(), target=net.nodes(pop_name='OLM'),
              connection_rule=1,
              syn_weight=1.0,
              target_sections=['somatic'],
              delay=0.1,
              distance_range=[-10000, 10000],
              dynamics_params='AMPA_ExcToInh.json',
              model_template='exp2syn')


net.build()
net.save(output_dir='network')

backgroundPN.build()
backgroundPN.save_nodes(output_dir='network')

backgroundOLM.build()
backgroundOLM.save_nodes(output_dir='network')

psg = PoissonSpikeGenerator(population='bg_pn')
psg.add(node_ids=range(1),  # need same number as cells
        firing_rate=2,    # 1 spike every 1 second Hz
        times=(0.0, 5))  # time is in seconds for some reason
psg.to_sonata('2_cell_inputs/bg_pn_spikes.h5')

print('Number of background spikes for pn: {}'.format(psg.n_spikes()))

psg = PoissonSpikeGenerator(population='bg_olm')
psg.add(node_ids=range(1),  # need same number as cells
        firing_rate=20,    # 8 spikes every 1 second Hz
        times=(0.0, 5))  # time is in seconds for some reason
psg.to_sonata('2_cell_inputs/bg_olm_spikes.h5')

print('Number of background spikes for olm: {}'.format(psg.n_spikes()))
