import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
R, rd = 14, 4.0
def arcarrow(c, a0, a1, role='varie', lw=1.2, n=20):
    pts = [(c[0] + R * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + R * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw=lw); arrow(ax, pts[-2], pts[-1], role, lw=lw)
def clock(c, n, start, end):
    for h in range(n):
        a = math.radians(90 - 360 * h / n)
        disc(ax, c[0] + R * math.cos(a), c[1] + R * math.sin(a), rd, 'sujet' if h == start else 'resultat' if h == end else 'fixe', label=str(h), size='s')
A, B = (22, 30), (66, 30)
clock(A, 4, 3, 0); clock(B, 3, 2, 0)
arcarrow(A, 180 - 26, 90 + 26)
arcarrow(B, -150 - 26, -270 + 26)
text(ax, 9, 44, '+1', 'varie', 'm', weight='bold')
text(ax, 50, 36, '+1', 'varie', 'm', weight='bold')
text(ax, 22, 30, 'ℤ/4', 'sujet', 's'); text(ax, 66, 30, 'ℤ/3', 'sujet', 's')
text(ax, 44, 57, '(3, 2) + (1, 1) = (0, 0)', 'encre', 'l')
text(ax, 22, 8, 'lignes : 3 + 1 = 4 → 0', 'encre', 's')
text(ax, 66, 8, 'colonnes : 2 + 1 = 3 → 0', 'encre', 's')
save(fig, '60-004')
