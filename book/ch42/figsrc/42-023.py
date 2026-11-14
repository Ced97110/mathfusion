import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for y, (t1, t2) in zip([54, 40], [('gourde', 'carte'), ('carte', 'gourde')]):
    box(ax, 3, y - 5, 15, 10, 'sujet', label=t1, size='s')
    arrow(ax, (18.5, y), (24.5, y), 'varie')
    box(ax, 25, y - 5, 15, 10, 'sujet', label=t2, size='s')
arrow(ax, (41, 54), (54, 50), 'resultat'); arrow(ax, (41, 40), (54, 44), 'resultat')
box(ax, 55, 36, 30, 24, 'resultat')
text(ax, 70, 54, 'même sac', 'resultat', 'm')
text(ax, 70, 44, r'$\{a,b\}$', 'resultat', 'l')
box(ax, 2, 6, 40, 12, 'limite', fill=False, dash=True, label='ordre compté : 16 sacs', size='s')
box(ax, 46, 6, 40, 12, 'resultat', label='ordre ignoré : 8 sacs', size='s')
save(fig, '42-023')
