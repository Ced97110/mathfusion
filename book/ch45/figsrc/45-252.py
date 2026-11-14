import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for i in range(4):
    disc(ax,10,52-i*13,4,'sujet' if i!=1 else 'limite',label=str(i))
    arrow(ax,(14.6,52-i*13),(45.4,26+ (0)),'limite' if i==1 else 'fixe',lw=0.9)
disc(ax,50,26,4,'autre',label='0')
text(ax,67,44,'0 = 0 + 0 :','resultat','s'); text(ax,67,40,'somme gardée','resultat','s')
text(ax,67,32,'0 = 0 × 0 :','resultat','s'); text(ax,67,28,'produit gardé','resultat','s')
text(ax,67,16,'mais 1 → 0, pas 1','limite','s')
save(fig,'45-252')
