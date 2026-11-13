import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Preuve : f(-θ) = f(θ) pour tout θ  =>  r = f(θ) = f(-θ)  =>  M1 (r ; -θ) est sur la courbe. Cardioïde : P (1,5 ; 60°)
fig, ax = canvas(92)
box(ax, 2, 70, 44, 12, 'fixe', label=r'départ : $f(-\theta) = f(\theta)$', size='s')
box(ax, 2, 50, 44, 12, 'sujet', label=r'$M\,(r\,;\,\theta)$ : $r = f(\theta)$', size='s')
box(ax, 2, 30, 44, 12, 'varie', label=r'$r = f(\theta) = f(-\theta)$', size='s', weight='bold')
box(ax, 2, 10, 44, 12, 'resultat', label=r'$M_1\,(r\,;\,-\theta)$ sur la courbe', size='s')
for y in (70, 50, 30):
    arrow(ax, (24, y - 0.5), (24, y - 7.5), 'fixe')
arrow(ax, (47, 36), (52, 36), 'varie')
text(ax, 69, 36, 'étape qui porte la preuve', 'varie', 's')
# cardioïde r = 1 + cos θ, u = 10 mm
o = (62, 56); u = 10
f = lambda t: 1 + math.cos(t)
pts = [(o[0] + u * f(t) * math.cos(t), o[1] + u * f(t) * math.sin(t)) for t in [i * 2 * math.pi / 300 for i in range(301)]]
line(ax, pts, 'fixe', lw=1.2)
line(ax, [(o[0] - 6, o[1]), (o[0] + 24, o[1])], 'fixe', lw=0.7)
t = math.radians(60)
P = (o[0] + u * 1.5 * math.cos(t), o[1] + u * 1.5 * math.sin(t)); P1 = (P[0], 2 * o[1] - P[1])
line(ax, [o, P], 'sujet', lw=1.2); line(ax, [o, P1], 'resultat', lw=1.2)
line(ax, [P, P1], 'fixe', lw=0.7, dash=True)
disc(ax, P[0], P[1], 1.4, 'sujet'); disc(ax, P1[0], P1[1], 1.4, 'resultat'); disc(ax, o[0], o[1], 0.8, 'encre')
text(ax, P[0] + 4, P[1] + 3, '$P$', 'sujet', 's')
text(ax, P1[0] + 5, P1[1] - 3, '$P_1$', 'resultat', 's')
text(ax, 67, 26, r'$\cos 60° = \cos(-60°) = 0{,}5$', 'varie', 's')
text(ax, 67, 21, r'donc $r$ = 1,5 pour 60° et $-60°$', 'varie', 's')
save(fig, '40-043')
