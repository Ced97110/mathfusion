import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 4, 52, 'avant', 'fixe', 's', ha='left')
text(ax, 4, 28, 'après', 'fixe', 's', ha='left')
for k in range(4):
    x = 26 + 16 * k
    text(ax, x, 60, str(k + 1), 'fixe', 'm')
    disc(ax, x, 52, 3.2, 'sujet')
    disc(ax, x, 28, 3.2, 'sujet')
    arrow(ax, (x, 48.5), (x, 31.7), 'fixe')
text(ax, 44, 20, 'e : chacun reste à sa place', 'fixe', 's')
box(ax, 26, 3, 36, 10, 'resultat', label=r'$\{e\}$ : 1 seul élément', size='s')
save(fig, '64-019')
