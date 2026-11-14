import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 14, 67, 'dans $E$', 'sujet', 'm')
text(ax, 70, 67, 'dans $E^\\prime$', 'autre', 'm')
text(ax, 44, 67, r'$g=x^3-2$', 'fixe', 's')
disc(ax, 14, 47, 7, 'sujet', label=r'$\sqrt[3]{2}$', size='s')
labs = [r'$\sqrt[3]{2}$', r'$j\sqrt[3]{2}$', r'$j^2\sqrt[3]{2}$']
for i, y in enumerate([59, 47, 35]):
    disc(ax, 70, y, 6, 'autre', label=labs[i], size='s')
    arrow(ax, (21, 47 + (y - 47) * 0.3), (63.5, y), 'varie')
text(ax, 44, 24, 'étage 1 : 3 choix', 'varie', 'm')
text(ax, 44, 17, 'étage 2 : 2 choix', 'varie', 'm')
box(ax, 20, 2, 48, 11, 'resultat', label=r'$3\times 2=6$ isomorphismes', size='m')
save(fig, '62-070')
