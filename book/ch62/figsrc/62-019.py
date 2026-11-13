import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, s = 44, 38, 24
ang = [90, 210, 330]
P = [(cx + s * math.cos(math.radians(a)), cy + s * math.sin(math.radians(a))) for a in ang]
ax.add_patch(Circle((cx, cy), s, fill=False, ec=COL['fixe'], ls='--', lw=0.8, zorder=1))
poly(ax, P, 'sujet', fill=True)
for x, y in P:
    line(ax, [(cx, cy), (x, y)], 'fixe', lw=0.7)
def arc(a0, a1):
    d = 15; q0 = math.radians(a0 + d); q1 = math.radians(a1 - d); r = s + 4.5
    arrow(ax, (cx + r * math.cos(q0), cy + r * math.sin(q0)), (cx + r * math.cos(q1), cy + r * math.sin(q1)),
          'varie', lw=1.3, curve=math.tan(math.radians(a1 - a0 - 2 * d) / 4))
arc(90, 210); arc(210, 330); arc(330, 450)
for x, y in P:
    disc(ax, x, y, 1.6, 'sujet')
disc(ax, cx, cy, 1.1, 'encre')
text(ax, cx + 3, cy - 3, '0', 'encre', 's')
text(ax, 14, 56, '1/3 de tour', 'varie', 's')
text(ax, 76, 56, '× $j$', 'varie', 'm')
text(ax, 44, 3.5, '× $j$', 'varie', 'm')
text(ax, 44, 30, 'trois côtés égaux', 'sujet', 's')
text(ax, 44, 76, 'multiplier par $j$ = tourner autour de 0', 'encre', 'm')
save(fig, '62-019')
