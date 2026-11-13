import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
Lh = 33
def panel(x0, deg, vals, verdict, role, labels):
    y0 = 24
    t = math.radians(deg)
    B = (x0 + Lh * math.cos(t), y0); C = (x0 + Lh * math.cos(t), y0 + Lh * math.sin(t))
    line(ax, [(x0, y0), (x0 + Lh + 1, y0)], 'fixe', lw=1.2)
    line(ax, [(x0, y0), C], 'autre', lw=1.5)
    line(ax, [B, C], 'sujet', lw=1.8)
    arc = [(x0 + Lh * math.cos(a * t / 20), y0 + Lh * math.sin(a * t / 20)) for a in range(21)]
    line(ax, arc, 'varie', lw=0.9, dash=True)
    text(ax, x0 + 10, y0 + 6.5 + (3 if deg > 10 else 0), f'{deg}°', 'encre', 'm', weight='bold')
    text(ax, x0 + Lh / 2, 15.5, vals[0], 'sujet', 's'); text(ax, x0 + Lh / 2, 10.5, vals[1], 'autre', 's')
    text(ax, x0 + Lh / 2, 4.5, verdict, role, 's', weight='bold')
panel(4, 6, ('sin 0,1045', 'tan 0,1051'), 'presque égaux', 'resultat', None)
panel(48, 30, ('sin 0,5000', 'tan 0,5774'), 'écart > 15 %', 'limite', None)
x0 = 48; t = math.radians(30)
text(ax, x0 + 7, 24 + 18.5, 'route', 'autre', 's')
text(ax, x0 + Lh * math.cos(t) + 2, 24 + 8, 'montée', 'sujet', 's', ha='left')
text(ax, x0 + 24, 24 - 2.7, 'avancée', 'fixe', 's')
text(ax, x0 + Lh - 3, 24 + 3, 'écart', 'varie', 's') if False else None
save(fig, '26-090')
