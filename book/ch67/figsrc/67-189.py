import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$x=\alpha^{7}$ dans $x^{4}+x^{3}+1$', 'encre', 'm')
text(ax, 62, 55, r'colonnes : $1,\ \alpha,\ \alpha^{2},\ \alpha^{3}$', 'fixe', 's')
rows = [(44, r'$\alpha^{28}=\alpha^{13}$', '1  0  1  1'), (33, r'$\alpha^{21}=\alpha^{6}$', '0  0  1  1'), (22, '1', '1  0  0  0')]
for y, lab, bits in rows:
    text(ax, 3, y, lab, 'sujet', 'm', ha='left')
    text(ax, 62, y, bits, 'sujet', 'l')
text(ax, 31, 33, '+', 'encre', 'l')
text(ax, 31, 22, '+', 'encre', 'l')
line(ax, [(44, 16.5), (80, 16.5)], 'fixe')
text(ax, 3, 9, 'somme (mod 2)', 'resultat', 'm', ha='left')
text(ax, 62, 9, '0  0  0  0', 'resultat', 'l')
save(fig, '67-189')
