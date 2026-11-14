import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx, cy, R = 12, 8, 34
pt = lambda deg, r=R: (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
line(ax, [pt(t) for t in range(0, 61, 2)], 'fixe')
for d in (0, 20, 40, 60):
    line(ax, [(cx, cy), pt(d)], 'sujet' if d in (0, 60) else 'varie', lw=1.0)
line(ax, [pt(20), (pt(20)[0], cy)], 'fixe', dash=True)
line(ax, [(cx, cy), (pt(20)[0], cy)], 'resultat', lw=1.8)
for d in (0, 20, 40, 60):
    disc(ax, pt(d)[0], pt(d)[1], 1.0, 'sujet' if d in (0, 60) else 'varie')
text(ax, pt(10, 14)[0] + 1, pt(10, 14)[1] - 0.2, '20°', 'varie', 's')
text(ax, pt(30, 20)[0] + 2, pt(30, 20)[1], '20°', 'varie', 's')
text(ax, pt(50, 20)[0] - 1, pt(50, 20)[1] + 1, '20°', 'varie', 's')
text(ax, 22, 3, 'cos 20° ≈ 0,9397', 'resultat', 's')
text(ax, 68, 48, '8x³ − 6x − 1 = 0', 'sujet', 'm')
text(ax, 68, 40, '8 × 0,8298 ≈ 6,638', 'fixe', 's')
text(ax, 68, 34, '6 × 0,9397 ≈ 5,638', 'fixe', 's')
text(ax, 68, 28, '6,638 − 5,638 − 1 ≈ 0', 'resultat', 's')
text(ax, 68, 16, 'degré 3 : non constructible', 'limite', 's')
save(fig, '66-115')
