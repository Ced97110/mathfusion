import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 71, 'a = u (u⁻¹ a), avec a = 7', 'encre', 'l')
# deux écritures de 7 : l'unité est toujours un facteur
rows = [(54, '1', '7'), (36, '−1', '−7')]
for y, u, rest in rows:
    text(ax, 6, y + 6, '7 =', 'encre', 'm')
    box(ax, 12, y, 14, 12, 'sujet', label=u)
    text(ax, 31, y + 6, '×', 'encre', 'm')
    box(ax, 36, y, 14, 12, 'fixe', label=rest)
text(ax, 70, 60, 'u : une unité', 'sujet', 's')
text(ax, 70, 42, 'u : une unité', 'sujet', 's')
text(ax, 44, 30, 'ces écritures marchent pour tout a', 'fixe', 's')
# 12 : vrais diviseurs en plus
text(ax, 44, 22, 'Pour 12, d’autres diviseurs :', 'encre', 'm')
for i, d in enumerate(['2', '3', '4', '6']):
    box(ax, 12 + i * 17, 4, 14, 12, 'varie', label=d)
save(fig, '56-032')
