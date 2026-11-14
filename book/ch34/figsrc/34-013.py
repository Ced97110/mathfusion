import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 3.4; Nx, Ny = 37, 12
P = (Nx - 5*s, Ny); N = (Nx, Ny); R = (Nx + 9*s, Ny); Q = (Nx, Ny + 12*s)
def marks(): line(ax, [(Nx - 2, Ny), (Nx - 2, Ny + 2), (Nx, Ny + 2)], "encre", lw=0.6)
def names(rs=True):
    for pt, t, dx, dy in ((P, "P", -3, 0), (N, "N", 4, -3.5), (Q, "Q", 0, 4)) + (((R, "R", 3.5, 0),) if rs else ()):
        text(ax, pt[0] + dx, pt[1] + dy, "$" + t + "$", "encre", "m")
poly(ax, [P, N, Q], 'fixe'); poly(ax, [R, N, Q], 'fixe'); marks(); names()
line(ax, [N, Q], 'sujet', lw=2.4)
text(ax, 33.2, 32, r'$h$', 'sujet', 'xl'); text(ax, 40.8, 32, r'$h$', 'sujet', 'xl')
text(ax, 44, 59, r'$h = QN = 12$', 'sujet', 'm', ha='left')
save(fig, '34-013')
