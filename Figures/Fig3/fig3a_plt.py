import os
import numpy as np
from scipy.optimize import curve_fit
import ultraplot as uplt

def func(x, kcat, km):
    return kcat*x/(km+x)

# uplt.rc.cycle = '538'
# uplt.rc.update({'fontsize': 14})
uplt.rc.update({'cycle': 'FlatUI'})
# uplt.rc.update({'gridminor.linewidth': 0.1})

dv = ["3.4-5.3", "4.2-6.6", "5.1-7.9", "6.3-9.1"]
pb_closed = [0.007, 0.05, 0.30, 0.73]

X = [[], []]
Y = [[], []]
Y_fit = [[], []]

for i, elem in enumerate(dv):
    infile1 = f"./dv0-{elem:s}/turnover_rate.dat" 
    infile2 = f"./dv-{elem:s}/turnover_rate.dat" 
    # print(infile1, infile2)

    x1, y1 = np.loadtxt(infile1, usecols=(0, 2), unpack=True)
    x2, y2 = np.loadtxt(infile2, usecols=(0, 2), unpack=True)
    x1 = x1*0.001*300/0.00635
    x2 = x2*0.001*300/0.00635

    param1, param1_cov = curve_fit(func, x1, y1)
    param2, param2_cov = curve_fit(func, x2, y2)
    y1_fit = func(x1, param1[0], param1[1])
    y2_fit = func(x2, param2[0], param2[1])

    X[0].append(x1)
    X[1].append(x2)
    Y[0].append(y1)
    Y[1].append(y2)
    Y_fit[0].append(y1_fit)
    Y_fit[1].append(y2_fit)

nm = len(dv)
fig, axs = uplt.subplots(ncols=2, nrows=2, refheight="3cm", refaspect=1.0, sharex=4, sharey=4, wspace=0.9, hspace=0.9)

for i in range(nm):
    axs[i].scatter(X[0][i], Y[0][i], marker='o', s=24, c=f"C0", label="w/o crowder")
    axs[i].plot(X[0][i], Y_fit[0][i], lw=1.5, c=f"C0")
    axs[i].scatter(X[1][i], Y[1][i], marker='o', s=24, c=f"C1", label="with crowder")
    axs[i].plot(X[1][i], Y_fit[1][i], lw=1.5, ls='--', c=f"C1")
    # axs[i].format(title="$P_{closed}=%.3f$" % pb_closed[i])
    axs[i].text(470, 0.04, "$P_{closed}=%.3f$" % pb_closed[i])

axs.format(xlabel='[ATP] ($\mu$M)', ylabel='Turnover rate (ms$^{-1}$)')
axs.format(xlim=[-40, 1560], ylim=[-0.02, 0.46], xticks=500, xminorticks=250)
axs.format(yticks=0.1, yminorticks=0.05)
axs.format(grid=False)

axs[3].legend(loc='ul', ncols=1, frameon=False, handletextpad=0.0, columnspacing=0)
# axs[0].legend(loc='lr', ncol=3, frameon=True, columnspacing=0.5, labelspacing=0.5, handletextpad=-0.1, a=0.8, borderpad=0.3)
fig.savefig("fig3A.png", dpi=600)
fig.savefig("fig3A.svg")
fig.savefig("fig3A.pdf")
uplt.show()
