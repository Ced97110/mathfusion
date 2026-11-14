import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# panneau gauche : x^2+1 sur Q, sans racine
text(ax, 21, 61, r'sur $\mathbb{Q}$ : $x^2+1$ ne se casse pas', 'sujet', 's')
cx, base, sx, sy = 21, 24, 7.0, 4.0
line(ax, [(3, base), (39, base)], 'fixe')
xs = [i / 20 for i in range(-36, 37)]
line(ax, [(cx + x * sx, base + (x * x + 1) * sy) for x in xs], 'sujet', lw=1.2)
text(ax, 21, 17, 'aucune racine', 'fixe', 's')
# panneau droit : modulo 2
text(ax, 66, 61, 'modulo 2 : il se casse', 'varie', 's')
box(ax, 47, 40, 17, 9, 'varie', label=r'$x+1$')
text(ax, 67, 44.5, r'$\times$', 'encre', 'm')
box(ax, 70, 40, 17, 9, 'varie', label=r'$x+1$')
text(ax, 66, 32, r'$2x=0$ modulo 2', 'varie', 's')
text(ax, 66, 24, r'$(x+1)^2 = x^2+1$', 'varie', 's')
arrow(ax, (41, 50), (46, 50), 'varie')
box(ax, 14, 3, 60, 8, 'limite', label='la réciproque est fausse')
save(fig, '54-233')
