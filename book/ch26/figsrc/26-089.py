import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(54)
x0, y0, L = 4, 34, 66
rise = L * 0.1
line(ax, [(x0, y0), (x0 + L, y0)], 'fixe', lw=1.2, dash=True)
line(ax, [(x0 + L, y0), (x0 + L, y0 + rise)], 'sujet', lw=1.8)
line(ax, [(x0, y0), (x0 + L, y0 + rise)], 'autre', lw=1.8)
text(ax, x0 + L / 2, y0 - 3.5, 'avancée : non mesurée', 'fixe', 's')
text(ax, x0 + L + 2, y0 + rise / 2 + 1, 'montée', 'sujet', 's', ha='left')
text(ax, x0 + L + 2, y0 + rise / 2 - 2.5, '100 m', 'sujet', 's', ha='left')
text(ax, x0 + L / 2, y0 + rise + 4.5, 'route mesurée : 1 000 m', 'autre', 's')
box(ax, 8, 8, 72, 13, 'resultat'); text(ax, 44, 17, 'rapport mesuré', 'resultat', 's'); text(ax, 44, 11.5, '100 / 1 000 = 0,1 = sin θ', 'resultat', 'm', weight='bold')
save(fig, '26-089')
