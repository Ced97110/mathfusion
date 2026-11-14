import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, u = 8, 8, 8.0
P = (ox + 3 * u, oy + 4 * u); Q = (ox + 5 * u, oy)
line(ax, [(ox, oy), (ox + 6 * u, oy)], 'fixe'); line(ax, [(ox, oy), (ox, oy + 5 * u)], 'fixe')
line(ax, [P, (Q[0], P[1]), Q], 'fixe', dash=True)
arrow(ax, Q, P, 'sujet', lw=1.6, both=True)
disc(ax, P[0], P[1], 1.4, 'sujet'); disc(ax, Q[0], Q[1], 1.4, 'sujet')
text(ax, P[0] - 3, P[1] + 4, r'$x=(3,\,4)$', 'sujet', 's'); text(ax, Q[0] + 9, Q[1] + 4.5, r'$y=(5,\,0)$', 'sujet', 's')
text(ax, 66, 44, r'$x-y=(-2,\,4)$', 'varie', 's')
text(ax, 66, 36, r'$\langle x-y,\,x-y\rangle$', 'varie', 's'); text(ax, 66, 31, r'$=4+16=20$', 'varie', 's')
text(ax, 66, 22, r'$\|x-y\|=\sqrt{20}$', 'resultat', 'm', weight='bold'); text(ax, 66, 17, r'$\approx 4{,}47$', 'resultat', 's')
save(fig, '73-078')
