import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
f = numberline(ax, 4, 70, 24, 0, 30, step=1, labels=False, arrow_right=True)
for t in (1, 5, 13, 17, 25, 29):
    disc(ax, f(t), 24, 2.4, 'sujet' if t in (1, 5) else 'resultat', label=str(t), size='s')
for a, b, c in [(1, 13, -0.5), (13, 25, -0.5), (5, 17, 0.5), (17, 29, 0.5)]:
    up = c < 0
    arrow(ax, (f(a), 24 + (2.6 if up else -2.6)), (f(b), 24 + (2.6 if up else -2.6)), 'varie', curve=c)
    text(ax, (f(a) + f(b)) / 2, 24 + (10.5 if up else -10.5), '+ 12', 'varie', 's')
arrow(ax, (f(29) + 3.2, 24), (86, 24), 'resultat', lw=1.2)
text(ax, 79.5, 31, 'la liste ne\ns’arrête jamais', 'resultat', 's')
save(fig, '32-013')
