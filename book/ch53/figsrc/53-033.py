import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# clair : ALGEBRE ; trois clés de la famille (numéros vérifiés : 0,11,6,4,1,17,4 + b mod 26)
text(ax, 44, 69, 'clair : ALGEBRE', 'fixe', 'm', weight='bold')
rows = [(50, 0, 'ALGEBRE', 'fixe'), (34, 3, 'DOJHEUH', 'sujet'), (18, 5, 'FQLJGWJ', 'sujet')]
for y, b, w, role in rows:
    box(ax, 2, y, 22, 10, 'varie', label=f'b = {b}', weight='bold')
    arrow(ax, (25, y + 5), (36, y + 5), 'varie')
    box(ax, 38, y, 36, 10, role, label=w, size='l')
text(ax, 80, 55, '= clair', 'fixe', 's')
text(ax, 44, 9.5, '… jusqu’à b = 25', 'varie', 's')
text(ax, 44, 3.5, '26 chiffres : b de 0 à 25', 'sujet', 's', weight='bold')
save(fig, '53-033')
