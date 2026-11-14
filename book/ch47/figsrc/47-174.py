import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def dots(x0, y, n, role):
    for i in range(n): disc(ax, x0 + i * 8, y, 2.8, role)
text(ax, 44, 74, 'même longueur : relié', 'resultat', 'm')
dots(10, 60, 3, 'sujet'); dots(54, 60, 3, 'resultat')
text(ax, 18, 51, r'$(1\ 2\ 3)$', 'sujet', 's'); text(ax, 62, 51, r'$(1\ 3\ 2)$', 'resultat', 's')
arrow(ax, (31, 60), (51, 60), 'resultat'); text(ax, 41, 64, 'conjugués', 'resultat', 's')
line(ax, [(3, 41), (85, 41)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 34, 'longueurs 2 et 3 : jamais', 'limite', 'm')
dots(14, 20, 2, 'sujet'); dots(54, 20, 3, 'limite')
text(ax, 18, 11, r'$(1\ 2)$', 'sujet', 's'); text(ax, 62, 11, r'$(1\ 2\ 3)$', 'limite', 's')
arrow(ax, (27, 20), (51, 20), 'limite'); text(ax, 39, 20, r'$\times$', 'limite', 'xl')
save(fig, '47-174')
