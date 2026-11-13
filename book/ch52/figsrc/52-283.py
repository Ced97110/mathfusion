import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,2,44,24,14,'fixe',label='chap. 51'); box(ax,32,44,24,14,'varie',label='chap. 52'); box(ax,62,44,24,14,'fixe',label='suite')
arrow(ax,(26,51),(32,51),'varie'); arrow(ax,(56,51),(62,51),'varie')
text(ax,14,38,'anneaux donnés','fixe','s'); text(ax,44,38,'outils : quotient','varie','s'); text(ax,74,38,'chap. 53 à 56','fixe','s')
box(ax,4,14,22,10,'sujet',label=r'$\mathbb{Z}$'); box(ax,33,14,22,10,'sujet',label=r'$\mathbb{Z}/12$'); box(ax,62,14,22,10,'sujet',label=r'$\mathbb{Z}/4$')
arrow(ax,(26,19),(33,19),'varie'); arrow(ax,(55,19),(62,19),'varie')
text(ax,44,5,'garde la somme et le produit','varie','s')
save(fig,'52-283')
