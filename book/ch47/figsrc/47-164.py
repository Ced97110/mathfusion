import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'même groupe, deux sous-groupes', 'encre', 'm')
# N panel
box(ax, 3, 34, 82, 26, 'sujet', fill=False, dash=True, lw=0.7)
text(ax, 12, 52, r'$N$', 'sujet', 'l')
for i, l in enumerate(['1', '(1 2 3)', '(1 3 2)']):
    box(ax, 20 + i * 17, 41, 15, 9, 'sujet', label=l, size='s')
text(ax, 73, 51, 'gauche', 'sujet', 's'); text(ax, 73, 45, '= droite', 'resultat', 's')
text(ax, 73, 38, 'normal', 'resultat', 's')
# K panel
box(ax, 3, 4, 82, 26, 'autre', fill=False, dash=True, lw=0.7)
text(ax, 12, 22, r'$K$', 'autre', 'l')
for i, l in enumerate(['1', '(1 2)']):
    box(ax, 20 + i * 17, 11, 15, 9, 'autre', label=l, size='s')
text(ax, 73, 21, 'gauche', 'autre', 's'); text(ax, 73, 15, r'$\neq$ droite', 'limite', 's')
text(ax, 73, 8, 'pas normal', 'limite', 's')
save(fig, '47-164')
