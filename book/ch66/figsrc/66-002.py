import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(62)
cy, r = 33, 12
hexa = lambda cx: [P(cx, cy, r, 60 * i) for i in range(6)]
# triangle : un sommet sur deux de l'hexagone
cx = 15; disc(ax, cx, cy, r, 'fixe', fill=False)
h = hexa(cx)
for p in h: disc(ax, p[0], p[1], 0.9, 'fixe')
poly(ax, [h[0], h[2], h[4]], 'sujet')
for p in (h[0], h[2], h[4]): disc(ax, p[0], p[1], 1.3, 'varie')
text(ax, cx, cy + r + 4, r'$n=3$', 'varie'); text(ax, cx, cy - r - 6, 'triangle :\nun sommet sur deux', 'sujet', 's')
# carré : deux diamètres perpendiculaires
cx = 44; disc(ax, cx, cy, r, 'fixe', fill=False)
q = [P(cx, cy, r, 90 * i) for i in range(4)]
poly(ax, q, 'sujet')
line(ax, [q[0], q[2]], 'varie', lw=1.2); line(ax, [q[1], q[3]], 'varie', lw=1.2)
for p in q: disc(ax, p[0], p[1], 1.3, 'varie')
text(ax, cx, cy + r + 4, r'$n=4$', 'varie'); text(ax, cx, cy - r - 6, 'carré : 2 diamètres\nperpendiculaires', 'sujet', 's')
# hexagone : le rayon est reporté
cx = 73; disc(ax, cx, cy, r, 'fixe', fill=False)
h = hexa(cx)
poly(ax, h, 'sujet')
line(ax, [(cx, cy), h[0]], 'varie', lw=1.2)
for p in h: disc(ax, p[0], p[1], 1.3, 'varie')
text(ax, cx + r / 2, cy - 2.6, r'$r$', 'varie', 's')
text(ax, cx, cy + r + 4, r'$n=6$', 'varie'); text(ax, cx, cy - r - 6, 'hexagone :\non reporte $r$', 'sujet', 's')
save(fig, '66-002')
