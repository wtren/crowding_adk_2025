import os
import sys
import numpy as np
import scipy.stats as ss
import glob

def fpt1(traj, dt):
    state1, state2 = 'OOEE', 'CCTM'
    nf = len(traj)
    # print(nf)
    if(state1 not in traj or state2 not in traj):
        print("Error! No substrates binding event in this trajectory!")
    else:
        i0 = traj.index(state1)
        # print(i0)
        while(i0 < nf):
            if(state2 not in traj[i0+1:]):
                print("Caution! No cycle in this trajectory!")
                break
            else:
                i1 = traj[i0+1:].index(state2)
                dt.append(i1)
                # print(i1)
                i1 = i1 + i0 + 1
                if(state1 in traj[i1+1:]):
                    i0 = traj[i1+1:].index(state1) + i1 + 1
                else:
                    break

def fpt2(traj0, dt):
    traj = []
    state1, state2 = 'B', 'E'
    for elem in traj0:
        if elem == 'CCDD':
            traj.append('B')
        elif elem[2:] in ['DE', 'DM', 'ED', 'TD']:
        # elif elem == 'CCTM':
            traj.append('I')
        elif(elem[0:2] != 'CC' and (elem[2:] in ['EE', 'EM', 'TE'])):
            traj.append('E')
        else:
            traj.append('X')

    nf = len(traj)
    # print(nf)
    if(state1 not in traj or state2 not in traj):
        print("Error! No substrates binding event in this trajectory!")
    else:
        i0 = traj.index(state1)
        # print(i0)
        while(i0 < nf):
            if(state2 not in traj[i0+1:]):
                print("Caution! No cycle in this trajectory!")
                break
            else:
                i1 = traj[i0+1:].index(state2)
                # dt.append(i1)
                if 'I' in traj[i0+1:i0+1+i1]:
                    dt.append(i1)
                    # print("zz")
                    # print(i1)
                i1 = i1 + i0 + 1
                if(state1 in traj[i1+1:]):
                    i0 = traj[i1+1:].index(state1) + i1 + 1
                else:
                    break



chi_closed = 0.5
# dir = "/home/wtren/Works/adk_crowding/jjlu_data/fig6/P_0.003"
# dir1 = "/media/wtren/Elements1/jjlu/fig5/chem-crowd-ref--3.1--4.8"
# dir2 = "/media/wtren/Elements1/jjlu/fig5/chem-crowd-ref--3.1--4.8-p2"
# conc_of_sub = [0.1, 0.5, 2.0, 4.0, 6.0, 10.0, 14.0, 18.0, 24.0, 32.0]

conc_of_sub = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0]

data1 = []
data2 = []
mdstep2time = 0.5*112/10**5
cc_factor = 0.001*300/0.00635

# fpath1 = "/media/wtren/One Touch/ADK_crowding/jjlu_data/fig6/"
# fpath2 = "V0.0_P0.003/"
# fpath2 = "V0.0_P0.3/"
# fpath2 = "V0.3_P0.003/"
# fpath2 = "V0.3_P0.3/"

fpath1 = "/media/wtren/One Touch/ADK_crowding/jjlu_data/fig4/"
fpath2 = "V_0.3/"
pb = [0.730, 0.540, 0.310, 0.150, 0.050, 0.020, 0.007, 0.003]



for idx, cc in enumerate(conc_of_sub):
    # files = glob.glob(os.path.join(dir, f"data-{cc:.1f}_*"))
    files = glob.glob(fpath1+fpath2+f"data-{cc:.1f}_*")
    print(files)

    dt_binding = []
    dt_unbinding = []

    for filename in files:
        print(filename)
        ss1_lists = []
        ss2_lists = []
        with open(filename, "r") as fp:
            for line in fp.readlines()[2:]:
                tmp = line.split()
                state_of_sub1 = tmp[4].strip()
                state_of_sub2 = tmp[5].strip()

                state_of_amp = 'O'
                state_of_lid = 'O'

                if(float(tmp[1]) > chi_closed ):
                    state_of_lid = 'C'
                if(float(tmp[2]) > chi_closed):
                    state_of_amp = 'C'
                ss1 = state_of_lid + state_of_amp + state_of_sub1 + state_of_sub2
                    
                # if((state_of_lid == 'C' and state_of_amp == 'C') and \
                #     (state_of_sub1 == 'D' and state_of_sub2 == 'D')):
                #     ss2 = "CB"
                # elif((state_of_lid != 'C' or state_of_amp != 'C') and \
                #     (state_of_sub1 != 'D' or state_of_sub2 != 'D')):
                # elif(state_of_sub2 != 'D'):
                #     ss2 = "OU"
                # else:
                #     ss2 = "XX"
                ss1_lists.append(ss1)
                # ss2_lists.append(ss2)
            # print(ss_lists)

        fpt1(ss1_lists, dt_binding)
        fpt2(ss1_lists, dt_unbinding)
        
    # data1.append([cc*cc_factor, np.mean(dt_binding)*mdstep2time, np.std(dt_binding)*mdstep2time])
    # data2.append([cc*cc_factor, np.mean(dt_unbinding)*mdstep2time, np.std(dt_unbinding)*mdstep2time])

    data1.append([pb[idx], np.mean(dt_binding)*mdstep2time, np.std(dt_binding)*mdstep2time])
    data2.append([pb[idx], np.mean(dt_unbinding)*mdstep2time, np.std(dt_unbinding)*mdstep2time])

data1 = np.array(data1)
data2 = np.array(data2)
np.savetxt(fpath2[:-1]+"_binding_mfpt.txt", data1, fmt="%8.3f")
np.savetxt(fpath2[:-1]+"_unbinding_mfpt.txt", data2, fmt="%8.3f")
