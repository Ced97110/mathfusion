import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(62)
cx, cy, r = 20, 34, 14
line(ax, [(cx - r, cy), (cx + r, cy)], 'fixe')
line(ax, arc(cx, cy, r, 0, 180, 180), 'autre', lw=1.4)
for d in range(0, 181):
    L = 2.6 if d % 10 == 0 else 1.1
    a = math.radians(d)
    line(ax, [(cx + r * math.cos(a), cy + r * math.sin(a)), (cx + (r - L) * math.cos(a), cy + (r - L) * math.sin(a))], 'autre', lw=0.3 if d % 10 else 0.6)
text(ax, cx, cy + 4, '180°', 'autre', 'l')
text(ax, cx, 25, '180 parts de 1°', 'autre', 's')
text(ax, cx, 19, 'choix humain', 'autre', 's', weight='bold')
text(ax, 43, cy + 4, '=', 'resultat', 'xl')
cx2, cy2, r2 = 66, 42, 12
ax.add_patch(Circle((cx2, cy2), r2, ec=COL['sujet'], fc=FILL['sujet'], lw=1.4, zorder=2))
line(ax, [(cx2 - r2, cy2), (cx2 + r2, cy2)], 'varie', lw=1.8)
text(ax, cx2, cy2 + 5, r'$\pi$', 'sujet', 'l')
text(ax, cx2, 25, 'tour ÷ diamètre', 'sujet', 's')
text(ax, cx2, 19, 'propriété du cercle', 'sujet', 's', weight='bold')
save(fig, '29-051')
