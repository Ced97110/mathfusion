import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(96)
h = 15
def single(x, y, w, role):
    a, b, c = (x, y), (x + w, y), (x + w * 0.4, y + h)
    poly(ax, [a, b, c], role); line(ax, [a, b, c, a], role, 1.0)
    line(ax, [a, b], 'encre', 2.4)
# a : un triangle seul
single(34, 68, 20, 'autre')
text(ax, 44, 89, 'triangle seul : 1 base mesurée', 'autre', 's', weight='bold')
# b : trois triangles sans côté commun
for x in (6, 33, 60):
    single(x, 36, 20, 'autre')
text(ax, 44, 57, 'triangles séparés : 3 bases mesurées', 'autre', 's', weight='bold')
# c : réseau, cinq triangles qui se touchent par un côté
n = 7
V = [(6 + i * 76 / (n - 1), 4 if i % 2 == 0 else 4 + h) for i in range(n)]
for i in range(5):
    poly(ax, [V[i], V[i + 1], V[i + 2]], 'sujet'); line(ax, [V[i], V[i + 1], V[i + 2], V[i]], 'sujet', 0.9)
for i in range(1, 5):
    line(ax, [V[i], V[i + 1]], 'varie', 1.8)
line(ax, [V[0], V[1]], 'encre', 2.6)
text(ax, 44, 25, 'réseau : 1 base, 4 côtés communs', 'sujet', 's', weight='bold')
save(fig, '38-061')
