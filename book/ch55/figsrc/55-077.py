import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def tri(cx, a, b, c):
    A, B, C = (cx, 58), (cx - 14, 32), (cx + 14, 32)
    for p, q in ((A, B), (A, C), (B, C)):
        d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
        line(ax, [(p[0] + ux * 3.6, p[1] + uy * 3.6), (q[0] - ux * 3.6, q[1] - uy * 3.6)], 'fixe', lw=1.0)
    vals = [(A, a), (B, b), (C, c)]
    for p, v in vals:
        disc(ax, p[0], p[1], 3.6, 'sujet', label=str(v), size='m')
    text(ax, cx - 12, 48, str(a * b), 'varie', 'm', weight='bold')
    text(ax, cx + 12, 48, str(a * c), 'varie', 'm', weight='bold')
    text(ax, cx, 26, str(b * c), 'varie', 'm', weight='bold')
    text(ax, cx, 41, str(a * b + a * c + b * c), 'resultat', 'l', weight='bold')
tri(22, 2, 3, 4)
tri(66, 1, 5, 6)
save(fig, '55-077')
