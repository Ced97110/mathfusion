import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, 'cadran à 6 heures', 'fixe', 'm')
cols = [52 + 8 * j for j in range(3)]
rows = [42, 34]
for y in rows:
    for x in cols:
        disc(ax, x, y, 2.6, 'sujet')
line(ax, [(44, 30.5), (43, 30.5), (43, 45.5), (44, 45.5)], 'sujet')
line(ax, [(47.5, 49.5), (47.5, 50.5), (72.5, 50.5), (72.5, 49.5)], 'autre')
text(ax, 27, 38, r'$2\cdot1\neq0$', 'sujet', 'm')
text(ax, 60, 54, r'$3\cdot1\neq0$', 'autre', 'm')
text(ax, 81, 38, '6 uns', 'resultat', 's')
box(ax, 4, 14, 80, 10, 'resultat', label=r'$(2\cdot1)(3\cdot1)=6\cdot1=0$')
box(ax, 4, 2, 80, 8, 'limite', label='2 et 3 : diviseurs de zéro')
save(fig, '51-137')
