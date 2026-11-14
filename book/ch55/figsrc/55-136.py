import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
q = 3
n_maps = q ** q            # 3 outputs for each of the 3 inputs
n_polys = q ** q           # 3 values for each of the 3 coefficients
assert n_maps == n_polys == 27
cells = [(i, j, k) for i in range(q) for j in range(q) for k in range(q)]
assert len(cells) == 27
u = 4.6
cubes(ax, cells, (19, 22), u, 'sujet')
cubes(ax, cells, (69, 22), u, 'autre')
text(ax, 19, 66, 'applications', 'sujet', 'm', weight='bold')
text(ax, 19, 61.5, r'$3^3=27$', 'sujet', 'm')
text(ax, 69, 66, 'polynômes', 'autre', 'm', weight='bold')
text(ax, 69, 61.5, r'degré $<3$ : $3^3=27$', 'autre', 's')
# each polynomial gives a different map, 27 against 27: nothing is missed
arrow(ax, (63 - 12, 40), (31 + 3, 40), 'varie')
text(ax, 44, 44, 'tous différents', 'varie', 's')
box(ax, 14, 3, 60, 9, 'resultat', label='27 contre 27 : toutes atteintes', size='s')
save(fig, '55-136')
