import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role='varie'):
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    line(ax, pts, role)

fig, ax = canvas(86)
g = 10
line(ax, [(4, g), (84, g)], 'fixe', lw=1.0)
A, B = 22, 40
ang = math.radians(65)
for x in (A, B):
    disc(ax, x, g, 1.1, 'sujet')
    line(ax, [(x, g), (x + 40 * math.cos(ang), g + 40 * math.sin(ang))], 'sujet', lw=1.2)
    arrow(ax, (x + 40 * math.cos(ang), g + 40 * math.sin(ang)), (x + 56 * math.cos(ang), g + 56 * math.sin(ang)), 'sujet', lw=1.0)
    arc(ax, x, g, 7, 0, 65, 'varie')
text(ax, A - 3, g - 4, 'A', 'sujet', 'm')
text(ax, B + 3, g - 4, 'B', 'sujet', 'm')
text(ax, 31, g - 4, '1 km', 'fixe', 's')
text(ax, A + 11, g + 6.5, r'$\alpha$', 'varie', 's')
text(ax, B + 11.5, g + 6.5, r'$\beta$', 'varie', 's')
text(ax, 54.7, 76, 'vers une étoile', 'autre', 'm')
text(ax, 68, 38, 'très loin', 'fixe', 'm')
text(ax, 68, 33.5, r'$\beta=\alpha$', 'sujet', 'l')
save(fig, '38-074')
