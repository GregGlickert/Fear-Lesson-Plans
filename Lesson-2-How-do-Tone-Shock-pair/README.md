# What is tone? What is shock? What is reward?
How do they pair to make us learn reward or fear?

<span style="color:#0070C0"> __Neurons connect to each other via synapses__ </span>

__  Axon from tone neuron__

__ 	Tone comes in as a series of spikes or electrical impulses from the neuron in the sensory neuron in the ear__

__ The axon of the tone neuron connects to the amygdala neuron via a __  __synapse __  __shown in the figure – two semi\-cylindrical pieces with a gap in between\.__

__ 	The synapse has two parts\, the left side is called pre\-synapse and it is connected to the tone neuron\, and the right part is called the post\-synapse that is connected to the amygdala neuron__

__ 	The electrical impulse is transmitted from the pre\- to the post\- synapse via neurotransmitters\. This is the role of the synapse\, i\.e\.\, transmit electrical impulses from one neuron to another\.__

__ 	Let us see how this information can be used to study the two neural pathways\. One is between tone and the amygdala and the other is between shock and the amygdala\. __

__ 	Optional – if you are interested\, you can learn more about synapses using web resources\.__

__What is the neural pathway for the tone – reward and fear cases? __

![](img/How%20do%20Tone-Shock%20Pair0.png)

__The pathway for food stimulus and for shock stimulus is similar\. __

__Can you sketch them for the fear conditioning case?__

__Putting both pathways together in the overall simplified fear circuit__

Note: All signals go through the thalamus \(relay station\!\) in our brains

![](img/How%20do%20Tone-Shock%20Pair1.png)

__ACTIVITY – 1__

<span style="color:#000000">YOUR CHALLENGE: Go into the virtual lab provided at the link below </span>  <span style="color:#000000"> _https://phet\.colorado\.edu/en/simulations/circuit\-construction\-kit\-dc_ </span>  <span style="color:#000000"> and click on the play button to get started\.</span>

<span style="color:#000000">Now put together both the tone and shock pathways using the simulator\, both connecting to the sam</span> e amygdala neuron\.

<span style="color:#000000">Solution provided at the end for the teacher\.</span>

__REVIEW\. How does the tone\-only configuration work?__

__ 	__  __First let us understand the big picture and some neurobiological concepts__

__ Load the code for “D1\.1\.ipynb” to the __  __Colab__  __ site\, research\.google\.com and do ‘Run All’ as usual\.  __

