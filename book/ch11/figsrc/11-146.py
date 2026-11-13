import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (22, 8); u = 1.8
allc = [(i, j, k) for i in range(10) for j in range(10) for k in range(10)]
cubes(ax, [c for c in allc if c != (0, 0, 0)], o, u, 'sujet')
cubes(ax, [(0, 0, 0)], o, u, 'varie')
text(ax, 22, 54, '1 m³ = 10 × 10 × 10', 'sujet', 'm')
text(ax, 22, 3.5, '1 000 petits cubes', 'sujet', 's')
arrow(ax, (46, 32), (25.5, 8.2), 'varie', curve=0.3)
box(ax, 46, 30, 17, 8, 'varie', label='1 L')
text(ax, 75, 34, 'un petit cube', 'varie', 's')
# conversions
box(ax, 46, 18, 15, 8, 'sujet', label='0,35 m³', size='s')
arrow(ax, (62, 22), (71, 22), 'varie'); text(ax, 66.5, 26.5, '× 1 000', 'varie', 's')
box(ax, 72, 18, 14, 8, 'resultat', label='350 L', size='s')
box(ax, 46, 5, 15, 8, 'sujet', label='0,6 m³', size='s')
arrow(ax, (71, 9), (62, 9), 'varie'); text(ax, 66.5, 13.5, '÷ 1 000', 'varie', 's')
box(ax, 72, 5, 14, 8, 'resultat', label='600 L', size='s')
save(fig, '11-146')
