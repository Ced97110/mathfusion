import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
pas = ('irréductible (Eisenstein)', '3 racines réelles', 'transposition + 5-cycle', r'ils engendrent $S_5$')
ys = (66, 48, 30, 12)
for y, t in zip(ys, pas):
    box(ax, 3, y, 40, 12, 'sujet', label=t, size='s')
for a, b in zip(ys[:-1], ys[1:]):
    arrow(ax, (23, a - 0.5), (23, b + 12.5), 'varie')
box(ax, 52, 12, 34, 12, 'resultat', label=r'$G=S_5$ : 120', size='s')
box(ax, 52, 38, 34, 12, 'resultat', label='non résoluble', size='s')
box(ax, 52, 64, 34, 14, 'resultat', label='pas de radicaux', size='s')
arrow(ax, (44, 18), (51, 18), 'varie')
arrow(ax, (69, 25), (69, 37), 'varie'); arrow(ax, (69, 51), (69, 63), 'varie')
save(fig, '64-183')
