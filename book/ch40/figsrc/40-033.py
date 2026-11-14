import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# (0, θ) = pôle pour tout θ (0, 90°, 200°) ; le point (2 ; 0°) n'a qu'un angle sur un tour
fig, ax = canvas(70)
text(ax, 30, 66, 'distance 0', 'sujet', 'm')
text(ax, 70, 66, 'distance 2', 'autre', 'm')
o = (30, 32)
for deg, lab, dx, dy in [(0, '(0 ; 0°)', 0, 0), (90, '(0 ; 90°)', 0, 0), (200, '(0 ; 200°)', 0, 0)]:
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    line(ax, [o, (o[0] + 17 * c, o[1] + 17 * s)], 'fixe', dash=True)
    text(ax, (o[0] + 10) if deg == 0 else o[0] + (19 if deg == 200 else 25) * c, (o[1] + 4) if deg == 0 else o[1] + 21 * s + (0 if deg != 90 else 1), lab, 'sujet', 's')
disc(ax, o[0], o[1], 2.0, 'sujet')
text(ax, 30, 11, 'les trois sont le pôle O', 'sujet', 's')
text(ax, 30, 6, 'une infinité d’angles', 'sujet', 's')
# point à distance 2 : un seul angle
p0 = (58, 32); u = 10
line(ax, [(p0[0] - 4, p0[1]), (p0[0] + 30, p0[1])], 'fixe')
disc(ax, p0[0], p0[1], 1.0, 'encre')
q = (p0[0] + 2 * u, p0[1])
line(ax, [p0, q], 'autre', lw=1.8)
disc(ax, q[0], q[1], 1.5, 'autre')
text(ax, q[0] - 6, q[1] + 6, '(2 ; 0°)', 'autre', 's')
text(ax, 72, 11, 'un seul angle sur un tour', 'autre', 's')
text(ax, 72, 6, 'pour une distance > 0', 'autre', 's')
text(ax, p0[0] - 2, p0[1] - 4, 'O', 'encre', 's')
save(fig, '40-033')
