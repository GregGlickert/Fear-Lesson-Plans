import os, sys
from bmtk.simulator import bionet
import numpy as np
import synapses
import warnings


def run(config_file):
    warnings.simplefilter(action='ignore', category=FutureWarning)
    synapses.load()

    conf = bionet.Config.from_json(config_file, validate=True)
    conf.build_env()
    graph = bionet.BioNetwork.from_config(conf)
    sim = bionet.BioSimulator.from_config(conf, network=graph)

    sim.run()
    bionet.nrn.quit_execution()


if __name__ == '__main__':
    if __file__ != sys.argv[-1]:
        run(sys.argv[-1])
    else:
        run('2Cell_SC.json')
