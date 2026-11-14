import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def wedge(x, y, a, r, role):
    pts = [(x, y)] + [(x + r * math.cos(a * k / 16), y + r * math.sin(a * k / 16)) for k in range(17)]
    poly(ax, pts, role, lw=0.5)
cols = [(4, 'sujet', 20.0, 'ligne de plus grande pente', 0, '20°'), (48, 'limite', 12.7, 'chemin écarté de 50°', 50, '12,7°')]
for x0, role, deg, title, phi, lab in cols:
    cx = x0 + 18
    text(ax, cx, 80, title, role, 's')
    # vue de dessus
    base = (cx, 44); L = 26
    if phi:
        line(ax, [base, (cx, 44 + L)], 'fixe', lw=1.0, dash=True)
        a = math.radians(phi)
        wedge(cx, 44, math.radians(phi), 0, role) if False else None
        pts = [base] + [(cx + 14 * math.sin(a * k / 16), 44 + 14 * math.cos(a * k / 16)) for k in range(17)]
        poly(ax, pts, role, lw=0.5)
        text(ax, cx + 8, 63, '50°', role, 's')
        arrow(ax, base, (cx + L * math.sin(a), 44 + L * math.cos(a)), role, lw=1.8)
    else:
        arrow(ax, base, (cx, 44 + L), role, lw=1.8)
    disc(ax, *base, 1.2, 'encre')
    # vue de côté
    ax0, ay0 = x0 + 2, 14
    line(ax, [(ax0, ay0), (ax0 + 38, ay0)], 'fixe', lw=1.0)
    a = math.radians(deg)
    wedge(ax0, ay0, a, 13, role)
    line(ax, [(ax0, ay0), (ax0 + 34 * math.cos(a), ay0 + 34 * math.sin(a))], role, lw=2.0)
    text(ax, ax0 + 15, ay0 - 3.5, lab, role, 'm')
text(ax, 44, 3.5, 'angle avec l’horizontale', 'fixe', 's')
save(fig, '27-055')
