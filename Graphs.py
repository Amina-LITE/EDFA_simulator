import numpy as np
from matplotlib import pyplot as plt

def Gain_plot(Probe): 
    print(Probe)
    #Need to work on the format for probe to extract a plottable list 
    '''
    Gain = 10*np.log10( poutamp[0:settings.N_sig]/np.squeeze(settings.Signalf.T ))
    plt.plot(settings.WL_sig , 10*np.log10( poutamp[0:settings.N_sig]/np.squeeze(settings.Signalf.T )),'-or' )
    plt.grid()
    plt.xlabel('Wavelength [ nm ]', fontsize = 14)
    plt.ylabel('Gain [ dB ]', fontsize = 14)
    #plt.xlim(WL_sig_start-5,WL_sig_stop+5)
    plt.show()
    '''