import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(60)
cx, cy, r = 20, 30, 15
disc(ax, cx, cy, r, 'fixe', fill=False)
poly(ax, [(cx, cy)] + arcpts(cx, cy, r, -6, 6), 'sujet')
text(ax, cx, cy + r + 6, 'même virage', 'sujet', 's')
text(ax, cx, cy - r - 5, '104,7 m', 'resultat', 'm')
box(ax, 52, 38, 34, 12, 'varie', label='12° : 0,01745', size='s')
box(ax, 52, 10, 34, 12, 'varie', label='13,33 grades : 0,01571', size='s') if False else box(ax, 52, 10, 34, 12, 'varie', label='13,33 gr. : 0,01571', size='s')
arrow(ax, (cx + r + 1, cy + 2), (52, 44), 'fixe')
arrow(ax, (cx + r + 1, cy - 2), (52, 16), 'fixe')
text(ax, 69, 30, 'change avec l’unité', 'varie', 's')
save(fig, '29-010')
