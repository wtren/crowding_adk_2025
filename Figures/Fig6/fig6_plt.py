import os
import numpy as np
import ultraplot as uplt

# uplt.rc.cycle = '538'
uplt.rc.update({'legend.fontsize': 12})
uplt.rc.update({'cycle': 'FlatUI'})

dir2 = ["./data/V0.0_P0.003_", 
        "./data/V0.0_P0.3_", 
        "./data/V0.3_P0.003_", 
        "./data/V0.3_P0.3_", 
        "./data/V_0.0_", 
        "./data/V_0.3_"]

binding_rate = []
unbinding_rate = []
turnover_rate = []

for i, elem in enumerate(dir2):

    fn1 = elem + "binding_mfpt.txt"
    fn2 = elem + "unbinding_mfpt.txt"
    fn3 = elem + "turnover_rate.dat"
    
    if(i<4):
        data1 = np.loadtxt(fn1, skiprows=2)
        data2 = np.loadtxt(fn2, skiprows=2)
        data3 = np.loadtxt(fn3, skiprows=2)
    else:
        data1 = np.loadtxt(fn1, skiprows=1)
        data2 = np.loadtxt(fn2, skiprows=1)
        data3 = np.loadtxt(fn3, skiprows=1)
    print(i, data1, data2, data3)

    binding_rate.append(data1)
    unbinding_rate.append(data2)
    turnover_rate.append(data3)

fig, axs = uplt.subplots(ncols=3, nrows=2, refheight='4cm', sharex=False, sharey=0, refaspect=1.2, wspace=4.0, hspace=4.0)
# axs_new = axs.flatten()

im1 = axs[0].plot(binding_rate[0][:, 0], binding_rate[0][:, 1], ls='--', marker='s', s=5, c='C0', label="substrate binding (w/o crowding)")
im2 = axs[0].plot(binding_rate[2][:, 0], binding_rate[2][:, 1], ls='-', marker='o', s=5, c='C0', label="substrate binding (with crowding)")
im3 = axs[0].plot(turnover_rate[0][:, 0], 1./turnover_rate[0][:, 3], ls='--', marker='s', s=5, c='C2', label="catalytic cycle (w/o crowding)")
im4 = axs[0].plot(turnover_rate[2][:, 0], 1./turnover_rate[2][:, 3], ls='-', marker='o', s=5, c='C2', label="catalytic cycle (with crowding)")
axs[0].format(yticks=[1, 10], ylim=[0.3, 120])

axs[1].plot(binding_rate[1][:, 0], binding_rate[1][:, 1], ls='--', marker='s', s=5, c='C0')
axs[1].plot(binding_rate[3][:, 0], binding_rate[3][:, 1], ls='-', marker='o', s=5, c='C0')
axs[1].plot(turnover_rate[1][:, 0], 1./turnover_rate[1][:, 3], ls='--', marker='s', s=5, c='C2')
axs[1].plot(turnover_rate[3][:, 0], 1./turnover_rate[3][:, 3], ls='-', marker='o', s=5, c='C2')
axs[1].format(yticks=[1, 10], ylim=[0.2, 13])

axs[2].plot(binding_rate[4][:, 0], binding_rate[4][:, 1], ls='--',  marker='s', s=5, c='C0')
axs[2].plot(binding_rate[5][:, 0], binding_rate[5][:, 1], ls='-',  marker='o', s=5, c='C0')
axs[2].plot(turnover_rate[4][:, 0], 1./turnover_rate[4][:, 3], ls='--',  marker='s', s=5, c='C2')
axs[2].plot(turnover_rate[5][:, 0], 1./turnover_rate[5][:, 3], ls='-',  marker='o', s=5, c='C2')
axs[2].format(yticks=[1, 10], ylim=[0.2, 15])

im5 = axs[3].plot(unbinding_rate[0][:, 0], unbinding_rate[0][:, 1], ls='--',  marker='s', s=5, c='C1', label="product release (w/o crowding)")
im6 = axs[3].plot(unbinding_rate[2][:, 0], unbinding_rate[2][:, 1], ls='-',  marker='o', s=5, c='C1', label="product release (with crowding)")
axs[3].plot(turnover_rate[0][:, 0], 1./turnover_rate[0][:, 3], ls='--',  marker='s', s=5, c='C2')
axs[3].plot(turnover_rate[2][:, 0], 1./turnover_rate[2][:, 3], ls='-',  marker='o', s=5, c='C2')
axs[3].format(yticks=[1, 10], ylim=[0.3, 120])

axs[4].plot(unbinding_rate[1][:, 0], unbinding_rate[1][:, 1], ls='--',  marker='s', s=5, c='C1')
axs[4].plot(unbinding_rate[3][:, 0], unbinding_rate[3][:, 1], ls='-',  marker='o', s=5, c='C1')
axs[4].plot(turnover_rate[1][:, 0], 1./turnover_rate[1][:, 3], ls='--',  marker='s', s=5, c='C2')
axs[4].plot(turnover_rate[3][:, 0], 1./turnover_rate[3][:, 3], ls='-',  marker='o', s=5, c='C2')
axs[4].format(yticks=[1, 10], ylim=[0.2, 13])

axs[5].plot(unbinding_rate[4][:, 0], unbinding_rate[4][:, 1], ls='--',  marker='s', s=5, c='C1')
axs[5].plot(unbinding_rate[5][:, 0], unbinding_rate[5][:, 1], ls='-',  marker='o', s=5, c='C1')
axs[5].plot(turnover_rate[4][:, 0], 1./turnover_rate[4][:, 3], ls='--',  marker='s', s=5, c='C2')
axs[5].plot(turnover_rate[5][:, 0], 1./turnover_rate[5][:, 3], ls='-',  marker='o', s=5, c='C2')
axs[5].format(yticks=[1, 10], ylim=[0.2, 15])

axs.format(xscale='log', yscale='log')
axs[0].format(ylabel='MFPT (ms)', xlabel='[ATP] ($\mu$M)')
axs[0].format(xlim=[80, 1900], xticks=[100, 200, 500, 1000, 1600], xminorticks=100)

axs[1].format(ylabel='MFPT (ms)', xlabel='[ATP] ($\mu$M)')
axs[1].format(xlim=[80, 1900], xticks=[100, 200, 500, 1000, 1600], xminorticks=100)

axs[2].format(ylabel='MFPT (ms)', xlabel='$P_{closed}$', xlim=[0.002, 1.0])
# axs[2].format(xlim=[80, 1900], xticks=[100, 200, 500, 1000, 1600], xminorticks=100)

axs[3].format(ylabel='MFPT (ms)', xlabel='[ATP] ($\mu$M)')
axs[3].format(xlim=[80, 1900], xticks=[100, 200, 500, 1000, 1600], xminorticks=100)

axs[4].format(ylabel='MFPT (ms)', xlabel='[ATP] ($\mu$M)')
axs[4].format(xlim=[80, 1900], xticks=[100, 200, 500, 1000, 1600], xminorticks=100)

axs[5].format(ylabel='MFPT (ms)', xlabel='$P_{closed}$', xlim=[0.002, 1.0])
# axs[5].format(xlim=[80, 1900], xticks=[100, 200, 500, 1000, 1600], xminorticks=100)
axs.format(grid=False)

hs = [im1, im2, im3, im4, im5, im6]
fig.legend(hs, ncols=2, center=True, frame=False, loc='b', col=2)

fig.savefig("fig6.png", dpi=600)
fig.savefig("fig6.pdf")
fig.savefig("fig6.svg")
uplt.show()
