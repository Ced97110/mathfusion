import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, s = 6, 31, 20   # 1 unité = 20 mm ; cercle x² + y² = 2x : centre (1 ; 0), rayon 1
arrow(ax, (2, oy), (50, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 21), (ox, oy + 24), 'fixe', lw=0.8)
pts = [(ox + s * (1 + math.cos(t)), oy + s * math.sin(t)) for t in [2 * math.pi * i / 200 for i in range(201)]]
line(ax, pts, 'sujet', lw=1.2)
th = math.pi / 3
px, py = ox + s * 0.5, oy + s * 0.5 * math.sqrt(3)   # r = 2 cos 60° = 1
line(ax, [(ox, oy), (px, py)], 'varie', lw=1.1)
line(ax, [(px, oy), (px, py)], 'resultat', lw=1.1)
line(ax, [(ox, oy), (px, oy)], 'resultat', lw=1.1)
disc(ax, px, py, 1.0, 'sujet')
a = [(ox + 5 * math.cos(t), oy + 5 * math.sin(t)) for t in [th * i / 20 for i in range(21)]]
line(ax, a, 'varie', lw=0.8)
text(ax, ox + 8.5, oy + 2.3, 'θ', 'varie', 's')
text(ax, ox + 3.2, oy + 13, 'r', 'varie', 'm')
text(ax, px + 9, py - 8.5, 'y = r sin θ', 'resultat', 's')
text(ax, px, oy - 3, 'x = r cos θ', 'resultat', 's')
text(ax, 38, oy + 15, r'$x^2+y^2=r^2$', 'sujet', 's')
# colonne de droite : la chaîne de l'exemple
bx, bw = 52, 34
box(ax, bx, 44, bw, 10, 'sujet', label=r'$x^2+y^2=2x$', size='s')
box(ax, bx, 26, bw, 10, 'varie', label=r'$r^2=2r\cos\theta$', size='s')
box(ax, bx, 8, bw, 10, 'resultat', label=r'$r=2\cos\theta$', size='s')
arrow(ax, (bx + bw / 2, 44), (bx + bw / 2, 36), 'varie')
arrow(ax, (bx + bw / 2, 26), (bx + bw / 2, 18), 'varie')
text(ax, bx + bw / 2 + 2, 40, '3 remplacements', 'varie', 's', ha='left') if False else None
text(ax, bx + bw / 2, 59, 'cercle de centre (1 ; 0)', 'sujet', 's')
text(ax, bx + bw / 2 + 2, 22, 'divisé par r', 'varie', 's', ha='left')
save(fig, '40-084')
