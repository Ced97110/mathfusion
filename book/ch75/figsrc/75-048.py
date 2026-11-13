import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 3, 18, 30, 16, 'sujet', label=r'$F$', size='xl', weight='bold')
text(ax, 18, 40, 'écrit une seule fois', 'sujet', 's')
for k, (lab, nm) in enumerate([(r'$\mathbb{R}$', 'réels'), (r'$\mathbb{C}$', 'complexes'), (r'$\mathbb{F}_q$', 'q éléments')]):
    y = 38 - k*16
    box(ax, 52, y - 5, 18, 10, 'autre', label=lab, size='l')
    text(ax, 79, y, nm, 'fixe', 's', ha='center')
    arrow(ax, (33, 26), (51.5, y), 'varie', lw=1.0)
save(fig, '75-048')
