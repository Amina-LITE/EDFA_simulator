
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

"""Import cross sections and generate required related data"""

def LoadCrossSectionData(WL_sig, WL_pump, WL_ase, Temp_sim):
    hp = 6.62607004e-34 # Planck constant m2kg/s
    c  = 299792458      # Speed of light in vacuum m/s
    NepersPerdB = 1/(10*np.log10(np.exp(1)))
    # defining path as raw string not normal string!
    file = r"fibers\M053301_cg.xlsx"
    #file = r"C:\Users\sal62519\Desktop\Python Simulator\Fibers\LSL_10422.xlsx "
    data_Xsec = pd.read_excel(file,sheet_name='CrossSection') #reading file
    WL_ref  = np.squeeze( data_Xsec[['Wavelength']] )
    Abs_ref = np.squeeze( data_Xsec[['Abs']] )*NepersPerdB     # convert dB/m to Np/m
    Ems_ref = np.squeeze( data_Xsec[['Ems']] )*NepersPerdB     # convert dB/m to Np/m
    Abs_interp = interp1d(WL_ref, Abs_ref, kind='linear')
    Ems_interp = interp1d(WL_ref, Ems_ref, kind='linear')
    WL = np.concatenate((WL_sig, WL_pump, WL_ase), axis=0)
    Abs   =  Abs_interp(WL)
    Ems   =  Ems_interp(WL)
    EmsSi =  Ems_interp(WL_sig)
    AbsSi =  Abs_interp(WL_sig)
    EmsPu =  Ems_interp(WL_pump)
    AbsPu =  Abs_interp(WL_pump)
    EmsEr =  Ems_interp(WL_ase)
    AbsEr =  Abs_interp(WL_ase)
    
        
    # fiber cross section temp 
    data_Param = pd.read_excel(file,sheet_name='Parameters') #reading file
    Temp       = np.squeeze(data_Param[['Temp']] )
    
    EmsSi, AbsSi =  XsecTempConv(EmsSi, AbsSi, Temp, Temp_sim)
    EmsPu, AbsPu =  XsecTempConv(EmsPu, AbsPu, Temp, Temp_sim)
    EmsEr, AbsEr =  XsecTempConv(EmsEr, AbsEr, Temp, Temp_sim)


    # defining path as raw string not normal string!
    file = r"fibers\M053301_cg.xlsx"
    #file = r"C:\Users\sal62519\Desktop\Python Simulator\Fibers\LSL_10422.xlsx "
    data_Param = pd.read_excel(file,sheet_name='Parameters') #reading file
   
    Loss     =  np.squeeze(data_Param[['BackgroundLoss']] )   # convert dB/m to Np/m
    bgls_Si  =  Loss*NepersPerdB*np.power(1550.0/WL_sig,4)
    EmsSi    =  EmsSi + bgls_Si
    AbsSi    =  AbsSi - bgls_Si
    bgls_Er  =  Loss*NepersPerdB*np.power(1550.0/WL_ase,4)
    EmsEr    =  EmsEr + bgls_Er
    AbsEr    =  AbsEr - bgls_Er
    bgls_Pu  =  Loss*NepersPerdB*np.power(1550.0/WL_pump,4)
    EmsPu    =  EmsPu + bgls_Pu
    AbsPu    =  AbsPu - bgls_Pu

    NU        = c/(WL*1e-9)        # Frquency array
    NU_ase    = c/(WL_ase*1e-9)    # ASE grid Frquency array
    # Delta nu array for ASE calulation. It is only calculated at ASE Wavelengths
    N_ase  = WL_ase.shape[0]
    DNU_ase = np.full((N_ase), 0.00)
    DNU_ase[0] = NU_ase[0]-NU_ase[1]
    DNU_ase[1:] = -np.diff(NU_ase)
    gstarhnudeltanu = 2*hp*np.multiply(np.multiply( EmsEr,DNU_ase),NU_ase) # 
    IsPump980 = np.full((len(WL),1),0)
    IsPump980[WL<1000] = 1
    
    CS=[]
    CS.append(AbsSi)
    CS.append(EmsSi)
    CS.append(AbsPu)
    CS.append(EmsPu)
    CS.append(AbsEr)
    CS.append(EmsEr)
    CS.append(gstarhnudeltanu)
    CS.append(NU)
    CS.append(IsPump980)
    
    return CS,gstarhnudeltanu

def XsecTempConv(EmsOLD, AbsOLD, TempOLD, TempNEW):
    # Input temperatures are Celcius. For calculations should be converted to Kelvin
    # This function converts giles parameters of certain temperatures to ones at another
    TempOLDK = TempOLD + 273.15 # Convert temerature to Kelvin
    TempNEWK = TempNEW + 273.15 # Convert temerature to Kelvin    
    AbsNEW = AbsOLD
    EmsNEW = EmsOLD
    return (EmsNEW,AbsNEW)

