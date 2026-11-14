import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

e, h = ord('E') - 65, ord('H') - 65
assert (e, h, h - e) == (4, 7, 3)

fig, ax = canvas(80)
box(ax, 4, 62, 60, 10, 'sujet', label='1. H est la plus fréquente', size='s')
box(ax, 4, 46, 60, 10, 'varie', label='2. on suppose : E est devenu H', size='s')
box(ax, 4, 30, 60, 10, 'varie', label=r'3. $4 + b = 7$, donc $b = 3$', size='s')
box(ax, 4, 14, 60, 10, 'sujet', label=r'4. déchiffrer avec $b = 3$', size='s')
for y in (62, 46, 30):
    arrow(ax, (34, y), (34, y - 6 + 0.0), 'fixe', lw=0.8)
box(ax, 4, 0.5, 28, 9.5, 'resultat', label='lisible : stop', size='s')
box(ax, 36, 0.5, 30, 9.5, 'limite', label='illisible :\nlettre suivante', size='s')
arrow(ax, (20, 14), (20, 10.5), 'resultat', lw=0.8)
arrow(ax, (51, 14), (51, 10.5), 'limite', lw=0.8)
arrow(ax, (66.5, 5), (66.5, 51), 'limite', lw=0.8, curve=-0.0)
line(ax, [(66.5, 5), (66.5, 51)], 'limite', lw=0.8)
arrow(ax, (66.5, 51), (65, 51), 'limite', lw=0.8)
save(fig, '53-065')
