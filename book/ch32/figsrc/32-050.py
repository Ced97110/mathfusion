import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
f = numberline(ax, 8, 76, 24, -360, 720, step=180, every=2)
pts = [(23.58, 'up', '23,58°'), (156.42, 'down', '156,42°'), (383.58, 'up', '383,58°'), (516.42, 'down', '516,42°')]
for v, d, s in pts:
    disc(ax, f(v), 24, 1.2, 'resultat')
    text(ax, f(v), 24 + (5 if d == 'up' else -9.5), s, 'resultat', 's')
disc(ax, f(-336.42), 24, 1.2, 'fixe', fill=False)
text(ax, f(-336.42) + 1, 29, '−336,42°', 'fixe', 's')
text(ax, 79, 29, '…', 'fixe', 'l')
text(ax, 44, 44, 'la liste ne s’arrête pas', 'encre', 'm')
text(ax, 44, 5, 'angles arrondis à 0,01°', 'fixe', 'm')
save(fig, '32-050')
