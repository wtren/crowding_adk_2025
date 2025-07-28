import numpy as np
import ultraplot as uplt
from scipy.optimize import curve_fit

def func(x, kcat, km):
    return kcat*x/(km+x)

# uplt.rc.cycle = 'FlatUI'
uplt.rc.cycle = '538'

dirs = [[
        "./dilute/", \
        "./exv_V0.1/", \
        "./e0.2_V0.1/", \
        "./e0.3_V0.1/"
        ], 
        [
        "./dilute/", \
        "./e0.1_V0.2/", \
        "./e0.2_V0.2/", \
        "./e0.3_V0.2/"
        ],
        [
        "./dilute/", \
        "./exv_V0.3/", \
        "./e0.2_V0.3/", \
        "./e0.3_V0.3/"
        ]]

conc_factor = 0.001*300/0.00635
labs = ['dilute', 'inert', 
        '$\epsilon_{attr}$=0.2', 
        '$\epsilon_{attr}$=0.3']
num1 = 6
fig, axs = uplt.subplots(ncols=3, nrows=1, refwidth="4cm", refaspect=1, wspace=0.7)
colors = ['k', 'r', 'C3', 'C2']
styles = ['-', '-', '--', '--', '--', '--']
markers = ['o', 'o', 'x', 'x', 'x', 'x']
for j in range(3):
    for i in range( len(dirs[j]) ):
        infn = dirs[j][i] + "turnover_rate.dat"
        xi, yi = np.loadtxt(infn, usecols=(0, 2), unpack=True)
        xi *= conc_factor
        param0, param0_cov = curve_fit(func, xi, yi)
        yi_fit = func(xi, param0[0], param0[1])
        if(j == 0):
            axs[j].plot(xi, yi_fit, lw=1.3, color=colors[i], label=labs[i])
        else:
            axs[j].plot(xi, yi_fit, lw=1.3, color=colors[i])
        axs[j].scatter(xi, yi, marker='o', s=12, color=colors[i])

axs.format(xlabel='[ATP] ($\mathrm{\mu}$M)')
axs.format(ylabel='Turnover rate (ms$^{-1}$)')
# axs.legend(ncol=1, frameon=False)

axs[0].legend(ncol=1, frameon=False)
# fig.legend(ncol=4, frameon=False, loc='t')
# axs.format(ylim=[0, 0.41], yticks=0.1)
axs.format(xlim=[-40, 1570], yticks=0.1)
axs.format(grid=False)

# axs[0].text(1050, 0.04, "$\phi=0.1$")
# axs[1].text(1050, 0.04, "$\phi=0.2$")
# axs[2].text(1050, 0.04, "$\phi=0.3$")

axs[0].format(title="$\phi=0.1$", titlesize='large')
axs[1].format(title="$\phi=0.2$", titlesize='large')
axs[2].format(title="$\phi=0.3$", titlesize='large')

fig.savefig("fig_s2.png", dpi=600)
fig.savefig("fig_s2.pdf")
fig.savefig("fig_s2.svg")

uplt.show()
