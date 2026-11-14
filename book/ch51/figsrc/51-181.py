import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,2,64,84,14,'sujet',label=r'départ : $\mathbb{H}$ en tableaux complexes')
arrow(ax,(44,64),(44,59.5),'fixe')
box(ax,2,31,84,28,'varie')
text(ax,44,54.5,'étape clé : trois contrôles','varie','m',weight='bold')
text(ax,44,49.5,r'$\mathbb{H}$ est un sous-anneau de $M_2(\mathbb{C})$','varie','s')
for x,l in zip((5,32.5,60),(r'① $1\in\mathbb{H}$',r'② différence $\in\mathbb{H}$',r'③ produit $\in\mathbb{H}$')):
    box(ax,x,34,25,11,'encre',label=l,size='s')
arrow(ax,(44,31),(44,26.5),'fixe')
text(ax,47,28.7,r'héritées de $M_2(\mathbb{C})$','fixe','s',ha='left')
box(ax,2,12,84,14,'resultat',label='arrivée : huit règles héritées')
text(ax,44,6,'3 contrôles, pas 8 règles à vérifier','encre','s')
save(fig,'51-181')
