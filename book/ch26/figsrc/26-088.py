import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 30, 50, '1', 'sujet', 'xl', ha='right', weight='bold')
text(ax, 44, 50, 'in', 'encre', 'xl', weight='bold')
text(ax, 58, 50, '55', 'fixe', 'xl', ha='left', weight='bold')
text(ax, 30, 41, 'montée 1 m', 'sujet', 's', ha='right'); text(ax, 62, 41, 'avancée 55 m', 'fixe', 's')
arrow(ax, (28, 47), (27, 43), 'sujet'); arrow(ax, (60, 47), (60, 43), 'fixe')
x0, y0, u = 4, 20, 1.3
L = 55 * u
line(ax, [(x0, y0), (x0 + L, y0)], 'fixe', lw=1.0)
line(ax, [(x0, y0), (x0 + L, y0 + u)], 'sujet', lw=1.6)
line(ax, [(x0 + L, y0), (x0 + L, y0 + u)], 'sujet', lw=2.0)
line(ax, [(x0, y0), (x0 + L, y0 + 10 * u * 5.5)], 'autre', lw=0.9, dash=True) if False else None
text(ax, x0 + L + 2, y0 + 0.5, '1', 'sujet', 's', ha='left')
text(ax, x0 + L / 2, y0 - 4, '55', 'fixe', 's')
text(ax, 44, 8, 'pente 1/55 ≈ 0,0182', 'resultat', 'm')
save(fig, '26-088')
