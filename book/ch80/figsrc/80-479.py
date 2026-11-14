import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(86)
C = [(44, 38, 'Möbius', 'sujet', 15, 8)]
disc(ax, 44, 40, 9, 'sujet', label='Möbius', size='s')
nodes = [(20, 70, 'parties d\'un ensemble', 'fixe'), (68, 70, 'permutations', 'fixe'), (20, 12, 'coloriages', 'fixe'), (68, 12, 'entiers sans facteur\ncommun avec 30 : 8', 'resultat')]
for x, y, l, r in nodes:
    box(ax, x - 16, y - 6, 32, 12, r, label=l, size='s')
    dx, dy = x - 44, y - 40; n = math.hypot(dx, dy)
    arrow(ax, (44 + dx / n * 9.5, 40 + dy / n * 9.5), (x - dx / n * 0 - (dx / abs(dx)) * 0, y - (6.5 if y > 40 else -6.5)), 'varie')
text(ax, 44, 82, 'Rota, 1964 : outil de la combinatoire', 'encre', 's')
save(fig, '80-479')
