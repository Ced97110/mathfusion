import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Quatre gestes : θ = π/2 (quart de tour), règle 1 + cos θ = 1 -> point au-dessus du pôle à distance 1
fig, ax = canvas(74)
text(ax, 44, 69.5, r'$r = f(\theta)$ se lit de droite à gauche' + '\n' + r'les gestes : de haut en bas', 'encre', 's')
steps = [('varie', r'1  choisir $\theta$ = $\pi/2$'),
         ('fixe', r'2  calculer $f(\theta)$ = 1 + 0 = 1'),
         ('sujet', r'3  tourner de $\theta$ depuis l’axe'),
         ('sujet', r'4  avancer de $r$ = 1')]
y = 52
for i, (role, lab) in enumerate(steps):
    box(ax, 2, y - 12 * i, 44, 9, role, label=lab, size='s')
    if i < 3:
        arrow(ax, (24, y - 12 * i), (24, y - 12 * i - 3), 'fixe')
o = (66, 12); u = 20
line(ax, [(o[0] - 12, o[1]), (o[0] + 18, o[1])], 'fixe')
line(ax, [o, (o[0], o[1] + 36)], 'fixe', dash=True)
line(ax, [o, (o[0], o[1] + u)], 'sujet', lw=1.8)
pts = [(o[0] + 8 * math.cos(math.radians(a)), o[1] + 8 * math.sin(math.radians(a))) for a in range(0, 91, 3)]
line(ax, pts, 'varie', lw=1.2)
disc(ax, o[0], o[1] + u, 1.3, 'sujet')
disc(ax, o[0], o[1], 0.9, 'encre')
text(ax, o[0] - 3, o[1] - 3, 'O', 'encre', 's')
text(ax, o[0] + 13, o[1] + 8, r'$\theta$ = 90°', 'varie', 's')
text(ax, o[0] + 8, o[1] + 14, r'$r$ = 1', 'sujet', 's')
save(fig, '40-030')
