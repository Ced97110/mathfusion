import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 36; ox, oy = 8, 14
A = (ox + 0.6 * u, oy); B = (ox + 0.6 * u, oy + 0.8 * u)
poly(ax, [(ox, oy), A, B], 'fixe')
line(ax, [(ox, oy), A], 'sujet', lw=2.0); line(ax, [A, B], 'resultat', lw=2.0); line(ax, [(ox, oy), B], 'fixe', lw=1.0)
text(ax, (ox + A[0]) / 2, oy - 3.5, '0,6', 'sujet', 'm', weight='bold')
text(ax, A[0] + 3, (oy + B[1]) / 2, '0,8', 'resultat', 'm', weight='bold', ha='left')
text(ax, ox + 6, oy + 18, '1', 'fixe', 'm', ha='right')
text(ax, 8 + 10, 62, 'cos x = 3/5', 'sujet', 'm')
bx = 40; bw = 46
box(ax, bx, 46, bw, 9, 'sujet', label='cos x = 0,6 (donné)', size='s')
arrow(ax, (bx + bw / 2, 46), (bx + bw / 2, 40), 'varie')
text(ax, bx + bw / 2 + 2.5, 43, 'identité', 'varie', 's', ha='left')
text(ax, bx + bw / 2 + 2, 43, '1 − 0,36 = 0,64', 'varie', 's', ha='left') if False else None
box(ax, bx, 31, bw, 9, 'resultat', label=r'$\sin^2 x$ = 1 − 0,36 = 0,64', size='s')
arrow(ax, (bx + bw / 2, 31), (bx + bw / 2, 25), 'varie')
text(ax, bx + bw / 2 + 2.5, 28, r'sin $x$ = $\pm$ 0,8', 'varie', 's', ha='left')
for i, n in enumerate(['tan', 'sec', 'cosec', 'cotan']):
    box(ax, bx + i * 11.8, 14, 10.4, 9, 'resultat', label=n, size='s')
text(ax, bx + bw / 2, 8, 'les définitions donnent les 4 autres', 'fixe', 's')
save(fig, '31-093')
