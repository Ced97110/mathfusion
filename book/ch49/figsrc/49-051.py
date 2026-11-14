import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for i,(s,r) in enumerate([('x','sujet'),(r'$x^{-1}$','autre'),('x','sujet')]): box(ax,29+10*i,48,9,9,r,label=s)
arrow(ax,(34,47),(20,34),'varie'); arrow(ax,(54,47),(68,34),'varie')
box(ax,14,22,12,11,'resultat',label='x'); box(ax,62,22,12,11,'resultat',label='x')
text(ax,44,27.5,'=','resultat','l')
text(ax,20,16,'efface les 2 premières','varie','s'); text(ax,68,16,'efface les 2 dernières','varie','s')
text(ax,44,7,'même mot réduit : x','resultat','m')
save(fig,'49-051')
