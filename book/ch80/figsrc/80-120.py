import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,3,40,38,16,'sujet',label=None); box(ax,47,40,38,16,'autre',label=None)
text(ax,22,51,'identité','sujet','s'); text(ax,22,44,r'$v\mapsto v$','sujet','s')
text(ax,66,51,'double','autre','s'); text(ax,66,44,r'$v\mapsto 2v$','autre','s')
arrow(ax,(22,40),(38,26),'resultat'); arrow(ax,(66,40),(50,26),'resultat')
box(ax,10,10,68,16,'resultat',label=None)
text(ax,44,20,'chaque sous-espace reste en place','resultat','s'); text(ax,44,14,'un seul automorphisme du treillis','resultat','s')
save(fig,'80-120')
