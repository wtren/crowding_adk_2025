import numpy as np
import ultraplot as uplt
import glob


dv = ["-3.0", "-2.0", "-1.0", "0.0", "1.0", "2.0", "3.0", "4.0"]

dirs = ["./nolig-mut-115-0/", \
        "./nolig-mutr-115-47/", \
        "./nolig-mutr-115-93/", \
        "./nolig-mutr-115/", \
        "./nolig-mutr-115-186/"
        ]
vol_frac = [0.0, 0.1, 0.2, 0.3, 0.4]
pb_closed = np.zeros([len(dv), len(vol_frac)], dtype='f')

for i, fpath in enumerate(dirs):
    for j, dv_j in enumerate(dv):
        files = glob.glob(fpath+f"data-{dv_j:s}-*") 
        N_tot = 0
        N_closed = 0
        for fname in files:
            data = np.loadtxt(fname, usecols=(1, 2), skiprows=2)
            sel = np.where((data[:, 0] > 0.5) & (data[:, 1] > 0.5))
            N_tot = N_tot + data.shape[0]
            N_closed = N_closed + sel[0].shape[0]

        pb = N_closed / N_tot
        pb_closed[j][i] = pb

fig, ax = uplt.subplots(ncols=1, nrows=1, refaspect=1.1, refheight="4cm")

name = 'imola'
idxs = uplt.arange(0, 1, 0.12)
for i in range(len(dv)):
    ax.plot(vol_frac, pb_closed[i], marker='o', lw=0.9, s=4, color=(name, idxs[i]))

ax.plot(vol_frac, pb_closed[2], marker='o', lw=0.9, s=4, color='r')

ax.format(xlim=[-0.02, 0.42], ylim=[-0.05, 1.0])
ax.format(xticks=0.1, xminorticks=[], yticks=0.2)
ax.format(xlabel="$\phi$", fontsize=10)
ax.format(ylabel="$P_{closed}$")
ax.format(grid=False)

fig.savefig("fig5B.png", dpi=600)
fig.savefig("fig5B.svg")
fig.savefig("fig5B.pdf")
uplt.show()
