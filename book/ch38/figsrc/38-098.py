import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
# trois triangles aux angles 60°, 60°, 60° : même forme, tailles différentes
x = 4.0
for side, role in ((12.0, 'sujet'), (22.0, 'sujet'), (32.0, 'sujet')):
    h = side * math.sqrt(3) / 2
    poly(ax, [(x, 12), (x + side, 12), (x + side / 2, 12 + h)], role)
    text(ax, x + side / 2, 12 + h * 0.3, '60°', 'sujet', 's')
    x += side + 5
text(ax, 44, 56, 'angles : 60°, 60°, 60°', 'encre', 'm')
text(ax, 44, 6, 'même forme, taille inconnue : la base manque', 'varie', 's')
text(ax, 44, 50, 'quelle taille ?', 'varie', 's')
save(fig, '38-098')
