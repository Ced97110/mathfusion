import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# case 1 : P = O
text(ax, 22, 57, 'cas 1 : P = O', 'sujet', 's', weight='bold')
line(ax, [(4, 38), (40, 38)], 'fixe'); line(ax, [(22, 24), (22, 52)], 'fixe')
disc(ax, 22, 38, 1.5, 'sujet')
text(ax, 30, 43, 'P = O', 'sujet', 's')
text(ax, 22, 15, 'chaque terme a un facteur 0', 'encre', 's')
text(ax, 22, 7, 'q = 0', 'resultat', 'l', weight='bold')
# case 2 : P = (3, 4)
o, u = (52, 28), 4
text(ax, 66, 57, 'cas 2 : dérivées nulles en P', 'sujet', 's', weight='bold')
line(ax, [(48, 28), (84, 28)], 'fixe'); line(ax, [(52, 24), (52, 52)], 'fixe')
px, py = o[0] + 3 * u, o[1] + 4 * u
line(ax, [(px, 28), (px, py)], 'varie', dash=True); line(ax, [(52, py), (px, py)], 'varie', dash=True)
disc(ax, px, py, 1.5, 'sujet')
text(ax, px, 24.5, '3', 'varie', 's'); text(ax, 48.5, py, '4', 'varie', 's')
text(ax, px + 8, py + 3, 'P (3 ; 4)', 'sujet', 's')
text(ax, 66, 15, r'$q = 3\times 0 - 4\times 0$', 'encre', 's')
text(ax, 66, 7, 'q = 0', 'resultat', 'l', weight='bold')
save(fig, '70-152')
