import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
c = (10, 8); s = 1.0
def P(r, d): return (c[0] + r * math.cos(math.radians(d)), c[1] + r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=40): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
R = 36
for i in range(3):
    pts = [c] + arc(R, 30 * i, 30 * (i + 1), 20)
    poly(ax, pts, 'varie' if i % 2 == 0 else 'fixe')
    mx, my = P(24, 30 * i + 15)
    text(ax, mx, my, 'θ = 30°', 'varie' if i % 2 == 0 else 'fixe', 's')
for d in (0, 30, 60, 90):
    line(ax, [c, P(R, d)], 'encre', lw=0.7)
line(ax, arc(R + 3.5, 0, 90), 'resultat', lw=1.4)
arrow(ax, P(R + 3.5, 88), P(R + 3.5, 90), 'resultat', lw=1.4)
tx, ty = P(R + 8, 45)
text(ax, tx - 12, ty + 9.5, '3 × 30° = 90°', 'resultat', 's', ha='left')
text(ax, 52, 26, 'l’angle θ est ajouté', 'encre', 's', ha='left')
text(ax, 52, 21.5, '3 fois : 3θ', 'encre', 's', ha='left')
save(fig, '39-078')
