import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# r = 2a cos θ -> (x - a)² + y² = a². Cas a = 1, θ = 60° : P (0,5 ; 0,866), centre C (1 ; 0), CP = 1
fig, ax = canvas(112)
bx = [(r'$r = 2a\cos\theta$', 'sujet'),
      (r'$r^2 = 2a \cdot r\cos\theta$', 'varie'),
      (r'$x^2 + y^2 = 2ax$', 'fixe'),
      (r'$(x - a)^2 + y^2 = a^2$', 'resultat')]
for i, (lab, role) in enumerate(bx):
    y = 98 - 12 * i
    box(ax, 2, y, 46, 9, role, label=lab, size='s', weight='bold' if i == 1 else 'normal')
    if i < 3:
        arrow(ax, (25, y - 0.4), (25, y - 2.6), 'fixe')
text(ax, 68, 94.5, '× r : étape clé', 'varie', 's')
text(ax, 68, 80.5, r'$r^2 \to x^2+y^2$, $r\cos\theta \to x$', 'fixe', 's')
text(ax, 68, 70.5, 'compléter le carré', 'resultat', 's')
# vérification chiffrée : a = 1, u = 22
u = 22; o = (12, 27)
line(ax, [(o[0] + 2 * u * math.cos(math.radians(t)) ** 2, o[1] + 2 * u * math.cos(math.radians(t)) * math.sin(math.radians(t))) for t in range(0, 361, 3)], 'fixe', lw=1.0)
arrow(ax, (o[0] - 4, o[1]), (o[0] + 2 * u + 6, o[1]), 'fixe', lw=0.8)
C = (o[0] + u, o[1]); P = (o[0] + 0.5 * u, o[1] + 0.866 * u); Q = (P[0], o[1])
line(ax, [C, P], 'sujet', lw=1.5)
line(ax, [P, Q], 'resultat', lw=1.0, dash=True)
line(ax, [Q, C], 'varie', lw=1.0, dash=True)
disc(ax, C[0], C[1], 1.0, 'sujet', fill=False); disc(ax, P[0], P[1], 1.3, 'sujet'); disc(ax, o[0], o[1], 0.9, 'encre')
text(ax, P[0] - 5, P[1] + 3, '$P$', 'sujet', 's')
text(ax, C[0] + 2, C[1] - 4, '$C$ (1 ; 0)', 'sujet', 's')
text(ax, (Q[0] + C[0]) / 2, Q[1] + 3, '0,5', 'varie', 's')
text(ax, P[0] - 5, (P[1] + Q[1]) / 2, '0,866', 'resultat', 's')
text(ax, C[0] + 9, (P[1] + C[1]) / 2 + 3, '1', 'sujet', 's')
text(ax, 66, 43, r'$a = 1$, $\theta = 60°$', 'encre', 's')
text(ax, 66, 37, r'$0{,}5^2 + 0{,}866^2 = 1$ = rayon²', 'sujet', 's')
save(fig, '40-050')
