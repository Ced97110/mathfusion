import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(64)
O = (10, 6)
def at(a, r): return (O[0] + r * math.cos(math.radians(a)), O[1] + r * math.sin(math.radians(a)))
poly(ax, [O] + arcpts(O, 40, 0, 35), 'sujet'); poly(ax, [O] + arcpts(O, 40, 35, 90), 'autre')
line(ax, [O, (O[0] + 48, O[1])], 'fixe'); line(ax, [O, (O[0], O[1] + 48)], 'fixe')
line(ax, [O, at(35, 48)], 'encre')
line(ax, arcpts(O, 44, 0, 90), 'resultat', lw=1.2)
text(ax, *at(15, 28), '35°', 'sujet', 'l', weight='bold')
text(ax, *at(63, 24), '55°', 'autre', 'l', weight='bold')
text(ax, *at(45, 48), '90°', 'resultat', 'l')
text(ax, 68, 57, '35° + 55° = 90°', 'resultat', 'm')
text(ax, 68, 51, 'angles complémentaires', 'resultat', 's')
save(fig, '31-033')
