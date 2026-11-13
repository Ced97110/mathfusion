import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pos(h, cx, cy, R):
    a = math.radians(90 - 30 * h); return (cx + R * math.cos(a), cy + R * math.sin(a))
def edge(p, q, off):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * off, p[1] + u[1] * off), (q[0] - u[0] * off, q[1] - u[1] * off)

fig, ax = canvas(56)
box(ax, 2, 24, 36, 28, 'sujet'); text(ax, 20, 46, 'Définition', 'sujet', 's', weight='bold')
text(ax, 20, 37, 'le plus petit sous-groupe\ncontenant 4', 'sujet', 's')
cx, cy, R = 68, 36, 13
for h in range(12):
    x, y = pos(h, cx, cy, R); disc(ax, x, y, 1.6, 'fixe')
text(ax, cx, cy, '?', 'limite', 'xl', weight='bold')
text(ax, cx, 14, 'quels éléments ?', 'limite', 's')
arrow(ax, (39, 38), (52, 38), 'limite'); text(ax, 45.5, 43, 'ne dit pas', 'limite', 's')
text(ax, 44, 5, 'il faut comparer avec tous les autres', 'varie', 's')
save(fig, '46-061')
