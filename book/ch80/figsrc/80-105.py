import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,3,18,34,36,'sujet',label=None,dash=True); box(ax,51,18,34,36,'resultat',label=None,dash=True)
text(ax,20,58,r'$U$ : tout l’ensemble','sujet','s'); text(ax,68,58,r'$\eta(U)$ : tout l’ensemble','resultat','s')
for i,(a,b) in enumerate([(r'$(1+i,\,1+i)$',r'$(1-i,\,1-i)$'),(r'$(2,\,2)$',r'$(2,\,2)$'),(r'$(3i,\,3i)$',r'$(-3i,\,-3i)$')]):
    y=46-i*11
    text(ax,20,y,a,'sujet','s'); text(ax,68,y,b,'resultat','s'); arrow(ax,(36,y),(52,y),'varie')
text(ax,44,10,r'$\eta$ appliquée à chaque vecteur','varie','s')
save(fig,'80-105')
