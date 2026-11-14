import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="encre", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(52)
s = 7.5
def tri(x0, y0, ch):
    C = (x0, y0); A = (x0 + 4 * s, y0); B = (x0, y0 + 3 * s)
    poly(ax, [C, A, B], 'fixe')
    line(ax, [C, B], 'fixe', lw=0.9); line(ax, [A, B], 'fixe', lw=0.9)
    role = 'sujet' if ch == 'A' else 'varie'
    line(ax, [C, A], role, lw=2.6)
    text(ax, x0 - 3, y0 + 1.5 * s, '3', 'fixe', 's')
    text(ax, x0 + 2 * s + 3.0, y0 + 1.5 * s + 3.4, '5', 'fixe', 's')
    text(ax, x0 + 2 * s, y0 + 3, '4', role, 'm', weight='bold')
    if ch == 'A':
        arc(ax, A, 6, 143.13, 180); text(ax, A[0] + 3, A[1] - 3, 'A', 'encre', 'm', weight='bold')
        text(ax, x0 + 2 * s + 2, y0 - 4, '4 touche A : adjacent', role, 's')
    else:
        arc(ax, B, 6, 270, 323.13); text(ax, B[0] + 3.2, B[1] + 2.2, 'B', 'encre', 'm', weight='bold')
        text(ax, x0 + 2 * s + 2, y0 - 4, '4 ne touche pas B : opposé', role, 's')
tri(8, 12, 'A'); tri(50, 12, 'B')
text(ax, 25, 43, "pour l'angle A", 'encre', 'm'); text(ax, 67, 43, "pour l'angle B", 'encre', 'm')
save(fig, '25-067')
