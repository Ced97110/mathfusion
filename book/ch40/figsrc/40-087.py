import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [15, 44, 73]
# cadres
box(ax, 2, 14, 26, 46, 'fixe', fill=False)
box(ax, 31, 14, 26, 46, 'fixe', fill=False)
box(ax, 60, 14, 26, 46, 'sujet', fill=False, lw=1.1)

# 1) y = f(x) : l'entrée x est une coordonnée
x0, y0 = 7, 26
arrow(ax, (x0 - 3, y0), (x0 + 19, y0), 'fixe', lw=0.7)
arrow(ax, (x0, y0 - 3), (x0, y0 + 24), 'fixe', lw=0.7)
c = [(x0 + 1 + i * 0.7, y0 + 2 + 14 * math.sin(i * 0.7 / 18 * math.pi)) for i in range(26)]
line(ax, c, 'fixe', lw=1.0)
px, py = c[13]
line(ax, [(px, y0), (px, py)], 'fixe', dash=True, lw=0.7)
disc(ax, px, py, 1.0, 'fixe')
disc(ax, px, y0, 1.2, 'varie')
text(ax, px, y0 - 4, 'x', 'varie', 's')
text(ax, cx[0], 9, 'y = f(x)', 'fixe', 's')

# 2) r = f(θ) : l'entrée θ est une coordonnée
ox, oy = 37, 30
line(ax, [(ox, oy), (ox + 19, oy)], 'fixe', lw=0.7)
ang = math.radians(50)
rr = 15
line(ax, [(ox, oy), (ox + rr * math.cos(ang), oy + rr * math.sin(ang))], 'fixe', lw=0.9)
disc(ax, ox + rr * math.cos(ang), oy + rr * math.sin(ang), 1.0, 'fixe')
line(ax, [(ox + 7 * math.cos(a_), oy + 7 * math.sin(a_)) for a_ in [ang * i / 20 for i in range(21)]], 'varie', lw=1.1)
text(ax, ox + 10, oy + 3.6, 'θ', 'varie', 's')
text(ax, cx[1], 9, 'r = f(θ)', 'fixe', 's')

# 3) x = f(t), y = g(t) : t n'est pas une coordonnée
x1, y1 = 66, 26
arrow(ax, (x1 - 3, y1), (x1 + 19, y1), 'fixe', lw=0.7)
arrow(ax, (x1, y1 - 3), (x1, y1 + 14), 'fixe', lw=0.7)
c = [(x1 + 3 + i * 0.6, y1 + 3 + 9 * math.sin(i * 0.6 / 14 * math.pi)) for i in range(26)]
line(ax, c, 'sujet', lw=1.0)
px, py = c[13]
disc(ax, px, py, 1.0, 'sujet')
line(ax, [(x1 + 1, 55), (x1 + 19, 55)], 'varie', lw=1.2)
disc(ax, x1 + 10, 55, 1.2, 'varie')
text(ax, x1 + 10, 58.5, 't', 'varie', 's') if False else None
text(ax, x1 + 4, 51.3, 't', 'varie', 's')
arrow(ax, (x1 + 10, 53.5), (px, py + 1.5), 'varie', lw=0.8)
text(ax, cx[2], 9, 'x = f(t), y = g(t)', 'sujet', 's')
text(ax, cx[0], 3.5, 'x : coordonnée', 'fixe', 's')
text(ax, cx[1], 3.5, 'θ : coordonnée', 'fixe', 's')
text(ax, cx[2], 3.5, 't : pas coordonnée', 'sujet', 's')
save(fig, '40-087')
