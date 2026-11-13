import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
u = 5; ly = 8; E = (16, ly); F = (E[0] + 5 * u, ly)
A = (E[0], ly + 8); B = (F[0], A[1] + 5 * u * math.sqrt(3)); C = (F[0], A[1])
line(ax, [(8, ly), (60, ly)], 'fixe', lw=1.0)
line(ax, [A, E], 'fixe', dash=True); line(ax, [B, F], 'fixe', dash=True)
line(ax, [A, C], 'sujet', lw=1.4, dash=True)
line(ax, [A, B], 'resultat', lw=2.0)
line(ax, [E, F], 'sujet', lw=2.4)
for p, sx, sy in ((E, 1, 1), (F, -1, 1)):
    line(ax, [(p[0] + sx * 2, p[1]), (p[0] + sx * 2, p[1] + 2), (p[0], p[1] + 2)], 'fixe', lw=0.7)
t = math.radians(60)
line(ax, [(A[0] + 10 * math.cos(a * t / 20), A[1] + 10 * math.sin(a * t / 20)) for a in range(21)], 'varie', lw=1.0)
text(ax, A[0] + 13, A[1] + 7, 'θ', 'varie', 'm')
for s, p, dx, dy in (('A', A, -3, 0), ('B', B, 0, 3.5), ('C', C, 3, -2.5), ('E', E, -2.5, -3), ('F', F, 2.5, -3)):
    text(ax, p[0] + dx, p[1] + dy, s, 'encre', 'm')
text(ax, 60, ly + 2.5, 'l', 'fixe', 'm', ha='left')
text(ax, 28, 42, 'AB = 10', 'resultat', 'm', ha='right')
text(ax, 30, ly - 4, 'EF = 5', 'sujet', 'm') if False else None
box(ax, 54, 38, 32, 16, 'sujet'); text(ax, 70, 49, 'EF = AB cos θ', 'sujet', 'm'); text(ax, 70, 42.5, '5 = 10 × cos 60°', 'sujet', 's')
save(fig, '26-093')
