import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(56)
u = 13; G = (10, 8); T = (G[0] + 3.58 * u, 8); H = (10, 8 + 3 * u)
poly(ax, [G, T, H], 'fixe')
line(ax, [G, T], 'sujet', lw=2.2); line(ax, [H, T], 'fixe', lw=1.4)
rmark(ax, G, (1, 0), (0, 1))
line(ax, arcpts(T, 9, 140, 180), 'varie', lw=1.0)
text(ax, 49.5, 12.4, '40°', 'varie', 's')
text(ax, 30, 3.5, 'adj. : ombre 3,58 m', 'sujet', 's', weight='bold')
text(ax, 54, 33, 'hyp. : rayon', 'fixe', 's', ha='left')
text(ax, 64, 49, 'deux côtés', 'varie', 's'); text(ax, 64, 45.5, "touchent l'angle", 'varie', 's')
save(fig, '31-046')