def LoadEDFParams():
    # defining path as raw string not normal string!
    file = r"fibers\M053301_cg.xlsx"
    #file = r"C:\Users\sal62519\Desktop\Python Simulator\Fibers\LSL_10422.xlsx "
    data_Param = pd.read_excel(file,sheet_name='Parameters') #reading file
    
    SatParam  = np.squeeze(data_Param[['SatParam']] )
    Loss      = np.squeeze(data_Param[['BackgroundLoss']] )/4.3429   # convert dB/m to Np/m
    ErPair    = np.squeeze(data_Param[['ErPairs']] )  
    Temp      = np.squeeze(data_Param[['Temp']] )
    Tau32     = np.squeeze(data_Param[['Tau32']] )
    Tau21     = np.squeeze(data_Param[['Tau21']] )
    Gamma     = np.squeeze(data_Param[['Gamma_Pump']] ) 

    Param = []    
    Param.append(SatParam)
    Param.append(Loss)
    Param.append(ErPair)
    Param.append(Temp)
    Param.append(Tau32)
    Param.append(Tau21)  
    Param.append(Gamma)

    return Param

def InitStates(NS):
    States = np.full((1,NS),0.5) # All states are set to 0.3    
    return States

def UpdateSSLevels(N2, NS, MNhat, VNhat, Epsilon, StepSize):     
    N2  = N2.reshape(1,NS)                              # 1 x NS matrix 
    VNhat2 = VNhat[0,0:NS].reshape(1,NS)                # 1 x NS matrix 
    MNhat2 = MNhat[0,0:NS].reshape(1,NS)                # 1 x NS matrix 
    N2  = N2 + StepSize*MNhat2/(np.sqrt(VNhat2)+Epsilon)
    N2  = np.clip(N2,0,1)
    return N2

def Calculate_SteadyState(N , PinSi, PinPu, PinEr, Param, CS, NS, L):
    #Nss = 0
    StepSize = 2e-2
    Epsilon  = 1e-10
    Beta1    = 0.9  # 
    Beta2    = 0.999  # 
    counter = 0 
    MAXCOUNTER = 1e4
    MN = np.full((1,NS),0)       # First  moment initial value
    VN = np.full((1,NS),0)       # Second moment initial value
    MNhat = np.full((1,NS),0)       # First  moment initial value
    VNhat = np.full((1,NS),0)       # Second moment initial value
    Beta1N    = 1  # 
    Beta2N    = 1  # 
    dNdt = Calculate_Derivative(N , PinSi, PinPu, PinEr ,Param, CS, NS, L)    
    NrmdN = np.linalg.norm(dNdt)    # 2-norm or Euclidean norm  equivalent to MATLAB norm(X)


    while (NrmdN>0.01):
        counter=counter+1
        #print(NrmdN)        
        MN    = Beta1*MN + (1-Beta1)*dNdt    # First Momentum Term Update
        VN    = Beta2*VN + (1-Beta2)*np.multiply(dNdt,dNdt)   # Second Momentum Term Update
        Beta1N = Beta1N * Beta1
        Beta2N = Beta2N * Beta2
        MNhat  =  MN/(1-Beta1N)  # First  moment initial value
        VNhat  =  VN/(1-Beta2N)
        StepSize_effective = StepSize 
        N = UpdateSSLevels(N, NS, MNhat, VNhat, Epsilon, StepSize_effective)                         # Update Steady state levels
        dNdt = Calculate_Derivative(N , PinSi, PinPu, PinEr ,Param, CS, NS, L)
        NrmdN = np.linalg.norm(dNdt)    # 2-norm or Euclidean norm  equivalent to MATLAB norm(X)
       
        if (counter == MAXCOUNTER):
            print('SteadyState could not converge in MAXCOUNTER iterations')
            NrmdN=-1    # Exit while loop  
            #print(N)  
    if (counter <MAXCOUNTER):
        print('Algorithm converged in less than MAXCOUNTER iterations:' + str(counter) )
        #print(N)
    return N    

