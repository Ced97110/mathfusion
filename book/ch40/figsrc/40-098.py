import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
R = 16

def wheel(cx, cy):
    line(ax, [(cx + R * math.cos(u), cy + R * math.sin(u)) for u in [2 * math.pi * i / 200 for i in range(201)]], 'fixe', lw=1.0)
    line(ax, [(cx, cy), (cx, cy - R)], 'fixe', lw=1.0)
    disc(ax, cx, cy, 0.9, 'fixe')
    disc(ax, cx, cy - R, 0.9, 'fixe')

# gauche : angle t quelconque (35° dessiné)
cx, cy = 23, 35
t = math.radians(50)
wheel(cx, cy)
mx, my = cx - R * math.sin(t), cy - R * math.cos(t)
line(ax, [(cx, cy), (mx, my)], 'sujet', lw=1.2)
line(ax, [(cx, cy), (cx, my)], 'resultat', lw=1.4)
line(ax, [(mx, my), (cx, my)], 'resultat', lw=1.4)
disc(ax, mx, my, 1.2, 'varie')
line(ax, [(cx + 5 * math.cos(-math.pi / 2 - u), cy + 5 * math.sin(-math.pi / 2 - u)) for u in [t * i / 20 for i in range(21)]], 'encre', lw=0.9)
text(ax, cx - 2.2, cy - 8.5, 't', 'encre', 's')
text(ax, cx + 3, cy + 2.2, 'C', 'fixe', 's')
text(ax, cx + 2.8, cy - R - 3, 'I', 'fixe', 's')
text(ax, mx - 3.5, my + 1.5, 'M', 'varie', 's')
text(ax, cx - 8.2, (cy + my) / 2 + 4, 'a', 'sujet', 's')
text(ax, cx + 2, (cy + my) / 2, 'a cos t', 'resultat', 's', ha='left')
text(ax, (cx + mx) / 2, my - 2.4, 'a sin t', 'resultat', 's')
text(ax, 23, 6, 'angle t quelconque', 'sujet', 's')

# droite : quart de tour, a = 0,35 m
cx, cy = 66, 35
wheel(cx, cy)
mx, my = cx - R, cy
line(ax, [(cx, cy), (mx, my)], 'sujet', lw=1.2)
disc(ax, mx, my, 1.2, 'varie')
line(ax, [(cx + 5 * math.cos(-math.pi / 2 - u), cy + 5 * math.sin(-math.pi / 2 - u)) for u in [math.pi / 2 * i / 20 for i in range(21)]], 'encre', lw=0.9)
text(ax, cx - 8, cy - 8, 't = 90°', 'encre', 's')
text(ax, cx + 3, cy + 2.2, 'C', 'fixe', 's')
text(ax, cx + 2.8, cy - R - 3, 'I', 'fixe', 's')
text(ax, mx - 3.5, my + 2.4, 'M', 'varie', 's')
text(ax, (cx + mx) / 2, cy + 3, 'a = 0,35', 'sujet', 's')
text(ax, 66, 10.5, 'à gauche de C : 0,35 m', 'resultat', 's')
text(ax, 66, 6, 'sous C : 0 m', 'resultat', 's')
text(ax, 66, 1.5, 'quart de tour', 'sujet', 's') if False else None
save(fig, '40-098')
