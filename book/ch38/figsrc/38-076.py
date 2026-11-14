import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role='varie'):
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    line(ax, pts, role)

fig, ax = canvas(82)
g = 14
A, B = 24, 66
d = math.radians(100)       # les deux visées ont la direction 100° (angle de 100° en A, de 80° en B)
L = 42
line(ax, [(A, g), (B, g)], 'fixe', lw=1.2)
for x in (A, B):
    line(ax, [(x, g), (x + L * math.cos(d), g + L * math.sin(d))], 'sujet', lw=1.2)
    disc(ax, x, g, 1.1, 'sujet')
arc(ax, A, g, 8, 0, 100, 'varie')
arc(ax, B, g, 8, 100, 180, 'varie')
text(ax, A + 11, g + 8, r'$\alpha=100°$', 'varie', 's')
text(ax, B - 1, g + 12, r'$\beta=80°$', 'varie', 's', ha='left')
text(ax, A, g - 4, 'A', 'sujet', 'm')
text(ax, B, g - 4, 'B', 'sujet', 'm')
text(ax, (A + B) / 2, g - 4, 'rive', 'fixe', 's')
text(ax, 44, 70, r'$\alpha+\beta=100°+80°=180°$', 'encre', 'm')
text(ax, 44, 63, 'visées parallèles : pas de poteau', 'limite', 'm')
save(fig, '38-076')
