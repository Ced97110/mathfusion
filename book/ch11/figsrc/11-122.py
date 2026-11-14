import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ox, oy, u = 20, 10, 4.5
cubes(ax, [(i, j, k) for i in range(4) for j in range(4) for k in range(4)], (ox, oy), u, 'sujet')
text(ax, ox+2*0.866*u+4.5, oy+u-3, '4 mm', 'varie', 's')
text(ax, ox-2*0.866*u-4.5, oy+u-3, '4 mm', 'varie', 's')
text(ax, ox+4*0.866*u+5.5, oy+u*2.5+2, '4 mm', 'varie', 's')
text(ax, 64, 38, '4 mm × 4 mm × 4 mm', 'encre', 's')
text(ax, 64, 31, '= 64 mm³', 'resultat', weight='bold')
text(ax, 64, 20, 'mm × mm × mm', 'encre', 's')
text(ax, 64, 13, '= mm³', 'resultat', weight='bold')
save(fig, '11-122')
