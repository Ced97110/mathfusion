import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, R = 26, 30, 22
line(ax, [(cx + R * math.cos(a * 0.05), cy + R * math.sin(a * 0.05)) for a in range(0, 127)], 'fixe')
a = math.radians(50)
Px, Py = cx + R * math.cos(a), cy + R * math.sin(a)
line(ax, [(cx, cy), (Px, cy), (Px, Py), (cx, cy)], 'sujet', lw=1.1)
disc(ax, Px, Py, 1.3, 'sujet')
text(ax, cx - 3, cy + 3, 'O', 'sujet', 's')
text(ax, Px + 3, Py + 3, 'P', 'sujet', 's')
text(ax, Px + 0.5, cy - 3, 'H', 'sujet', 's')
s = 0.8; ox, oy = 60, 18
hx, py_ = ox + (Px - cx) * s, oy + (Py - cy) * s
poly(ax, [(ox, oy), (hx, oy), (hx, py_)], 'varie', fill=False, lw=0.8)
arrow(ax, (hx - 0.4, py_ - 0.4), (ox + 1, oy + 1), 'varie', lw=1.4)
arrow(ax, (hx, py_), (hx, oy + 0.5), 'resultat', lw=1.6)
line(ax, [(hx, oy), (ox, oy)], 'fixe', lw=1.4)
text(ax, 63, 32, 'force totale', 'varie', 's')
text(ax, hx + 2, (py_ + oy) / 2, 'verticale', 'resultat', 's', ha='left')
text(ax, (ox + hx) / 2, oy - 3.5, 'horizontale', 'fixe', 's')
text(ax, 67, 46, 'même forme que OHP', 'sujet', 's')
text(ax, 44, 5, 'verticale : loi du ressort', 'resultat', 's')
save(fig, '30-164')
