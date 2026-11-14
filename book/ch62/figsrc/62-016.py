import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, s = 56, 35, 19
R = 2 ** (1 / 3)
ang = [0, 120, 240]
P = [(cx + R * s * math.cos(math.radians(a)), cy + R * s * math.sin(math.radians(a))) for a in ang]
ax.add_patch(Circle((cx, cy), R * s, fill=False, ec=COL['fixe'], ls='--', lw=0.8, zorder=1))
def arc(a0, a1):
    d = 16; q0 = math.radians(a0 + d); q1 = math.radians(a1 - d); r = R * s
    arrow(ax, (cx + r * math.cos(q0), cy + r * math.sin(q0)), (cx + r * math.cos(q1), cy + r * math.sin(q1)),
          'varie', lw=1.3, curve=math.tan(math.radians(a1 - a0 - 2 * d) / 4))
arc(0, 120); arc(120, 240)
for (x, y) in P:
    disc(ax, x, y, 1.5, 'sujet')
text(ax, P[0][0] + 3, P[0][1] + 3, '$r_1$', 'sujet', 'm')
text(ax, P[1][0] + 1, P[1][1] + 4, '$r_2$', 'sujet', 'm')
text(ax, P[2][0] + 1, P[2][1] - 4, '$r_3$', 'sujet', 'm')
text(ax, cx + 6, cy + 17, '× $j$', 'varie', 'm')
text(ax, cx - 28, cy, '× $j$', 'varie', 'm')
text(ax, 2, 60, '$r_2 = j\\,r_1$', 'sujet', 'l', ha='left')
text(ax, 2, 50, '$r_3 = j^2 r_1$', 'sujet', 'l', ha='left')
text(ax, 2, 36, '$j$ = un tiers\nde tour autour\ndu centre', 'varie', 's', ha='left')
save(fig, '62-016')