def Calculate_Power(Nss , PinSi, PinPu, PinEr ,Param, CS, NS, L):
    #PoutSi=0
    #PoutEr=0
    #PoutPu=0
    N2 = Nss                # 1 x NS matrix 
    N2 = np.clip(N2,0,1)
    N1 = 1-N2
    N1 = np.clip(N1,0,1)
    
    N1 = N1.reshape(1,NS)
    N2 = N2.reshape(1,NS)
    
    #ONES  = np.full((1, NS), 1)
    loss   = Param[1]
    
    PoutSi = np.full( ( PinSi.shape[0] , NS+1) , 0.00 )
    PoutPu = np.full( ( PinPu.shape[0] , NS+1) , 0.00 )
    PoutEr = np.full( ( PinEr.shape[0] , NS+1) , 0.00 )
    PoutSi_eff = np.full( ( PinSi.shape[0] , NS+1) , 0.00 )
    PoutPu_eff = np.full( ( PinPu.shape[0] , NS+1) , 0.00 )
    PoutEr_eff = np.full( ( PinEr.shape[0] , NS+1) , 0.00 )
    
    PoutSi[:,0] = np.squeeze(PinSi)
    PoutPu[:,0] = np.squeeze(PinPu)
    PoutEr[:,0] = np.squeeze(PinEr)
    PoutSi_eff[:,0] = np.squeeze(PinSi)
    PoutPu_eff[:,0] = np.squeeze(PinPu)
    PoutEr_eff[:,0] = np.squeeze(PinEr)

    N_sig = int(0.5*PinSi.shape[0])
    N_pump= int(0.5*PinPu.shape[0])
    N_ase = int(0.5*PinEr.shape[0])
    AbsSi = CS[0].reshape(N_sig,1)      # 2xN-sig , 1 matrix
    AbsPu = CS[2].reshape(N_pump,1) 
    AbsEr = CS[4].reshape(N_ase,1) 
    EmsSi = CS[1].reshape(N_sig,1)      # 2xN-sig , 1 matrix
    EmsPu = CS[3].reshape(N_pump,1) 
    EmsEr = CS[5].reshape(N_ase,1) 
    gstarhnudeltanu = CS[6].reshape(N_ase,1) 
    g_Si = -np.dot(AbsSi,N1) +np.dot(EmsSi,N2) - loss
    g_Er = -np.dot(AbsEr,N1) +np.dot(EmsEr,N2) - loss
    g_Pu = -np.dot(AbsPu,N1) +np.dot(EmsPu,N2) - loss 
    g_Si_eff = -np.dot(AbsSi,N1) +np.dot(EmsSi,N2) 
    g_Er_eff = -np.dot(AbsEr,N1) +np.dot(EmsEr,N2) 
    g_Pu_eff = -np.dot(AbsPu,N1) +np.dot(EmsPu,N2)
    G_Si = np.exp(g_Si*L/NS)
    G_Pu = np.exp(g_Pu*L/NS)
    G_Er = np.exp(g_Er*L/NS)
    G_Si_eff = np.exp(g_Si_eff*L/NS)
    G_Pu_eff = np.exp(g_Pu_eff*L/NS)
    G_Er_eff = np.exp(g_Er_eff*L/NS)

    ASE =  np.divide( np.multiply(np.dot(gstarhnudeltanu,N2), G_Er-1) , g_Er)
    G_Si_fb = np.concatenate((G_Si,np.fliplr(G_Si)),axis=0)
    G_Pu_fb = np.concatenate((G_Pu,np.fliplr(G_Pu)),axis=0)
    G_Er_fb = np.concatenate((G_Er,np.fliplr(G_Er)),axis=0)
    G_Si_fb_eff = np.concatenate((G_Si_eff,np.fliplr(G_Si_eff)),axis=0)
    G_Pu_fb_eff = np.concatenate((G_Pu_eff,np.fliplr(G_Pu_eff)),axis=0)
    G_Er_fb_eff = np.concatenate((G_Er_eff,np.fliplr(G_Er_eff)),axis=0)
    ASE_fb  = np.concatenate((ASE,np.fliplr(ASE)),axis=0)

    for index in range(NS):
        PoutSi[:,index+1] = np.multiply(PoutSi[:,index], G_Si_fb[:,index]) 
        PoutPu[:,index+1] = np.multiply(PoutPu[:,index], G_Pu_fb[:,index]) 
        PoutEr[:,index+1] = np.multiply(PoutEr[:,index], G_Er_fb[:,index]) + ASE_fb[:,index]
        PoutSi_eff[:,index+1] = np.multiply(PoutSi_eff[:,index], G_Si_fb_eff[:,index]) 
        PoutPu_eff[:,index+1] = np.multiply(PoutPu_eff[:,index], G_Pu_fb_eff[:,index]) 
        PoutEr_eff[:,index+1] = np.multiply(PoutEr_eff[:,index], G_Er_fb_eff[:,index]) + ASE_fb[:,index]
    PoutSi[N_sig:2*N_sig,:] =  np.fliplr(PoutSi[N_sig:2*N_sig,:]) 
    PoutPu[N_pump:2*N_pump,:] =  np.fliplr(PoutPu[N_pump:2*N_pump,:]) 
    PoutEr[N_ase:2*N_ase,:] =  np.fliplr(PoutEr[N_ase:2*N_ase,:]) 
    PoutSi_eff[N_sig:2*N_sig,:] =  np.fliplr(PoutSi_eff[N_sig:2*N_sig,:]) 
    PoutPu_eff[N_pump:2*N_pump,:] =  np.fliplr(PoutPu_eff[N_pump:2*N_pump,:]) 
    PoutEr_eff[N_ase:2*N_ase,:] =  np.fliplr(PoutEr_eff[N_ase:2*N_ase,:]) 
       
    return (PoutSi, PoutPu, PoutEr,PoutSi_eff, PoutPu_eff, PoutEr_eff)

