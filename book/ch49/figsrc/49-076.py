import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,3,14,39,42,'limite'); text(ax,22.5,50,'sous-groupe seul','limite','s')
box(ax,46,14,39,42,'resultat'); text(ax,65.5,50,'sous-groupe normal','resultat','s')
text(ax,22.5,38,r'$x^4$','sujet','l'); text(ax,65.5,38,r'$x^4$','sujet','l')
text(ax,65.5,26,r'$yx^4y^{-1}$','sujet','l')
box(ax,6,19,33,10,'fixe',dash=True,label=r'$yx^4y^{-1}$ oublié',size='s')
text(ax,22.5,8,'quotient : pas un groupe','limite','s'); text(ax,65.5,8,'quotient : un groupe','resultat','s')
save(fig,'49-076')
