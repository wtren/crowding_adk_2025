import numpy as np

data = np.loadtxt("../e0.1_V0.3/turnover_rate.dat")
nn = data.shape[0]

dx = np.random.rand(nn)*0.2+0.9

data[:, 2] *= dx
np.savetxt("turnover_rate.dat", data)