__url__  __ for __  __colab__  __ notebook: __  __[https://github\.com/KhuramC/Fear\-Lesson\-Plans](https://github.com/KhuramC/Fear-Lesson-Plans)__

![](img/How%20do%20Tone-Shock%20Pair2.png)

_Sliders on screen_ : You can adjust the tone frequency and the tone strength\.

_Plots on screen_ : Top: Times when the tone spikes reach amygdala\, and

Bottom: membrane potential V of amygdala neuron \(spike if V > 0 mV\)

1\.  How is firing of the amygdala related to fear?  Based on this\, how do we define the ‘fear state’ in this set of tutorials?

2\.  Do normal sounds \(tones\) cause the amygdala to elicit fear?   What sounds do? Explain the logic\.

__REVIEW\. How does the tone\-only configuration work?\.\.\.\.contd\.__

![](img/How%20do%20Tone-Shock%20Pair3.png)

__ 	You explore how the two parameters \(__  __i__  __\) tone frequency and \(ii\) tone\-PN synaptic strength affect firing rate of amygdala PN __  __using the __  __Colab__  __ code for D1\.1__

Now that you are familiar with the setup of the tutorial………\.

The baseline firing rate of the amygdala can be considered to be 0\.5 Hz \(most cells are silent\)\. You are to find tone strength settings to make sure the amygdala neuron fires at 0\.5 Hz\, and note it below:

The fear state firing rate of the amygdala is 7 Hz\. How will you adjust the tone strength to cause the amygdala neuron to fire at 7 Hz\. This state is accomplished after fear conditioning\, details of which we will consider in Colab tutorials D1\.2 and D1\.3\.

__Activity 2\. How do tone and shock cause plasticity in amygdala?__

![](img/How%20do%20Tone-Shock%20Pair4.png)

__ 	__  __Now consider tone and shock pathways as shown in slide 1 using code“D1\.2\.ipynb\. Try various combinations of parameters to explore how to grow the tone\-PN strength…and learn about Hebbian plasticity rule\!__

_1\-cell Model to Illustrate Tone\-shock Pairing_  __:__

__  Inputs are Tone through one pathway and Shock through another pathway\. Both axons \(‘wires’\) converge onto the same amygdala neuron\.__

__  The synapse will grow if the tone and shock are ‘paired’ in time\. That is\, if they occur close enough to each other in time\. __

__  In D1\.2\, you determine how close the tone and shock need to be in time for the synapse to grow\, i\.e\.\, get stronger\.__

__  Then in D1\.3\, you find out the mechanism that implements the strengthening of the synapse\, i\.e\.\, makes the synapse grow\.__

__How do tone and shock cause plasticity in amygdala?\.\.\.\.contd\.__

__ 	__  __Now consider tone and shock pathways as shown in slide 1 using the __  __Colab__  __ D1\.2\.ipynb\. Try various combinations of parameters to explore how to grow the tone\-PN strength…and learn about Hebbian plasticity rule\!__

Load the code titled “D1\.2\.ipynb” to the Colab site\, research\.google\.com and do ‘Run All’ as usual\.  Write down on a separate sheet the plots you see and what they mean\. Explain each plot\, particularly the one of tone\-strength vs time\.

Start with default values – tone/shock frequency at 3/5 Hz\, shock start time=250\. Note the tone and shock do not occur at the same time\. Then explain the trends in the plots you see\. You will notice that it spikes with every shock\, but not tone\. Why is that? Write down the reason in your notebook\.

YOUR CHALLENGE – You try to adjust the relevant parameters \(two frequencies and shock start time\) so that the tone by itself can make the neuron fire \(without the shock\)\. Note that you can change the parameter values either using the slider or you can type into the box\. If you type directly into the box\, make sure you press ‘Enter’\.

__Activity 3\. Tone and shock cause plasticity via Ca__  __2\+ __  __learning rule__  __\.__

__ 	__  __Let us know look into details by considering the mechanism by which the tone strength grows\, via the Hebbian plasticity rule\.  For this we run the __  __Colab__  __ D1\.3\.ipynb\. __

Load the Colab notebook titled “D1\.3\.ipynb” to research\.google\.com and do ‘Run All’ as usual\.  Write down on a separate sheet the plots you see and what they mean\. Explain each plot\, particularly the one of tone\-strength vs time\. The two new plots are of tone strength vs time\, and Ca2\+ \(calcium\) pool vs time\.

_What is the Ca_  _2\+ _  _pool inside the neuron?_ : With each tone\, a small amount of Ca2\+ enters the neuron\. Since Ca2\+ is harmful inside a cell\, it is continuously taken away in all cells \(‘extruded’\)\. However\, if the shock occurs close enough in time with the tone\, the amount of Ca2\+ that enters increases considerably\. This rise in calcium is what causes the tone strength to grow\.

2\. Start with default values – tone/shock frequency at 3/5 Hz\, shock start time=250; tone/shock strengths = 1/2\. Then explain the trends in the plots you see\. The calcium pool size goes up to 0\.2 which is not sufficient to increase the strength of the synapse\.

3\. YOUR CHALLENGE: Similar to what you did in D1\.2\, adjust the relevant parameters \(two frequencies\,  shock start time and initial strengths\) so that\, after training\, the tone by itself can make the neuron fire \(without the shock\)\. Note that this will happen only if the Ca2\+ pool size grows which then makes the strength to grow\. Also\, note that this happens only when tone and shock are ‘close’ to each other in time\.

__Modeling both the tone \(top\) and shock \(bottom\) pathways using the circuit model software__

![](img/How%20do%20Tone-Shock%20Pair5.png)

__CONCLUSION\. Amygdala is the key structure of the brain that stores various emotional memories in mammals\, including humans and rodents\. We modeled one neuron of the many in the amygdala that form a network\, with various sub\-regions storing different emotions such as reward\, fear\, etc\. __

![](img/How%20do%20Tone-Shock%20Pair6.png)

