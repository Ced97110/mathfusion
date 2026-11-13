import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
R = 15

def wheel(cx, cy):
    line(ax, [(cx + R * math.cos(u), cy + R * math.sin(u)) for u in [2 * math.pi * i / 200 for i in range(201)]], 'fixe', lw=1.0)
    disc(ax, cx, cy, 0.9, 'fixe')
    text(ax, cx + 3, cy + 2.2, 'C', 'fixe', 's') if False else None

# gauche : t petit (40° dessiné) -> M sous C
cx, cy = 22, 33
wheel(cx, cy)
t = math.radians(40)
mx, my = cx - R * math.sin(t), cy - R * math.cos(t)
line(ax, [(cx, cy), (mx, my)], 'sujet', lw=1.2)
line(ax, [(cx, cy), (cx, my)], 'resultat', lw=1.3)
line(ax, [(mx, my), (cx, my)], 'fixe', lw=0.7, dash=True)
disc(ax, mx, my, 1.2, 'varie')
text(ax, mx - 3.3, my + 1.5, 'M', 'varie', 's')
text(ax, cx + 3, cy + 2.2, 'C', 'fixe', 's')
text(ax, cx + 2, (cy + my) / 2 + 1, 'a cos t', 'resultat', 's', ha='left')
text(ax, 22, 61, 't < π/2', 'sujet', 'm')
text(ax, 22, 8, 'cos t > 0 : M sous C', 'resultat', 's')

# droite : t = π -> cos t = −1, M au-dessus de C
cx, cy = 66, 33
wheel(cx, cy)
line(ax, [(cx, cy), (cx, cy + R)], 'sujet', lw=1.2)
line(ax, [(cx + 2.5, cy), (cx + 2.5, cy + R)], 'resultat', lw=1.3) if False else None
disc(ax, cx, cy + R, 1.2, 'varie')
disc(ax, cx, cy - R, 0.9, 'fixe')
text(ax, cx + 3.3, cy + R + 1.8, 'M', 'varie', 's')
text(ax, cx + 3, cy - 2.4, 'C', 'fixe', 's')
text(ax, cx + 3.5, cy + R / 2, 'a cos t = −0,35', 'resultat', 's', ha='left') if False else None
text(ax, 66, 61, 't = π', 'sujet', 'm')
text(ax, 66, 13.5, 'cos t = −1', 'resultat', 's')
text(ax, 66, 8, 'M au-dessus de C', 'resultat', 's')
text(ax, 66, 2.5, 'y = 0,35 + 0,35 = 0,70', 'varie', 's')
save(fig, '40-101')
