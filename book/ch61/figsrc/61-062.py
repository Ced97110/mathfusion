import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for i, (lab) in enumerate(['unitaire', 'plus petit degré', r'nul en $u$']):
    y = 46 - i * 15
    box(ax, 4, y - 5, 36, 10, 'sujet', label=lab, size='m'); arrow(ax, (40.5, y), (50, 31), 'varie')
box(ax, 51, 24, 32, 14, 'resultat', label=r'$m(x)$', size='xl')
text(ax, 67, 44, 'une lettre', 'resultat', 's')
text(ax, 67, 18, r'$m(u)=0$', 'resultat', 'm')
save(fig, '61-062')
