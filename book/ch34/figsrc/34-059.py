import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 3.0; o = (4, 8); X = 5 * s; Y = 9 * s; hh = 12 * s
N = (o[0] + X, o[1] + hh); Pp = o; Rr = (o[0] + X + Y, o[1]); F = (o[0] + X, o[1])
poly(ax, [Pp, N, F], 'fixe'); poly(ax, [F, N, Rr], 'fixe')
line(ax, [F, N], 'sujet', lw=1.6)
line(ax, [Pp, F], 'varie', lw=1.6); line(ax, [F, Rr], 'varie', lw=1.6)
text(ax, F[0] - 3, 8 + hh / 2, 'h', 'sujet', 's'); text(ax, o[0] + X / 2, 3.5, 'x', 'varie', 's'); text(ax, F[0] + Y / 2, 3.5, 'y', 'varie', 's')
text(ax, o[0] + X / 2 - 2, 8 + hh / 2 + 7, 'r', 'fixe', 's'); text(ax, F[0] + Y / 2 + 3, 8 + hh / 2 + 6, 'p', 'fixe', 's')
text(ax, N[0] - 3.5, N[1] - 5, 'A', 'encre', 's'); text(ax, N[0] + 3.5, N[1] - 5, 'B', 'encre', 's')
text(ax, 50, 54, 'cos A cos B', 'sujet', 's', ha='left'); box(ax, 71, 50, 16, 8, 'sujet', label='h × h', size='s')
text(ax, 50, 38, 'sin A sin B', 'varie', 's', ha='left'); box(ax, 71, 34, 16, 8, 'varie', label='x × y', size='s')
text(ax, 54, 22, '−', 'resultat', 'xl', ha='left'); box(ax, 66, 18, 21, 8, 'resultat', label='QP − QH', size='s')
for y in (54, 38, 22): arrow(ax, (66 if y == 22 else 67, y), (65.5 if y == 22 else 70.5, y), 'fixe') if False else None
save(fig, '34-059')
