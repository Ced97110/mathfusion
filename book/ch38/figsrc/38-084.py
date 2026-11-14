import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(92)
# deux angles au sommet dessinés exactement : 3,25° (base 1000 m) et 10,16° (base 5000 m)
L = 58.0
rows = [(62, 3.25, 'sujet', 'base 1000 m', r'angle $3{,}25°$', 'erreur 2,5 %'),
        (20, 10.16, 'resultat', 'base 5000 m', r'angle $10{,}16°$', 'erreur 0,5 %')]
for y, ang, role, l1, l2, l3 in rows:
    o = (5, y)
    a = math.radians(ang)
    line(ax, [o, (o[0] + L, o[1])], role, lw=1.2)
    line(ax, [o, (o[0] + L * math.cos(a), o[1] + L * math.sin(a))], role, lw=1.2)
    text(ax, 5, y - 6, l1, role, 's', ha='left')
    text(ax, 5, y + 12, l2, 'varie', 's', ha='left')
    text(ax, 66, y + 3, l3, role, 's', ha='left')
arrow(ax, (44, 50), (44, 34), 'varie')
text(ax, 62, 42, 'on recule A', 'varie', 's')
text(ax, 44, 86, 'agrandir l’angle au sommet', 'encre', 'm')
save(fig, '38-084')
