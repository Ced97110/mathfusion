import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
# Rangée du haut : d -> (facteur) -> BS
box(ax, 2, 46, 18, 9, 'fixe', label='d = 1 000 m', size='s')
arrow(ax, (20.5, 50.5), (24.5, 50.5), 'varie')
box(ax, 25, 46, 38, 9, 'varie', label=r'$\times\,\sin\alpha\,/\,\sin(\beta-\alpha)$', size='s')
arrow(ax, (63.5, 50.5), (67.5, 50.5), 'varie')
box(ax, 68, 46, 18, 9, 'sujet', label='BS ≈ 5 451 m', size='s')
text(ax, 44, 40, '= 5,451 pour 18° et 21,25°', 'varie', 's', weight='bold')
# Triangle ABS à l'échelle : AB = 10 mm (1 000 m), BS = 54,5 mm (5 451 m)
g = 14.0
A = (4.0, g); B = (14.0, g)
S = (B[0] + 54.5 * math.cos(math.radians(21.25)), g + 54.5 * math.sin(math.radians(21.25)))
poly(ax, [A, B, S], 'fixe')
line(ax, [A, B], 'fixe', lw=1.8)
line(ax, [B, S], 'sujet', lw=1.8)
text(ax, 9, g - 4.5, 'd', 'fixe', 's', weight='bold')
text(ax, 36, g + 18, 'BS', 'sujet', 's', weight='bold')
save(fig, '38-042')
