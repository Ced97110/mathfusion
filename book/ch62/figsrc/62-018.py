import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, s = 40, 38, 28
ang = [0, 120, 240]
P = [(cx + s * math.cos(math.radians(a)), cy + s * math.sin(math.radians(a))) for a in ang]
ax.add_patch(Circle((cx, cy), s, fill=False, ec=COL['fixe'], ls='--', lw=0.8, zorder=1))
def arc(a0, a1):
    d = 17; q0 = math.radians(a0 + d); q1 = math.radians(a1 - d)
    arrow(ax, (cx + s * math.cos(q0), cy + s * math.sin(q0)), (cx + s * math.cos(q1), cy + s * math.sin(q1)),
          'varie', lw=1.3, curve=math.tan(math.radians(a1 - a0 - 2 * d) / 4))
arc(0, 120); arc(120, 240); arc(240, 360)
disc(ax, *P[0], 1.7, 'resultat'); disc(ax, *P[1], 1.7, 'sujet'); disc(ax, *P[2], 1.7, 'sujet')
text(ax, P[0][0] + 3, P[0][1] + 3.5, '$j^3 = 1$', 'resultat', 'm', ha='left')
text(ax, P[1][0] - 3, P[1][1] + 3.5, '$j$', 'sujet', 'm', ha='right')
text(ax, P[2][0] - 3, P[2][1] - 3.5, '$j^2$', 'sujet', 'm', ha='right')
text(ax, cx + 11, cy + 25, '× $j$', 'varie', 's')
text(ax, cx - 28, cy, '× $j$', 'varie', 's')
text(ax, cx + 11, cy - 25, '× $j$', 'varie', 's')
text(ax, 44, 76, '$j^3 = 1$ et $j \\neq 1$', 'encre', 'l')
text(ax, 44, 3, '3 fois × $j$ : retour en 1, mais $j$ n’est pas 1', 'encre', 's')
text(ax, cx - 3, cy + 5, '$j$ = (−0,5 ; 0,87)', 'sujet', 's', ha='right') if False else None
save(fig, '62-018')
