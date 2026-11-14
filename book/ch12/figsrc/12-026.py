import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 18, 56, '12 euros', 'sujet', 'm')
line(ax, [(8, 49), (28, 49)], 'encre', lw=1.4)
text(ax, 18, 42, '3 amis', 'autre', 'm')
text(ax, 18, 30, 'trait : partager', 'varie', 's')
arrow(ax, (34, 49), (46, 49), 'varie')
for i in range(3):
    box(ax, 50 + i * 12, 44, 10, 10, 'resultat', label='4')
text(ax, 68, 38, 'parts égales', 'resultat', 's')
text(ax, 44, 24, r'$x/y$ : $x$ partagé en $y$ parts', 'encre', 's')
save(fig, '12-026')
