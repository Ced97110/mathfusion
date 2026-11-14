import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(56)
R = 22
def panel(cx, ang, name, l1, l2, role2):
    C = (cx, 24)
    line(ax, arcpts(C, R, 0, 90), 'fixe')
    line(ax, [C, (C[0] + R + 2, C[1])], 'fixe'); line(ax, [C, (C[0], C[1] + R + 2)], 'fixe')
    P = (C[0] + R * math.cos(math.radians(ang)), C[1] + R * math.sin(math.radians(ang)))
    line(ax, [C, P], 'sujet', lw=1.2)
    line(ax, [P, (P[0], C[1])], 'fixe', dash=True)
    line(ax, [C, (P[0], C[1])], 'varie', lw=2.4)
    disc(ax, P[0], P[1], 1.0, 'sujet')
    text(ax, P[0] + 3, P[1] + 2.2, 'P', 'sujet', 's')
    text(ax, cx + 11, 15.5, name, 'encre', 'l', weight='bold')
    text(ax, cx + 11, 10.5, l1, 'varie', 's')
    text(ax, cx + 11, 6, l2, role2, 's')
text(ax, 44, 52, 'il faut cos θ ≠ 0', 'sujet', 'm')
panel(8, 89, '89°', 'cos ≈ 0,0175', '1 ÷ cos 89° ≈ 57,30', 'resultat')
panel(52, 90, '90°', 'cos = 0', '1 ÷ 0 : impossible', 'limite')
save(fig, '31-037')
