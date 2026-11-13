import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(46)
u = 12; G = (10, 10); T = (G[0] + 4 * u, 10); H = (10, 10 + 2.3094 * u)
poly(ax, [G, T, H], 'fixe')
line(ax, [H, T], 'sujet', lw=2.2)
rmark(ax, G, (1, 0), (0, 1))
text(ax, 10, 4, 'angle droit', 'fixe', 's', ha='left')
text(ax, 44, 39, 'hyp. = 4,62 m', 'sujet', 'm', ha='left', weight='bold')
text(ax, 37, 27.5, 'en face de l’angle droit', 'varie', 's', rot=-30)
save(fig, '31-047')
