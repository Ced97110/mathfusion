import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$V$ : 4 permutations de 4 objets', 'sujet', 'm')
s = 11.0
# corners: 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right
pos = lambda x0, c: {1: (x0, 36), 2: (x0 + s, 36), 3: (x0, 36 - s), 4: (x0 + s, 36 - s)}[c]
panels = [(6, [], '1'), (28, [(1, 2), (3, 4)], '(12)(34)'), (50, [(1, 3), (2, 4)], '(13)(24)'), (72, [(1, 4), (2, 3)], '(14)(23)')]
for i, (x0, pairs, cap) in enumerate(panels):
    for c in (1, 2, 3, 4):
        p = pos(x0, c)
        disc(ax, p[0], p[1], 2.3, 'sujet', label=str(c) if i == 0 else None, size='s')
    for a, b in pairs:
        pa, pb = pos(x0, a), pos(x0, b)
        dx, dy = pb[0] - pa[0], pb[1] - pa[1]
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        arrow(ax, (pa[0] + ux * 2.9, pa[1] + uy * 2.9), (pb[0] - ux * 2.9, pb[1] - uy * 2.9), 'varie', both=True)
    text(ax, x0 + s / 2, 18, cap, 'varie' if pairs else 'fixe', 's')
text(ax, 44, 8, 'les 3 autres : aucun objet immobile', 'fixe', 's')
save(fig, '65-078')
