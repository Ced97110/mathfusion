import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 24, 64, r'$\{1,\sigma\}$', 'sujet', 'l')
text(ax, 71, 64, 'symétries du segment', 'autre', 's')
labels = ['1 : ne change rien', r'$\sigma:\sqrt{2}\mapsto-\sqrt{2}$', r'$\sigma\circ\sigma=1$']
ends = [('A', 'B'), ('B', 'A'), ('A', 'B')]
for i in range(3):
    c = 50 - 18 * i
    box(ax, 2, c - 7, 44, 14, 'sujet', label=labels[i])
    arrow(ax, (47, c), (57, c), 'resultat', both=True)
    line(ax, [(67.2, c), (76.8, c)], 'autre', lw=1.2)
    disc(ax, 64, c, 3, 'autre', label=ends[i][0], size='s')
    disc(ax, 80, c, 3, 'autre', label=ends[i][1], size='s')
save(fig, '63-016')
