import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,2,32,30,24,'sujet'); text(ax,17,51,r'$R$','sujet','l',weight='bold'); text(ax,17,40,r'$AB$','sujet','xl')
box(ax,56,32,30,24,'autre'); text(ax,71,51,r'$R^{(0)}$','autre','l',weight='bold'); text(ax,71,40,r'$AB$','autre','xl')
arrow(ax,(34,44),(54,44),'varie'); text(ax,44,50,'identité','varie','s')
text(ax,17,27,'ordre : A puis B','sujet','s'); text(ax,71,27,'ordre : B puis A','autre','s')
text(ax,44,20,r"$R^{(0)}$ : mêmes matrices, produit à l'envers",'encre','s')
box(ax,4,3,80,12,'resultat',label=r'image de $AB$ = $AB$ = $B\times A$ dans $R^{(0)}$',size='s')
save(fig,'52-296')
