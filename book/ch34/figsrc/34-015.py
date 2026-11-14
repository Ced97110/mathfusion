import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 3.4; Nx, Ny = 37, 12
P = (Nx - 5*s, Ny); N = (Nx, Ny); R = (Nx + 9*s, Ny); Q = (Nx, Ny + 12*s)
def marks(): line(ax, [(Nx - 2, Ny), (Nx - 2, Ny + 2), (Nx, Ny + 2)], "encre", lw=0.6)
def names(rs=True):
    for pt, t, dx, dy in ((P, "P", -3, 0), (N, "N", 4, -3.5), (Q, "Q", 0, 4)) + (((R, "R", 3.5, 0),) if rs else ()):
        text(ax, pt[0] + dx, pt[1] + dy, "$" + t + "$", "encre", "m")
poly(ax, [P, N, Q], 'sujet'); marks(); names(False)
a0 = math.degrees(math.atan2(-12, -5)) % 360
arc = [(Q[0] + 12*math.cos(math.radians(a0 + (270 - a0)*i/20)), Q[1] + 12*math.sin(math.radians(a0 + (270 - a0)*i/20))) for i in range(21)]
line(ax, arc, 'varie', lw=1.4)
text(ax, 34.5, Q[1] - 17, r'$A$', 'varie', 'l')
text(ax, 23, 28.5, '13', 'sujet', 's'); text(ax, 28, 8, '5', 'sujet', 's'); text(ax, 40, 30, '12', 'fixe', 's')
text(ax, 50, 40, r'$A$ : angle en $Q$', 'varie', 'm', ha='left')
text(ax, 50, 28, r'$\sin A=\frac{5}{13}$', 'resultat', 'l', ha='left')
save(fig, '34-015')
