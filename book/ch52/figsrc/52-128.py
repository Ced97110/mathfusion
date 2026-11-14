import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
specs = [('sujet', r'$(3)$ idéal maximal'), ('fixe', r'$\mathbb{Z}/3\mathbb{Z}$ est un corps'),
         ('varie', 'un corps est intègre'), ('resultat', r'$(3)$ idéal premier')]
for k, (role, lab) in enumerate(specs):
    y = 62 - 17 * k
    box(ax, 4, y, 42, 11, role, label=lab, size='s')
    if k < 3: arrow(ax, (25, y), (25, y - 6), 'fixe')
text(ax, 66, 50.5, r'$\bar2\times\bar2=\bar1$', 'fixe', 's')
text(ax, 66, 33.5, 'on multiplie par l\'inverse', 'varie', 's')
save(fig, '52-128')
