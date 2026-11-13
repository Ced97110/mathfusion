import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 56, r'$2^{-1}$', 'sujet', 'xl')
text(ax, 44, 56, '=', 'encre', 'xl')
text(ax, 66, 56, r'$\frac{1}{2}$', 'resultat', 'xl')
text(ax, 44, 43, 'deux écritures de l’inverse de 2', 'fixe', 's')
for i in range(2):
    box(ax, 12 + i * 32, 20, 32, 10, 'resultat', label=r'$1/2$')
brace(ax, 12, 76, 19, 'fixe', label=r'$2\times 1/2 = 1$')
save(fig, '06-083')
