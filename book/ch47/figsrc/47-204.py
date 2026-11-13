import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 24, 33, 20
labs = ['$e$', '$x$', '$x^2$', '$x^3$', '$x^4$']
pts = []
for i in range(5):
    a = math.pi/2 - i*2*math.pi/5
    pts.append((cx + R*math.cos(a), cy + R*math.sin(a)))
for i, p in enumerate(pts):
    q = pts[(i + 1) % 5]; d = math.hypot(q[0]-p[0], q[1]-p[1]); ux, uy = (q[0]-p[0])/d, (q[1]-p[1])/d
    arrow(ax, (p[0] + ux*5.5, p[1] + uy*5.5), (q[0] - ux*5.5, q[1] - uy*5.5), 'varie')
for i, p in enumerate(pts):
    disc(ax, p[0], p[1], 5, 'fixe' if i == 0 else ('sujet' if i == 1 else 'resultat'), label=labs[i], size='m')
text(ax, 68, 52, r'$p=5$ éléments', 'encre', 's')
text(ax, 68, 40, r'$\langle x\rangle$ contient', 'sujet', 's'); text(ax, 68, 35, r'au moins 2', 'sujet', 's')
text(ax, 68, 25, 'taille divise 5', 'varie', 's'); text(ax, 68, 17, r'donc $\langle x\rangle=G$', 'resultat', 's')
save(fig, '47-204')
