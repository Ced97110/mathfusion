import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, u = 8, 10, 8
arrow(ax, (ox - 2, oy), (ox + 4.2 * u + 6, oy), 'fixe', lw=0.9); arrow(ax, (ox, oy - 2), (ox, oy + 6.4 * u), 'fixe', lw=0.9)
line(ax, [(ox + 4 * u, oy), (ox + 4 * u, oy + 6 * u)], 'sujet', lw=1.8)
disc(ax, ox + 4 * u, oy + u, 1.1, 'varie'); disc(ax, ox + 4 * u, oy + 5 * u, 1.1, 'varie')
text(ax, ox + 4 * u - 2.5, oy + u, '(4 ; 1)', 'varie', 's', ha='right'); text(ax, ox + 4 * u - 2.5, oy + 5 * u, '(4 ; 5)', 'varie', 's', ha='right')
text(ax, ox + 4 * u - 2.5, oy + 3 * u, 'montée 4', 'varie', 's', ha='right')
line(ax, [(ox + 4 * u, oy + 3), (ox + 4 * u + 3, oy + 3), (ox + 4 * u + 3, oy)], 'resultat', lw=0.9)
text(ax, ox + 4 * u + 4.5, oy + 5.5, '90°', 'resultat', 's', ha='left')
text(ax, ox + 4 * u + 3, oy - 3.5, 'avancée 0', 'fixe', 's') if False else None
box(ax, 52, 40, 34, 11, 'sujet', label='tan 90° : non définie', size='s')
text(ax, 69, 34, '=', 'encre', 'xl', weight='bold')
box(ax, 52, 16, 34, 11, 'sujet', label='droite verticale', size='s')
text(ax, 69, 10, 'montée / avancée = 4 / 0', 'limite', 's') if False else None
text(ax, 69, 8, 'pente 4/0 : impossible', 'limite', 's')
text(ax, 40, 5, 'avancée 0', 'fixe', 's')
save(fig, '26-092')
