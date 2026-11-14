import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 3.4; Nx, Ny = 37, 14
P = (Nx - 5*s, Ny); N = (Nx, Ny); R = (Nx + 9*s, Ny); Q = (Nx, Ny + 12*s)
poly(ax, [P, N, Q], 'sujet'); poly(ax, [R, N, Q], 'varie')
line(ax, [N, Q], 'encre', lw=1.2)
line(ax, [(Nx - 2, Ny), (Nx - 2, Ny + 2), (Nx, Ny + 2)], 'encre', lw=0.6)
for pt, t, dx, dy in ((P, 'P', -3, 0), (N, 'N', 0, 4.5), (Q, 'Q', 0, 4), (R, 'R', 3.5, 0)):
    text(ax, pt[0] + dx, pt[1] + dy, '$' + t + '$', 'encre', 'm')
text(ax, 34.5, 32, '12', 'sujet', 's'); text(ax, 39.8, 32, '12', 'varie', 's')
text(ax, 28.5, 38, '13', 'sujet', 's'); text(ax, 51, 36, '15', 'varie', 's')
text(ax, 28, 10.5, '5', 'sujet', 's'); text(ax, 52, 10.5, '9', 'varie', 's')
brace(ax, P[0], R[0], 7.5, 'fixe', label='14')
text(ax, 34.5, 46, '$A$', 'sujet', 's'); text(ax, 41.2, 46, '$B$', 'varie', 's')
save(fig, '34-012')
