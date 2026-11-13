import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
u = 17.0
def panel(ox, oy, drop):
    arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.4)
    arrow(ax, (ox, oy), (ox, oy + u), 'autre', lw=1.4)
    if drop:
        arrow(ax, (ox, oy), (ox + u, oy + u), 'varie', lw=1.4)
        line(ax, [(ox + u, oy), (ox + u, oy + u)], 'autre', lw=0.7, dash=True)
        line(ax, [(ox, oy + u), (ox + u, oy + u)], 'sujet', lw=0.7, dash=True)
panel(10, 14, True)
panel(58, 14, False)
text(ax, 10 + u + 1.5, 14 - 3, '(1, 0)', 'sujet', 's', ha='center')
text(ax, 10 - 1.5, 14 + u + 3, '(0, 1)', 'autre', 's', ha='left')
text(ax, 10 + u + 2, 14 + u + 3, '(1, 1)', 'varie', 's', ha='left')
text(ax, 58 + u + 1.5, 14 - 3, '(1, 0)', 'sujet', 's', ha='center')
text(ax, 58 - 1.5, 14 + u + 3, '(0, 1)', 'autre', 's', ha='left')
text(ax, 22, 45, 'liée : (1,1) = (1,0) + (0,1)', 'varie', 's')
text(ax, 70, 45, 'base du plan', 'resultat', 's')
arrow(ax, (37, 30), (52, 30), 'varie', lw=1.2)
text(ax, 44.5, 35, 'retirer (1, 1)', 'varie', 's')
text(ax, 44.5, 25, 'engendre encore', 'resultat', 's')
save(fig, '58-283')
