import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 3, 14, 38, 42, 'sujet')
text(ax, 22, 49, r'$G$', 'sujet', 'xl', weight='bold')
for x, l in zip([14, 30], ['1', r'$\sigma$']):
    disc(ax, x, 35, 5, 'sujet', label=l)
text(ax, 22, 21, r'$E=\mathbb{Q}(\sqrt{2})$', 'sujet', 's')
box(ax, 46, 14, 39, 42, 'autre')
text(ax, 65.5, 49, r'$G$', 'autre', 'xl', weight='bold')
for x, l in zip([53, 61.5, 70, 78.5], ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$']):
    disc(ax, x, 35, 3.9, 'autre', label=l, size='s')
text(ax, 65.5, 21, r'$E=\mathbb{Q}(\sqrt{2},\sqrt{3})$', 'autre', 's')
text(ax, 44, 6, r'même nom $G$, deux groupes', 'fixe', 's')
save(fig, '63-040')
