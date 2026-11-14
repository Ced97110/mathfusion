import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(90)
sh = lambda w: w[-1] + w[:-1]
text(ax, 44, 84, r'$g = 1 + x + x^3$ divise $x^7 + 1$', 'resultat', 's')
brow(fig, ax, 24, 72, '1100101', role='resultat', size='s', k=4, h=5.0)
brow(fig, ax, 64, 72, sh('1100101'), role='resultat', size='s', k=4, h=5.0)
arrow(ax, (43, 72), (47, 72), 'varie')
text(ax, 45, 78, 'décalage', 'varie', 's')
text(ax, 44, 64, 'les deux restent des multiples', 'resultat', 's')
line(ax, [(2, 58), (86, 58)], 'fixe')
text(ax, 44, 52, r'$1 + x^2$ ne divise pas $x^7 + 1$', 'limite', 's')
brow(fig, ax, 24, 40, '0000101', role='resultat', size='s', k=4, h=5.0)
brow(fig, ax, 64, 40, sh('0000101'), role='limite', size='s', k=4, h=5.0)
arrow(ax, (43, 40), (47, 40), 'varie')
text(ax, 45, 46, 'décalage', 'varie', 's')
text(ax, 24, 31, 'multiple de 1 + x²', 'resultat', 's')
text(ax, 64, 31, 'plus un multiple', 'limite', 's')
save(fig, '68-190')