def Calculate_Derivative(Nss , PinSi, PinPu, PinEr ,Param, CS, NS, L):
    #dNdt=0
    hp = 6.62607004e-34 # Planck constant m2kg/s
    c  = 299792458      # Speed of light in vacuum m/s
    N2 = Nss                # 1 x NS matrix 
    N2 = np.clip(N2,0,1)
    N1 = 1-N2
    N1 = np.clip(N1,0,1)
    
    N1 = N1.reshape(1,NS)
    N2 = N2.reshape(1,NS)
    dN2dt  = np.full((1, NS), 0)
    
    N_sig = int(0.5*PinSi.shape[0])
    N_pump= int(0.5*PinPu.shape[0])
    N_ase = int(0.5*PinEr.shape[0])
    N_all = N_sig + N_pump + N_ase

    Ksat    = Param[0]
    loss    = Param[1]
    ErPairs = Param[2]     #  percent pairs 
    Temp    = Param[3]
    tau32   = Param[4]
    tau21   = Param[5]

    NU = CS[7].reshape(N_all,1) 
    IsPump980 = CS[8].reshape(N_all,1)
    ONES  = np.full((1, NS), 1)
    IsPump980 = np.dot(IsPump980,ONES) 
    Coeffs  = 1/(hp*Ksat*NU)    
    Coeffs  = np.dot(Coeffs,ONES)
    DL = L/NS
    DLT=tau21*L/NS
    Ncurrent = N2
    PoutSi, PoutPu, PoutEr,PoutSi_eff, PoutPu_eff, PoutEr_eff = Calculate_Power(Ncurrent , PinSi, PinPu, PinEr ,Param, CS, NS, L)
    
    DP_Si   = PoutSi_eff[0:N_sig,1:NS+1] - PoutSi_eff[0:N_sig,0:NS] + PoutSi_eff[N_sig:2*N_sig,0:NS] - PoutSi_eff[N_sig:2*N_sig,1:NS+1]
    DP_Pu   = PoutPu_eff[0:N_pump,1:NS+1] - PoutPu_eff[0:N_pump,0:NS] + PoutPu_eff[N_pump:2*N_pump,0:NS] - PoutPu_eff[N_pump:2*N_pump,1:NS+1]
    DP_Er   = PoutEr_eff[0:N_ase,1:NS+1] - PoutEr_eff[0:N_ase,0:NS] + PoutEr_eff[N_ase:2*N_ase,0:NS] - PoutEr_eff[N_ase:2*N_ase,1:NS+1]
    DP      = np.concatenate((DP_Si, DP_Pu, DP_Er), axis=0)
    #DP      = Pout[0:len(WL),1:NR+1] - Pout[0:len(WL),0:NR] + Pout[len(WL):2*len(WL),0:NR] - Pout[len(WL):2*len(WL),1:NR+1]
    Pave_Si    = PoutSi[0:N_sig,0:NS] + PoutSi[N_sig:2*N_sig,0:NS]
    Pave_Pu    = PoutPu[0:N_pump,0:NS] + PoutPu[N_pump:2*N_pump,0:NS]
    Pave_Er    = PoutEr[0:N_ase,0:NS] + PoutEr[N_ase:2*N_ase,0:NS]
    Pave       = np.concatenate((Pave_Si, Pave_Pu, Pave_Er), axis=0)
    #Pave    = Pout[0:len(WL),0:NR] + Pout[len(WL):2*len(WL),0:NR]
    dPdZ980 = np.multiply(DP,np.multiply(Coeffs,IsPump980)) /DLT
    dPdZ1550= np.multiply(DP,np.multiply(Coeffs,1-IsPump980)) /DLT
    SumdPdZ980 = np.sum(dPdZ980, axis=0) 
    SumdPdZ980 = SumdPdZ980.reshape(1,NS)
    SumdPdZ1550 = np.sum(dPdZ1550, axis=0) 
    SumdPdZ1550 = SumdPdZ1550.reshape(1,NS)
    AbsPu = CS[2].reshape(N_pump,1)       
         
    dN2dt    = -(N2/tau21)   - SumdPdZ1550  - SumdPdZ980                
    return dN2dt 

