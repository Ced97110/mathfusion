import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 3, 36, 30, 14, 'sujet', label=r'$u=(1,i)$', size='l')
box(ax, 44, 40, 18, 12, 'fixe', label=r'$1^2=1$'); box(ax, 44, 22, 38, 12, 'varie', label=r'$i^2=-1$')
arrow(ax, (34, 45), (43, 46), 'fixe'); arrow(ax, (20, 35), (44, 28), 'varie', curve=0.0)
text(ax, 72, 46, 'première coord.', 'fixe', 's') if False else None
text(ax, 72, 46, r'$1^2+i^2$', 'encre', 'm')
box(ax, 14, 4, 60, 12, 'resultat'); text(ax, 44, 10, r'$1+(-1)=0$ : $u$ isotrope sur $\mathbb{C}$', 'resultat', 's')
text(ax, 18, 54, r'$x^2+y^2$', 'sujet', 's') if False else None
save(fig, '71-204')
