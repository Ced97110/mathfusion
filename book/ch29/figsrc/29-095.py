import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, R = 44, 12
a0, a1 = 90 - 57.3, 90 + 57.3
cy = 34 - R * math.cos(1.0)
P = (cx + R * math.cos(math.radians(a1)), cy + R * math.sin(math.radians(a1)))
Q = (cx + R * math.cos(math.radians(a0)), cy + R * math.sin(math.radians(a0)))
poly(ax, arcp(cx, cy, R, a0, a1), 'sujet')
line(ax, arcp(cx, cy, R, a0, a1), 'varie', lw=2.0)
line(ax, [P, Q], 'resultat', lw=2.0)
text(ax, cx, 44, 'arc', 'varie', 's')
text(ax, cx, 29.5, 'corde', 'resultat', 's')
u = 7
box(ax, 5.3, 12, 6 * u, 8, 'varie', label='arc 6 cm', size='s')
box(ax, 5.3 + 6 * u, 12, 5.05 * u, 8, 'resultat', label='corde ≈ 5,05 cm', size='s')
brace(ax, 5.3, 5.3 + 11.05 * u, 12, 'sujet', label='périmètre = 6 + 5,05 = 11,05 cm')
save(fig, '29-095')
