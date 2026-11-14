import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
for y,s in [(70,'départ'),(43,'étape clé'),(16,'arrivée')]: text(ax,10,y,s,'encre','s')
box(ax,22,58,64,20,'sujet',fill=False)
for x,v in zip([33,47,61,75],['3','4','12','12']): pass
text(ax,54,72,r'$k=12=3\times4$','sujet','l')
text(ax,54,63,r'$k$ composé, $l=3$, $m=4$','sujet','s')
box(ax,22,36,64,14,'varie',label=r'$\bar3\times\bar4=\bar{12}=\bar0$',size='l')
box(ax,22,8,64,16,'resultat',label='\n'.join([r'$\bar3\neq\bar0$ et $\bar4\neq\bar0$','produit nul']),size='m')
arrow(ax,(54,57),(54,51),'varie'); arrow(ax,(54,35),(54,25),'varie')
save(fig,'52-083')
