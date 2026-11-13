import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
f=numberline(ax,10,70,18,12,18,1)
text(ax,44,50,r'signe de $2n-30$','encre','s')
for v,r,l in [(14,'sujet','−2'),(15,'resultat','0'),(16,'varie','+2')]:
    box(ax,f(v)-4.5,28,9,8,r,label=l); line(ax,[(f(v),18),(f(v),28)],r,dash=True)
text(ax,f(15),41,r'seuil $n=15$','resultat','s')
text(ax,f(13.5),9,'1re moins chère','sujet','s'); text(ax,f(16.5),9,'2e moins chère','autre','s')
save(fig,'15-112')
