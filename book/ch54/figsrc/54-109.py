import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
assert 1 + 6 + 9 == 16 == 4 * 4
box(ax, 6, 68, 76, 11, 'fixe', label=r'départ : formule de $\eta_u$', size='m')
arrow(ax, (44, 67.5), (44, 59.5), 'varie')
box(ax, 6, 46, 76, 13, 'varie', label=r'$u^j\,u^k=u^{j+k}$', size='l')
text(ax, 70, 61.5, 'étape clé', 'varie', 's')
arrow(ax, (44, 45.5), (44, 37.5), 'varie')
box(ax, 6, 25, 76, 12, 'resultat', label=r'$\eta_u(AB)=\eta_u(A)\,\eta_u(B)$', size='m')
text(ax, 44, 15, r'exemple : $A=B=1+x$, $u=3$', 'encre', 's')
text(ax, 44, 7, r'$1+6+9=16=4\times4$', 'resultat', 'm')
save(fig, '54-109')
