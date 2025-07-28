import os
import numpy as np
from scipy.optimize import curve_fit
import ultraplot as uplt

def func(x, kcat, km):
    return kcat*x/(km+x)

pplt.rc.update({'cycle': 'FlatUI'})

pb_closed = [0.003, 0.007, 0.02, 0.05, 0.15, 0.31, 0.53, 0.73]
dv = ["3.1-4.8", "3.4-5.3", "3.8-5.9", "4.2-6.6", "4.7-7.3", "5.1-7.9", "5.7-8.5", "6.3-9.1"]

kcat_mean = [[], []]
kcat_std = [[], []]
km_mean = [[], []]
km_std = [[], []]

for i, elem in enumerate(dv):
    infile1 = f"./dv0-{elem:s}/turnover_rate.dat"
    infile2 = f"./dv-{elem:s}/turnover_rate.dat"

    x1, y1 = np.loadtxt(infile1, usecols=(0, 2), unpack=True)
    x2, y2 = np.loadtxt(infile2, usecols=(0, 2), unpack=True)
    # print(x1.shape, infile1)
    # print(x2.shape, infile2)

    x1 = x1*0.001*300/0.00635
    x2 = x2*0.001*300/0.00635

    num = 20
    ind1 = np.arange(x1.shape[0])
    ind2 = np.arange(x2.shape[0])
    kcat1_fit = []
    kcat2_fit = []
    km1_fit = []
    km2_fit = []

    for i in range(num):
        np.random.shuffle(ind1)
        np.random.shuffle(ind2)
        param1, param1_cov = curve_fit(func, x1[ind1[:6]], y1[ind1[:6]])
        param2, param2_cov = curve_fit(func, x2[ind2[:6]], y2[ind2[:6]])
        kcat1_fit.append(param1[0])
        kcat2_fit.append(param2[0])
        km1_fit.append(param1[1])
        km2_fit.append(param2[1])

    kcat1_fit = np.array(kcat1_fit)
    kcat2_fit = np.array(kcat2_fit)
    km1_fit = np.array(km1_fit)
    km2_fit = np.array(km2_fit)

    kcat_mean[0].append( np.mean(kcat1_fit) )
    kcat_mean[1].append( np.mean(kcat2_fit) )
    kcat_std[0].append( np.std(kcat1_fit) )
    kcat_std[1].append( np.std(kcat2_fit) )

    km_mean[0].append( np.mean(km1_fit) )
    km_mean[1].append( np.mean(km2_fit) )
    km_std[0].append( np.std(km1_fit) )
    km_std[1].append( np.std(km2_fit) )

fig, axs = uplt.subplots(ncols=1, nrows=2, refheight="3cm", refaspect=1.0, sharex=4, sharey=False, hspace=0.9)

axs[0].plot(pb_closed, kcat_mean[0], lw=1.5, c="C0", ls='-', marker='o', ms=5, bardata=kcat_std[0])
axs[0].plot(pb_closed, kcat_mean[1], lw=1.5, c="C1", ls='--', marker='o', ms=5, bardata=kcat_std[1])
axs[1].plot(pb_closed, km_mean[0], lw=1.5, c="C0", ls='-', marker="o", ms=5, bardata=km_std[0])
axs[1].plot(pb_closed, km_mean[1], lw=1.5, c="C1", ls='--', marker="o", ms=5, bardata=km_std[0])

axs.format(xlabel='$P_{closed}$', xscale='logit', xlim=[0.007, 0.86])
axs[0].format(ylabel='$k_{cat}\ (ms^{-1})$')
axs[1].format(ylabel='$K_{M}\ (\mu M)$', yticks=[100, 300, 500])
axs[0].format(xlim=[0.002, 0.95], ylim=[0.11, 0.46], xscale='log', yticks=0.1)
axs.format(grid=False)

fig.savefig("fig3_BC.png", dpi=600)
fig.savefig("fig3_BC.svg")
fig.savefig("fig3_BC.pdf")
uplt.show()
