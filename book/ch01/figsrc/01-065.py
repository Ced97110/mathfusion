import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
for x,c,d,n,v,r in [(6,18,'3','centaines','vaut 100','autre'),(32,44,'2','dizaines','vaut 10','sujet'),(58,70,'9','unités','vaut 1','autre')]:
    box(ax,x,45,24,9,r,label=d,size='l')
    text(ax,c,59,n,r,'s'); text(ax,c,40,v,r,'s')
for x0 in [40,46]:
    for k in range(10):
        y=14+2*k
        poly(ax,[(x0,y),(x0+2,y),(x0+2,y+2),(x0,y+2)],'sujet',lw=0.5)
text(ax,44,9,'2 paquets de dix = 20','resultat','m')
save(fig,'01-065')
