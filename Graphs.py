import numpy as np
from matplotlib import pyplot as plt

def general_Plot(Probe,ProbeName): 
    #print(Probe)
    #Need to work on the format for probe to extract a plottable list 

    plt.plot(Probe[1] , 10*np.log10(Probe[0]),'-or' ,color='blue')
    plt.grid()
    plt.title(ProbeName)
    plt.xlabel('Wavelength [ nm ]', fontsize = 14)
    plt.ylabel('Gain [ dB ]', fontsize = 14)
    plt.show()
