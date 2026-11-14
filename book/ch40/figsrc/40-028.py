import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# f(θ) : le résultat de la règle f pour l'angle θ. Règle 1 + cos θ, θ = 60° -> 1,5
fig, ax = canvas(72)
# chaîne entrée -> règle -> résultat
box(ax, 2, 54, 22, 11, 'varie', label=r'$\theta$ = 60°')
box(ax, 33, 54, 24, 11, 'fixe', label=r'$f$ : 1 + cos $\theta$')
box(ax, 66, 54, 20, 11, 'resultat', label=r'$f(\theta)$ = 1,5')
arrow(ax, (24.5, 59.5), (32.5, 59.5), 'varie')
arrow(ax, (57.5, 59.5), (65.5, 59.5), 'fixe')
text(ax, 13, 69, 'angle donné', 'varie', 's')
text(ax, 45, 69, 'la règle', 'fixe', 's')
text(ax, 76, 69, 'son résultat', 'resultat', 's')
# diagramme polaire : u = 20 mm par unité
o = (12, 12); u = 20
t = math.radians(60); r = 1.5
line(ax, [o, (o[0] + 2.2 * u, o[1])], 'fixe')
q = (o[0] + u * r * math.cos(t), o[1] + u * r * math.sin(t))
line(ax, [o, (o[0] + 1.9 * u * math.cos(t), o[1] + 1.9 * u * math.sin(t))], 'fixe', dash=True)
line(ax, [o, q], 'resultat', lw=1.8)
pts = [(o[0] + 9 * math.cos(math.radians(a)), o[1] + 9 * math.sin(math.radians(a))) for a in range(0, 61, 3)]
line(ax, pts, 'varie', lw=1.2)
disc(ax, q[0], q[1], 1.3, 'resultat')
disc(ax, o[0], o[1], 0.9, 'encre')
text(ax, o[0] - 1.5, o[1] - 3.5, 'O', 'encre', 's')
text(ax, o[0] + 14, o[1] + 4.2, r'$\theta$', 'varie', 's')
text(ax, q[0] + 13, q[1] + 1, r'$r = f(\theta)$ = 1,5', 'resultat', 's')
text(ax, 60, 24, 'le point est à la', 'encre', 's')
text(ax, 60, 20, r'distance $r = f(\theta)$', 'encre', 's')
text(ax, 60, 16, 'du pôle O', 'encre', 's')
save(fig, '40-028')
