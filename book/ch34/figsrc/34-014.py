import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 3.4; Nx, Ny = 37, 12
P = (Nx - 5*s, Ny); N = (Nx, Ny); R = (Nx + 9*s, Ny); Q = (Nx, Ny + 12*s)
def marks(): line(ax, [(Nx - 2, Ny), (Nx - 2, Ny + 2), (Nx, Ny + 2)], "encre", lw=0.6)
def names(rs=True):
    for pt, t, dx, dy in ((P, "P", -3, 0), (N, "N", 4, -3.5), (Q, "Q", 0, 4)) + (((R, "R", 3.5, 0),) if rs else ()):
        text(ax, pt[0] + dx, pt[1] + dy, "$" + t + "$", "encre", "m")
poly(ax, [P, N, Q], 'sujet'); poly(ax, [R, N, Q], 'fixe'); marks(); names()
line(ax, [N, Q], 'encre', lw=1.0)
text(ax, 25, 36, '13', 'sujet', 's'); text(ax, 28, 8.5, '5', 'sujet', 's')
text(ax, 51, 36, '15', 'fixe', 's'); text(ax, 52, 8.5, '9', 'fixe', 's')
box(ax, 2, 50, 30, 8, 'sujet', label='triangle PNQ')
arrow(ax, (20, 50), (27, 33), 'sujet', lw=0.8)
save(fig, '34-014')
