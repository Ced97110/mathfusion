import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
box(ax, 6, 92, 76, 9, 'sujet', label='si 2 = r × s (r, s ≠ ±1)')
arrow(ax, (44, 91), (44, 84), 'varie')
box(ax, 6, 73, 76, 10, 'varie', label='N(r) × N(s) = N(2) = 4', lw=1.6)
for x, lab in [(2, 'N(r) = 1'), (31, 'N(r) = 2'), (60, 'N(r) = 4')]:
    box(ax, x, 52, 26, 9, 'fixe', label=lab, size='s')
    arrow(ax, (44, 72), (x + 13, 62), 'varie')
reasons = ['r = ±1\nexclu', 'aucun point\nde norme 2', 'N(s) = 1,\ns = ±1 exclu']
for x, r in zip((2, 31, 60), reasons):
    text(ax, x + 13, 44, r, 'limite', 's')
    arrow(ax, (x + 13, 38), (x + 13, 23), 'fixe')
box(ax, 6, 12, 76, 10, 'resultat', label='2 ne se casse pas')
save(fig, '56-018')
