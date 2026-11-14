import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
for i in range(4):
    disc(ax, 6 + 6 * i, 68, 2, 'sujet')
text(ax, 32, 68, r'$2^{2}=4$ éléments', 'sujet', 'm', ha='left')
box(ax, 2, 50, 22, 11, 'sujet', label=r'$(a+b)^{2}$')
text(ax, 28, 55.5, '=', 'encre', 'l')
box(ax, 32, 50, 50, 11, 'fixe', label=r'$a^{2}+2ab+b^{2}$')
arrow(ax, (57, 50), (57, 42), 'varie')
box(ax, 10, 31, 70, 11, 'varie', label=r'$2=0$ donc $2ab=0$')
arrow(ax, (45, 31), (45, 23), 'resultat')
box(ax, 10, 12, 70, 11, 'resultat', label=r'$(a+b)^{2}=a^{2}+b^{2}$')
text(ax, 44, 5, r'Frobenius : $a\mapsto a^{2}$', 'encre', 'm')
save(fig, '66-140')
