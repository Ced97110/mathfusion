import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 3, 3, 82, 62, 'fixe', dash=True, fill=False)
text(ax, 44, 60, 'matrices commutant avec A', 'fixe', 's')
box(ax, 8, 32, 14, 10, 'sujet', label=r'$X$')
box(ax, 8, 14, 14, 10, 'sujet', label=r'$Y$')
line(ax, [(22.5, 37), (30, 31)], 'fixe'); line(ax, [(22.5, 19), (30, 31)], 'fixe')
for y, s in ((46, r'$X+Y$'), (31, r'$X\times Y$'), (16, r'$cX$')):
    box(ax, 50, y - 5, 30, 10, 'resultat', label=s)
    arrow(ax, (30, 31), (49.5, y), 'varie')
text(ax, 44, 8, 'les résultats restent dedans', 'resultat', 's')
save(fig, '60-268')
