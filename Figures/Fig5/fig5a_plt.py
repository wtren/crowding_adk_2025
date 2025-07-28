import os
import numpy as np
import ultraplot as uplt

pmf2d = []

R_lig_core = [[], []]
R_nmp_core = [[], []]

path1 = "/media/wtren/One Touch/ADK_crowding/jjlu_data/fig5/dilute_P0.3"
path2 = "/media/wtren/One Touch/ADK_crowding/jjlu_data/fig5/V0.3_P0.3"

for i in range(12):
    fn = f"./dilute/ake_-1.0_{i+1:d}.dist"
    data = np.loadtxt(fn, skiprows=1)
    R_lig_core[0].extend(list(data[:, 1]))
    R_nmp_core[0].extend(list(data[:, 0]))

for j in range(12):
    fn = f"./v_0.3/ake_-1.0_{j+1:d}.dist"
    data = np.loadtxt(fn, skiprows=1)
    R_lig_core[1].extend(list(data[:, 1]))
    R_nmp_core[1].extend(list(data[:, 0]))

# labs = ["V$_{frac}=0.0$", "V$_{frac}=0.3$"]
labs = ["$\phi=0.0$", "$\phi=0.3$"]
cm = "GnBu_r"
bn = 25
interval = np.arange(0, 10, 1.0)


fig, axs = uplt.subplots(ncols=2, nrows=1, sharex=4, sharey=4, refaspect=1, refheight="4cm", wspace=0.8)

for k in range(2):
    hist, xedges, yedges = np.histogram2d(R_lig_core[k], R_nmp_core[k], bins=[bn, bn])
    hist = hist.astype('float')
    hist = hist / np.max(hist)

    x0 = 0.5 * (xedges[1:] + xedges[:-1])
    y0 = 0.5 * (yedges[1:] + yedges[:-1])
    X, Y = np.meshgrid(x0, y0)
    Z = -np.log(hist.T)

    im = axs[k].contourf(X, Y, Z, cmap=cm, lw=0.2, ec='k', levels=interval)
    axs[k].text(20, 23.9, labs[k], size=10)

axs.format(xlabel='$R_{LID-CORE}\ (\AA)$')
axs.format(ylabel='$R_{NMP-CORE}\ (\AA)$')
axs.format(xlim=[19, 36], ylim=[17., 24.8])
axs.format(grid=False)

fig.savefig("fig5A.png", dpi=600)
fig.savefig("fig5A.svg")
fig.savefig("fig5A.pdf")
uplt.show()
