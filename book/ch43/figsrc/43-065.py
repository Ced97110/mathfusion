import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
vals = [-21, -9, 3, 15, 27]
f = lambda v: 44 + v * 1.25
y = 22
arrow(ax, (f(-21) - 5, y), (4, y), 'fixe', lw=0.9)
arrow(ax, (f(27) + 5, y), (84, y), 'fixe', lw=0.9)
line(ax, [(f(-21) - 5, y), (f(27) + 5, y)], 'fixe', lw=0.9)
text(ax, 8, y + 4, '…', 'fixe', 'l'); text(ax, 80, y + 4, '…', 'fixe', 'l')
for v in vals:
    disc(ax, f(v), y, 2.2, 'sujet')
    text(ax, f(v), y - 6, str(v).replace('-', '−'), 'sujet', 'm')
for a, b in zip(vals, vals[1:]):
    arrow(ax, (f(a) + 1, y + 2.5), (f(b) - 1, y + 2.5), 'varie', lw=0.9, curve=-0.7)
    text(ax, (f(a) + f(b)) / 2, y + 10.5, '+12', 'varie', 's')
text(ax, 44, 46, r'classe $\bar{3}$ : tous les entiers de la liste', 'sujet', 'm')
box(ax, 22, 2, 44, 8, 'resultat', label=r'$\bar{15}=\bar{3}$ : même paquet', size='m')
save(fig, '43-065')
