import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(88)
text(ax, 44, 82, r'règle du corps : $\alpha^3 = 1 + \alpha$', 'fixe', 'm')
text(ax, 2, 70, '1 + x + x³', 'sujet', 's', ha='left')
brow(fig, ax, 58, 70, '1101000', roles=['sujet' if c == '1' else 'fixe' for c in '1101000'])
text(ax, 58, 61, r'$x \to \alpha$ : $1 + \alpha + (1 + \alpha)$', 'encre', 's')
text(ax, 58, 53, '= 0 : dans le code', 'resultat', 'm')
line(ax, [(2, 46), (86, 46)], 'fixe')
text(ax, 2, 38, '1 + x', 'sujet', 's', ha='left')
brow(fig, ax, 58, 38, '1100000', roles=['sujet' if c == '1' else 'fixe' for c in '1100000'])
text(ax, 58, 29, r'$x \to \alpha$ : $1 + \alpha$', 'encre', 's')
text(ax, 58, 21, '≠ 0 : pas dans le code', 'limite', 'm')
text(ax, 44, 8, 'c(x) dans le code ⇔ c(α) = 0', 'resultat', 's')
save(fig, '68-203')
