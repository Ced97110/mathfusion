import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 20, 82, 'rectangle', 'sujet', 'm', weight='bold')
text(ax, 68, 82, r'$\mathbb{Z}/2\times\mathbb{Z}/2$', 'autre', 'm', weight='bold')
pairs = [('e', '(0, 0)'), ('h', '(1, 0)'), ('v', '(0, 1)'), ('d', '(1, 1)')]
for i, (a, b) in enumerate(pairs):
    y = 68 - i * 12
    box(ax, 8, y - 4, 24, 9, 'sujet', label=a, size='m')
    box(ax, 56, y - 4, 24, 9, 'autre', label=b, size='m')
    arrow(ax, (33, y + 0.5), (55, y + 0.5), 'varie', both=True)
box(ax, 4, 6, 38, 12, 'resultat', label=r'$h$ puis $v$ : $d$', size='m')
box(ax, 46, 6, 38, 12, 'resultat', label=r'$(1,0)+(0,1)=(1,1)$', size='s')
save(fig, '45-230')
