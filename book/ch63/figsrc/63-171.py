import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 20, 74, 'sous-groupes', 'sujet', 'm', weight='bold')
text(ax, 68, 74, 'corps', 'autre', 'm', weight='bold')
ys = [58, 34, 10]
left = [r'$G$', r'$\{1, \sigma_4\}$', r'$\{1\}$']
right = [r'$\mathbb{Q}$', r'$\mathbb{Q}(\sqrt{5})$', r'$\mathbb{Q}(\omega)$']
for l, r, y in zip(left, right, ys):
    box(ax, 4, y, 32, 12, 'sujet', label=l)
    box(ax, 52, y, 32, 12, 'autre', label=r)
    arrow(ax, (37, y + 6), (51, y + 6), 'fixe', both=True, lw=0.7)
for y in (46, 22):
    line(ax, [(20, y), (20, y + 12)], 'sujet', lw=1.2)
    line(ax, [(68, y), (68, y + 12)], 'autre', lw=1.2)
    text(ax, 22.5, y + 6, '2', 'varie', 'l', ha='left', weight='bold')
    text(ax, 65.5, y + 6, '2', 'varie', 'l', ha='right', weight='bold')
text(ax, 44, 4, 'mêmes nombres des deux côtés', 'resultat', 's')
save(fig, '63-171')
