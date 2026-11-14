import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(56)
ox, oy = 10, 8
a60 = math.radians(60)
poly(ax, [(ox, oy)] + arc(ox, oy, 16, 0, 60), 'sujet')
line(ax, [(ox, oy), (ox + 70, oy)], 'fixe')
line(ax, [(ox, oy), (ox + 40 * math.cos(a60), oy + 40 * math.sin(a60))], 'fixe')
line(ax, arc(ox, oy, 16, 0, 60), 'sujet', lw=1.8)
line(ax, arc(ox, oy, 27, 0, 60), 'autre', lw=1.6, dash=True)
text(ax, ox + 10.5 * math.cos(math.radians(28)), oy + 10.5 * math.sin(math.radians(28)), r'$d$', 'sujet', 'l')
text(ax, ox + 32 * math.cos(math.radians(30)), oy + 32 * math.sin(math.radians(30)), r'$\theta$', 'autre', 'l')
text(ax, 84, 50, r'$d$ = 60 : nombre de degrés', 'sujet', 's', ha='right')
text(ax, 84, 42, r'$\theta$ : nombre de radians', 'autre', 's', ha='right')
text(ax, 84, 16, 'même angle : 60°', 'encre', 's', ha='right')
save(fig, '29-052')
