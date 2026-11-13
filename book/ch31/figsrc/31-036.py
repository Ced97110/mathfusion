import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(54)
u = 13; L = (8, 8); R = (L[0] + 4 * u, 8); H = (R[0], 8 + 2.3094 * u)
poly(ax, [L, R, H], 'fixe')
line(ax, [L, H], 'sujet', lw=1.6); line(ax, [L, R], 'autre', lw=1.6)
rmark(ax, R, (-1, 0), (0, 1))
line(ax, arcpts(L, 9, 0, 30), 'varie', lw=1.0)
text(ax, 22, 11.5, '30°', 'varie', 's')
text(ax, (L[0] + R[0]) / 2, 4, '4', 'autre', 'm', weight='bold')
text(ax, 30, 28, '4,62', 'sujet', 'm', weight='bold')
text(ax, 4, 49, 'sec 30°', 'sujet', 'l', ha='left', weight='bold')
text(ax, 4, 43, '= 4,62 ÷ 4 ≈ 1,155', 'resultat', 'm', ha='left')
text(ax, 4, 37, '= 1 ÷ cos 30°', 'sujet', 'm', ha='left')
save(fig, '31-036')
