import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
lab=['e','a','a²','a³','a⁴']
box(ax,5,16,78,22,'sujet',fill=True,dash=True)
for i,l in enumerate(lab): disc(ax,16+i*14,27,4.8,'sujet',label=l)
text(ax,44,44,'puissances de a','sujet','m')
brace(ax,5,83,16,'resultat','5 éléments : divise 5, plus de 1')
text(ax,44,4,'tout le groupe : ≅ ℤ/5','resultat','m')
save(fig,'45-253')
