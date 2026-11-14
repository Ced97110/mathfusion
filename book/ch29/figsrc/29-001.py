import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(62)
cx, cy, R = 22, 31, 18
disc(ax, cx, cy, R, 'fixe', fill=False)
poly(ax, [(cx, cy)] + arcpts(cx, cy, R, -6, 6), 'sujet')
line(ax, [(cx, cy), (cx - R, cy)], 'fixe')
text(ax, cx - R / 2, cy + 3, '500 m', 'fixe', 's')
text(ax, cx + R + 4.5, cy, '12°', 'sujet', 's')
bx, bw, bh = 50, 36, 12
box(ax, bx, 46, bw, bh, 'fixe', label='tour : 3 141,6 m', size='s')
box(ax, bx, 27, bw, bh, 'sujet', label='part du tour : 1/30', size='s')
box(ax, bx, 8, bw, bh, 'resultat', label='virage ≈ 104,7 m', size='s')
arrow(ax, (bx + bw / 2, 46), (bx + bw / 2, 39), 'varie')
arrow(ax, (bx + bw / 2, 27), (bx + bw / 2, 20), 'varie')
text(ax, 20, 6, 'cercle de 500 m de rayon', 'fixe', 's')
save(fig, '29-001')
