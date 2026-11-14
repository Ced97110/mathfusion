import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 11, 68, r'$\times$', 'fixe', 'm')
text(ax, 35, 68, '3', 'sujet', 'm')
text(ax, 63, 68, r'$j$', 'sujet', 'm')
text(ax, 11, 53, '2', 'sujet', 'm')
text(ax, 11, 35, r'$i$', 'sujet', 'm')
cells = [(22, 46, r'$2\times 3=6$', 'sujet'), (50, 46, r'$2\times j=2j$', 'sujet'),
         (22, 28, r'$i\times 3=3i$', 'sujet'), (50, 28, r'$i\times j=k$', 'varie')]
for x, y, s, ro in cells:
    box(ax, x, y, 28, 14, ro, label=s)
text(ax, 64, 24, "d'après la table", 'varie', 's')
text(ax, 44, 18, 'on additionne les cases', 'resultat', 's')
box(ax, 14, 3, 60, 10, 'resultat', label=r'$6+3i+2j+k$', size='l')
save(fig, '51-173')
