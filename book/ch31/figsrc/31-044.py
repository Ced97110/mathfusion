import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def BX(ax, x, y, w, h, role, label, size='m', weight='normal'): return box(ax, x, y, w, h, role, label=label, size=size, weight=weight)
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(46)
O = (8, 8); R = 22; B = (O[0], O[1] + R)
line(ax, arcpts(O, R, 0, 90), 'fixe'); line(ax, [O, (O[0] + R + 2, O[1])], 'fixe')
line(ax, [B, (B[0] + R + 2, B[1])], 'fixe', dash=True)
line(ax, [O, B], 'sujet', lw=1.6)
disc(ax, B[0], B[1], 1.1, 'varie')
text(ax, 3, B[1] + 4, 'B = P = S', 'varie', 's', ha='left'); text(ax, O[0] - 3, O[1] - 2, 'O', 'encre', 's')
text(ax, 22, 33, 'BS = 0', 'varie', 's')
text(ax, 52, 38, 'tan', 'sujet', 's', weight='bold'); text(ax, 73, 38, 'cotan', 'autre', 's', weight='bold')
for y, a, c1, r1, c2, r2 in [(22, '0°', '= 0', 'resultat', "n'existe pas", 'limite'), (8, '90°', "n'existe pas", 'limite', '= 0', 'resultat')]:
    text(ax, 38, y + 5, a, 'encre', 'm', weight='bold')
    BX(ax, 42, y, 21, 10, r1, c1, 's'); BX(ax, 65, y, 21, 10, r2, c2, 's')
save(fig, '31-044')
