import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 86, 'pairs → 0, impairs → 1', 'fixe', 's')
text(ax, 44, 76, r'$f_{2}=x^{6}+x^{4}+x^{2}+x+1$', 'sujet', 'l')
text(ax, 44, 62, r'reste de la division de $f_{2}$', 'encre', 'm')
for i in range(5):
    box(ax, 6 + 16 * i, 47, 12, 9, 'fixe', label='≠ 0', size='s')
for a, b, lab in [(0, 1, 'degré 1'), (2, 2, 'degré 2'), (3, 4, 'degré 3')]:
    brace(ax, 6 + 16 * a, 6 + 16 * b + 12, 45.5, 'fixe', label=lab)
text(ax, 44, 32, '2 + 1 + 2 = 5 candidats', 'encre', 'm')
box(ax, 24, 14, 40, 10, 'resultat', label=r'$f_{2}$ irréductible', size='m')
text(ax, 44, 8, 'donc un cycle de longueur 6', 'resultat', 'm')
save(fig, '67-209')
