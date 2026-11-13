import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 44; x0 = 4; y0 = 12
box(ax, x0, y0, u, u, 'fixe', fill=False, dash=True)
box(ax, x0, y0, 0.6 * u, 0.6 * u, 'sujet', label='0,36', size='l')
text(ax, x0 + 0.3 * u, y0 - 3.5, 'sin A = 0,6', 'sujet', 's')
text(ax, x0 + 0.6 * u + 1.5, y0 + 0.3 * u, 'sin A', 'sujet', 's', ha='left')
text(ax, 66, 50, 'sin² A', 'sujet', 'xl'); text(ax, 66, 42, '=', 'encre', 'm'); text(ax, 66, 34, '(sin A)²', 'sujet', 'l')
text(ax, 44, 5, 'carré du nombre 0,6 : 0,36', 'resultat', 's')
save(fig, '34-053')
