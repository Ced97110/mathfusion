import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="encre", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(52)
s = 6.0
C = (14, 14); A = (C[0] + 4 * s, C[1]); B = (C[0], C[1] + 3 * s)
poly(ax, [C, A, B], 'fixe')
line(ax, [C, A], 'sujet', lw=2.2); line(ax, [C, B], 'varie', lw=2.2); line(ax, [A, B], 'autre', lw=2.6)
text(ax, C[0] + 2 * s, C[1] - 3.4, 'adjacent', 'sujet', 's'); text(ax, C[0] - 6.5, C[1] + 1.5 * s, 'opposé', 'varie', 's')
text(ax, C[0] + 2 * s + 6.5, C[1] + 1.5 * s + 4, 'hypoténuse :', 'autre', 's'); text(ax, C[0] + 2 * s + 6.5, C[1] + 1.5 * s + 8, 'échelle 5 m', 'autre', 's')
arc(ax, A, 5, 143.13, 180); text(ax, A[0] + 3, A[1] - 2.5, 'A', 'encre', 'm', weight='bold')
rows = [(40, 'varie', 'sujet', 'tangente'), (30, 'varie', 'autre', 'sinus (SOH)'), (20, 'sujet', 'autre', 'cosinus (CAH)')]
for y, n, d, lab in rows:
    box(ax, 46, y, 5, 5, n, lw=1.0); text(ax, 54, y + 2.5, '÷', 'encre', 'm'); box(ax, 57, y, 5, 5, d, lw=1.0)
    text(ax, 65, y + 2.5, lab, 'encre', 's', ha='left')
save(fig, '25-076')
