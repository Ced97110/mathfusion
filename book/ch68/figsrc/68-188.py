import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(80)
text(ax, 44, 74, r'$g = 1 + x + x^3$ divise $x^7 + 1$', 'sujet', 's')
box(ax, 26, 28, 36, 30, 'sujet', label='code =\nmultiples de g', size='m')
# deux boucles : une opération sur des mots du code redonne un mot du code
arrow(ax, (25, 32), (25, 54), 'varie', curve=-0.9)
text(ax, 2, 43, 'somme de\ndeux mots', 'varie', 's', ha='left')
arrow(ax, (63, 54), (63, 32), 'varie', curve=-0.9)
text(ax, 86, 43, 'décalage\n(× x)', 'varie', 's', ha='right')
text(ax, 44, 14, 'stable par + et par × x', 'resultat', 'm')
text(ax, 44, 6, 'donc idéal de R₇', 'resultat', 's')
save(fig, '68-188')
