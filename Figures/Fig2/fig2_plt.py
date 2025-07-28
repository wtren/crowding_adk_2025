import os
import numpy as np
from scipy.optimize import curve_fit
import proplot as pplt

def func(x, kcat, km):
    return kcat*x/(km+x)

# pplt.rc.cycle = '538'
# pplt.rc.update({'fontsize': 14})
pplt.rc.update({'cycle': 'Qual1'})

volume_frac = [0.0, 0.1, 0.2, 0.3, 0.4]
lab1 = ["V=0.0", "V=0.1", "V=0.2", "V=0.3", "V=0.4"]
lab2 = ["0.0", "0.1", "0.2", "0.3", "0.4"]

conc_atp = []
kv = [] 
kcat_mean = []
kcat_std = []
km_mean = []
km_std = []

x1 = []
y1 = []
y1_fit = []

# print(path)
for vf in volume_frac:
    infile = f"./v_{vf}/turnover_rate.dat"
    xi, yi = np.loadtxt(infile, usecols=(0, 2), unpack=True)
    xi = xi*0.001*300/0.00635
    conc_atp.append(xi)
    kv.append(yi)
    param0, param0_cov = curve_fit(func, xi, yi)
    yi_fit = func(xi, param0[0], param0[1])
    # print(vf, param0)
    x1.append(xi)
    y1.append(yi)
    y1_fit.append(yi_fit)

    num = 20
    ind = np.arange(xi.shape[0])
    # print(ind.shape)
    kcat_fit = []
    km_fit = []
    for i in range(num):
        np.random.shuffle(ind)
        param1, param1_cov = curve_fit(func, xi[ind[:6]], yi[ind[:6]])
        kcat_fit.append(param1[0])
        km_fit.append(param1[1])

    kcat_fit = np.array(kcat_fit)
    km_fit = np.array(km_fit)
    # print(vf, kcat_fit, km_fit)

    kcat_mean.append( np.mean(kcat_fit) )
    kcat_std.append( np.std(kcat_fit) )

    km_mean.append( np.mean(km_fit) )
    km_std.append( np.std(km_fit) )

# fig, axs = pplt.subplots(ncols=3, nrows=1, refwidth='4cm', sharex=False, sharey=False, refaspect=1, wspace=4.5)
fig, axs = pplt.subplots(ncols=3, nrows=1, refwidth='5cm', sharex=False, sharey=False, refaspect=1.2, wspace=4.7)

for i in range(len(volume_frac)):
    if i == 0:
        axs[0].scatter(x1[i], y1[i], marker='o', s=16, label=lab2[i], c='k')
        axs[0].plot(x1[i], y1_fit[i], lw=1.5, c='k')
    else:
        axs[0].scatter(x1[i], y1[i], marker='o', s=16, label=lab2[i], c=f'C{i-1}')
        axs[0].plot(x1[i], y1_fit[i], lw=1.5, c=f'C{i-1}')
# axs[0].scatter(xi, y0, marker='o', label='1')
# axs[0].plot(xi, y1, lw=1.5)
# ax.plot(x, x, lw=2, label='2')
print(kcat_std)
print(km_std)
axs[1].plot(volume_frac, kcat_mean, lw=1.4, marker='o', bardata=kcat_std)
axs[2].plot(volume_frac, km_mean, lw=1.4, marker='o', bardata=km_std)

axs[0].format(xlim=[-40, 1560], ylim=[0, 0.4], xlabel='[ATP] ($\mu$M)', ylabel='Turnover rate (ms$^{-1}$)')
axs[1].format(xlabel='$\phi$', ylabel='$k_{cat}$ (ms$^{-1}$)')
axs[1].format(xlim=[-0.02, 0.42], ylim=[0.1, 0.42], xticks=0.1, xminorticks=[], yticks=0.1)
axs[2].format(xlabel='$\phi$', ylabel='$K_{M}$ ($\mu M$)')
axs[2].format(xlim=[-0.02, 0.42], xticks=0.1, xminorticks=[])
axs[0].legend(loc='lr', ncol=3, frameon=True, columnspacing=0.5, labelspacing=0.5, handletextpad=-0.1, a=0.8, borderpad=0.3)

axs.format(grid=False)

fig.savefig("fig2.png", dpi=600)
fig.savefig("fig2.svg")
fig.savefig("fig2.pdf")
pplt.show()
