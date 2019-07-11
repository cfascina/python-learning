import numpy as np
from scipy import integrate
from matplotlib import pyplot as mplot
from mpl_toolkits.mplot3d import Axes3D

def solve_lorenz(num, angle = 0.0, max_time = 4.0, sigma = 10.0, beta = 8. / 3, rho = 28.0):
    fig = mplot.figure();

    ax = fig.add_axes([0, 0, 1, 1], projection = '3d');
    ax.set_xlim((-25, 25))
    ax.set_ylim((-35, 35))
    ax.set_zlim((5, 55))
    ax.axis('off')

    def lorenz_deriv(x_y_z, t0, sigma = sigma, beta = beta, rho = rho):
        x, y, z = x_y_z
        return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

    np.random.seed(1)
    x0 = -15 + 30 * np.random.random((num, 3))

    t = np.linspace(0, max_time, int(250 * max_time))
    x_t = np.asarray([integrate.odeint(lorenz_deriv, x0i, t) for x0i in x0])

    colors = mplot.cm.jet(np.linspace(0, 1, num));

    for i in range(num):
        x, y, z = x_t[i, :, :].T
        lines = ax.plot(x, y, z, '-', c = colors[i])
        _ = mplot.setp(lines, linewidth = 1);

    ax.view_init(30, angle)
    _ = mplot.show();

    return t, x_t

t, x_t = solve_lorenz(num = 10)
