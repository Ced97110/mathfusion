import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(66)
u = 15; G = (8, 8); T = (G[0] + 3.58 * u, 8); H = (8, 8 + 3 * u)
poly(ax, [G, T, H], 'fixe')
line(ax, [G, H], 'autre', lw=1.8); line(ax, [G, T], 'sujet', lw=1.8)
rmark(ax, G, (1, 0), (0, 1))
line(ax, arcpts(T, 9, 140, 180), 'varie', lw=1.0)
text(ax, 49.5, 12.4, '40°', 'varie', 's')
text(ax, 11, 30, 'poteau : 3 m', 'autre', 's', ha='left')
text(ax, 35, 3.5, 'ombre : 3,58 m', 'sujet', 's')
text(ax, 48, 26, 'rayon', 'fixe', 's', ha='left')
text(ax, 36, 60, 'cotan 40°', 'sujet', 'l', ha='left', weight='bold')
text(ax, 36, 53, '= 3,58 ÷ 3', 'resultat', 'm', ha='left')
text(ax, 36, 46, '≈ 1,19', 'resultat', 'm', ha='left')
save(fig, '31-040')
