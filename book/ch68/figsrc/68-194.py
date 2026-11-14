import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(84)
box(ax, 22, 70, 44, 10, 'varie', label=r'$g = 1 + x + x^3$ : degré 3', size='s')
arrow(ax, (58, 69), (58, 53), 'varie')
text(ax, 54, 61, 'n = 7 bits', 'encre', 's', ha='right')
xs, p = brow(fig, ax, 44, 48, BL * 7, roles=['sujet'] * 4 + ['varie'] * 3)
l = xs[0] - p / 2
brace(ax, l, l + 4 * p, 44, 'sujet', 'message : 4 bits')
brace(ax, l + 4 * p, l + 7 * p, 44, 'varie', 'contrôle : 3 bits')
text(ax, 44, 22, '2⁴ = 16 mots, distance 3', 'resultat', 'm')
text(ax, 44, 13, 'le degré de g = les 3 bits', 'fixe', 's')
save(fig, '68-194')
