import numpy as np
import simulation_engine as sim
import Settings as settings
import new_amp as ap
from matplotlib import pyplot as plt


GFF=[]
for i in range(4):
    # amp array where all the component objects are added to
    amp = []

    sim.createsourcelayer(ap.OpticalSource, amp)

    sim.calcualte_pump(ap.OpticalPump)

    sim.createcomponentlayer(ap.OpticalComponent, amp,GFF)

    component = amp[-1]
    poutamp = component.getOutputForward()

    Gain = poutamp[0:settings.N_sig]/np.squeeze(settings.Signalf.T )

    
    GFF = Gain -min(Gain)


plt.plot(settings.WL_sig , 10*np.log10( poutamp[0:settings.N_sig]/np.squeeze(settings.Signalf.T )),'-or' )
plt.grid()
plt.xlabel('Wavelength [ nm ]', fontsize = 14)
plt.ylabel('Gain [ dB ]', fontsize = 14)
plt.title("Total Amplifier Gain")
#plt.xlim(WL_sig_start-5,WL_sig_stop+5)
plt.show()






