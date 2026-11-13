import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

fig, ax = canvas(70)
cx, cy, R = 44, 34, 20
disc(ax, cx, cy, R, 'sujet', fill=False)
for k in range(12):
    a = math.radians(30 * k)
    ax.plot([cx + (R - 1.5) * math.cos(a), cx + R * math.cos(a)], [cy + (R - 1.5) * math.sin(a), cy + R * math.sin(a)], color=COL['sujet'], lw=0.8, zorder=3)
for a, role in [(90, 'varie'), (180, 'varie'), (360, 'resultat')]:
    p = (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
    line(ax, [(cx, cy), p], 'fixe')
    disc(ax, p[0], p[1], 1.6, role)
line(ax, arc(cx, cy, 7, 0, 85), 'varie', lw=1.2)
arrow(ax, arc(cx, cy, 7, 0, 90)[-2], arc(cx, cy, 7, 0, 90)[-1], 'varie')
text(ax, cx, cy + R + 4, '3 h : 90°', 'varie', 'm')
text(ax, cx - R - 2.5, cy, '6 h : 180°', 'varie', 'm', ha='right')
text(ax, cx + R + 2.5, cy, '12 h : 360°', 'resultat', 'm', ha='left')
text(ax, cx, cy - 6, '1 h = 30°', 'sujet', 'm')
save(fig, '32-003')
