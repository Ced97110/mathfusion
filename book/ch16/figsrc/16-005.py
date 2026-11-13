import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
x0 = 6; L = 76; s = L / 2846; w = 408 * s
text(ax, 44, 56, 'tour cherché', 'resultat', 'm')
box(ax, x0, 42, L, 9, 'resultat', label='2 846 m', size='m')
text(ax, x0, 36, 'essai 100 et 104', 'varie', 's', ha='left')
box(ax, x0, 27, w, 7, 'varie', label='408 m', size='s')
brace(ax, x0 + w + 1, x0 + L, 25, 'limite', label='trop court', down=True)
text(ax, 44, 8, 'quelle largeur essayer ensuite ?', 'varie', 'm')
save(fig, '16-005')
