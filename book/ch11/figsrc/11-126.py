import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 3.2; step = 4.4*u; ox = 20
for k in range(3):
    oy = 14 + k*step
    cubes(ax, [(i, j, 0) for i in range(4) for j in range(2)], (ox, oy), u, 'sujet')
    text(ax, 42, oy+6, f'couche {k+1} : 4 × 2 = 8', 'sujet', 's', ha='left')
text(ax, ox+2*0.866*u+4, 14+u-2.5, '4', 'encre', 's')
text(ax, ox-1*0.866*u-3.5, 14+u-1.5, '2', 'encre', 's')
text(ax, 42, 6, '3 × 8 = 24 cubes', 'resultat', ha='left', weight='bold')
save(fig, '11-126')
