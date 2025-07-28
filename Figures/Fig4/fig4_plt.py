import os
import numpy as np
import ultraplot as uplt

uplt.rc.update({'cycle': 'FlatUI'})


volume_frac = [0.0, 0.1, 0.2, 0.3, 0.4]
dv = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
dv.reverse()
pb_closed = [0.003, 0.007, 0.02, 0.05, 0.15, 0.31, 0.54, 0.73]
xticks = [str(elem) for elem in pb_closed]

rate = []

for i, elem in enumerate(volume_frac):
    infile = f"./V_{elem:.1f}/turnover_rate.dat"
    # infile = os.path.join(path, f"V_{elem:.1f}", "x1.dat")
    print(infile)
    data = np.loadtxt(infile, usecols=(2,))
    rate.append(data)

rate = np.array(rate)
fig, ax = uplt.subplots(ncols=1, nrows=1, refwidth="8cm", refaspect=1.6)

xedges = uplt.edges(dv)
yedges = uplt.edges(volume_frac)
# ax.pcolormesh(xedges, yedges, rate, )
# im = ax.pcolor(dv, volume_frac, rate, inbounds=1, cmap='plasma_r', vmin=0, vmax=0.4, lw=2.0, ec='white')
im = ax.pcolor(dv, volume_frac, rate, inbounds=1, cmap='GnBu', vmin=0, vmax=0.4, lw=2.0, ec='white')
ax.colorbar(im, loc='r', length=1, label='Turnover rate (ms$^{-1}$)', tickminor=False, ticks=0.1)

ax.format(xlabel='$\mathrm{P_{closed}}$', ylabel='Crowder volume fraction ($\mathrm{\phi}$)')
ax.format(xticks=dv, yticks=volume_frac)
ax.format(xminorticks='none', yminorticks='none')
ax.format(xticklabels=xticks)
ax.format(grid=False)

fig.savefig("fig4.png", dpi=600)
fig.savefig("fig4.svg")
fig.savefig("fig4.pdf")
uplt.show()
