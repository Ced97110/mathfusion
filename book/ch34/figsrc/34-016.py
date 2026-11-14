import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 3.4; Nx, Ny = 37, 12
P = (Nx - 5*s, Ny); N = (Nx, Ny); R = (Nx + 9*s, Ny); Q = (Nx, Ny + 12*s)
def marks(): line(ax, [(Nx - 2, Ny), (Nx - 2, Ny + 2), (Nx, Ny + 2)], "encre", lw=0.6)
def names(rs=True):
    for pt, t, dx, dy in ((P, "P", -3, 0), (N, "N", 4, -3.5), (Q, "Q", 0, 4)) + (((R, "R", 3.5, 0),) if rs else ()):
        text(ax, pt[0] + dx, pt[1] + dy, "$" + t + "$", "encre", "m")
poly(ax, [P, N, Q], 'sujet'); marks(); names(False)
line(ax, [P, Q], 'sujet', lw=2.6)
text(ax, 24, 36, r'$r$', 'sujet', 'xl')
text(ax, 40, 30, '12', 'fixe', 's'); text(ax, 28, 8, '5', 'fixe', 's')
text(ax, 50, 40, r'$r = QP = 13$', 'sujet', 'm', ha='left')
text(ax, 50, 30, 'en face', 'fixe', 'm', ha='left'); text(ax, 50, 25, "de l'angle droit", 'fixe', 'm', ha='left')
save(fig, '34-016')
