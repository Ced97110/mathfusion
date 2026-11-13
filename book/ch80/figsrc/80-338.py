import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
text(ax, 30, 77, 'filtre : on garde tout ce qui monte', 'sujet', 's')
box(ax, 6, 58, 40, 9, 'sujet', label='ℕ')
box(ax, 6, 38, 40, 9, 'sujet', label='ℕ sans 2')
box(ax, 6, 18, 40, 9, 'sujet', label='ℕ sans 2 et 5')
for y0, y1 in ((27.6, 37.4), (47.6, 57.4)):
    arrow(ax, (26, y0), (26, y1), 'varie')
    text(ax, 31, (y0 + y1) / 2, 'plus grand', 'varie', 's', ha='left')
box(ax, 58, 36, 22, 9, 'limite', label=r'$\{7\}$', dash=True)
arrow(ax, (58, 41), (46.6, 42.5), 'limite', curve=0.0)
text(ax, 69, 30, 'complément infini', 'limite', 's')
text(ax, 69, 25.5, 'donc pas dans la', 'limite', 's')
text(ax, 69, 21.5, 'collection', 'limite', 's')
save(fig, '80-338')
