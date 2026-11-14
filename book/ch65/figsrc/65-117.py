import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 77, r'$y^3-2$ : $p=0$, $q=-2$', 'sujet', 's')
labs = (r'$d=-108$', r'$-3d=324$', r'$\sqrt{324}=18$')
for i, l in enumerate(labs):
    box(ax, 3 + i * 30, 56, 23, 12, 'varie' if i == 2 else 'fixe', label=l, size='s')
for i in range(2):
    arrow(ax, (26 + i * 30, 62), (33 + i * 30, 62), 'varie')
box(ax, 3, 32, 38, 12, 'fixe', label=r'$-\frac{27q}{2}=27$', size='m')
box(ax, 47, 32, 38, 12, 'varie', label=r'$\frac{3}{2}\cdot18=27$', size='m')
arrow(ax, (74.5, 56), (68, 44.5), 'varie')
box(ax, 14, 6, 60, 14, 'resultat', label=r'$27+27=54=z_1^3$', size='m')
arrow(ax, (22, 32), (30, 20.5), 'resultat')
arrow(ax, (66, 32), (58, 20.5), 'resultat')
save(fig, '65-117')
