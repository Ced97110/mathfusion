import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,22,64,'produit, puis racine','sujet','s'); text(ax,66,64,'racines, puis produit','autre','s')
L=[(r'$9\times 4$','sujet'),('36','sujet'),('6','resultat')]; R=[(r'$\sqrt{9}\times\sqrt{4}$','autre'),(r'$3\times 2$','autre'),('6','resultat')]
for i in range(3):
    y=44-i*20
    box(ax,5,y,34,11,role=L[i][1],label=L[i][0]); box(ax,49,y,34,11,role=R[i][1],label=R[i][0])
for i,(a,b) in enumerate((('produit','racine'),('racines','produit'))):
    y=44-i*20
    for c,t in ((22,(a,b)[0] if False else None),):
        pass
arrow(ax,(22,44),(22,36),'varie'); arrow(ax,(22,24),(22,16),'varie')
arrow(ax,(66,44),(66,36),'varie'); arrow(ax,(66,24),(66,16),'varie')
text(ax,24.5,40,'produit','varie','s',ha='left'); text(ax,24.5,20,'racine','varie','s',ha='left')
text(ax,68.5,40,'racines','varie','s',ha='left'); text(ax,68.5,20,'produit','varie','s',ha='left')
text(ax,44,5.5,'=','resultat','l')
save(fig,'22-058')
