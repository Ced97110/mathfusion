import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, u = 13, 12, 10.5
arrow(ax, (ox, oy), (ox + 5 * u + 6, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy), (ox, oy + 5 * u + 6), 'fixe', lw=0.8)
text(ax, ox + 5 * u + 6, oy - 3.5, r'$a$', 'fixe', 'm'); text(ax, ox - 3.5, oy + 5 * u + 6, r'$b$', 'fixe', 'm')
for i in range(6):
    for j in range(6):
        if i != j and (i, j) != (4, 1):
            disc(ax, ox + i * u, oy + j * u, 0.7, 'fixe')
line(ax, [(ox, oy), (ox + 5 * u, oy + 5 * u)], 'sujet', lw=1.4)
for k in (1, 2, 3):
    disc(ax, ox + k * u, oy + k * u, 1.6, 'sujet')
disc(ax, ox + 3 * u, oy + 3 * u, 2.0, 'resultat')
text(ax, ox + 3 * u + 2.5, oy + 3 * u - 3.5, r'$(3\ ;\ 3)$', 'resultat', 's', ha='left')
disc(ax, ox + 4 * u, oy + u, 1.6, 'limite')
text(ax, ox + 4 * u, oy + u - 4, r'$(4\ ;\ 1)$ : 3', 'limite', 's')
text(ax, 40, 75, r'$a - b = 0$ : le noyau', 'sujet', 'm')
text(ax, 62, 56, 'la différence est 0', 'resultat', 's') if False else None
save(fig, '48-198')
