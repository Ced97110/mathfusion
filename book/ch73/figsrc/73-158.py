import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
line(ax, [(10, 12), (10, 48)], 'fixe', dash=True)
line(ax, [(3, 12), (80, 12)], 'sujet', lw=1.6); text(ax, 83, 16, r'$D$', 'sujet', 'l')
disc(ax, 37, 12, 1.3, 'sujet'); disc(ax, 64, 12, 1.3, 'resultat'); disc(ax, 10, 39, 1.3, 'limite')
text(ax, 37, 7, r'$p=(3,0)$', 'sujet', 's'); text(ax, 64, 7, r'$(6,0)$', 'resultat', 's'); text(ax, 14, 39, r'$(0,3)$', 'limite', 's', ha='left')
arrow(ax, (39, 14), (62, 14), 'resultat', curve=-0.35); text(ax, 50, 26, 'homothétie : reste sur D', 'resultat', 's')
arrow(ax, (36, 14), (11.5, 37.5), 'limite', curve=-0.3); text(ax, 52, 47, 'quart de tour : sort de D', 'limite', 's')
save(fig, '73-158')
