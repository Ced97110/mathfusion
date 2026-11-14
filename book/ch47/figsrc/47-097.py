import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,22,58,'modulo 12','encre','m'); text(ax,68,58,'différence','encre','m')
for y,l,d,r in [(42,'26 ≡ 2','24','sujet'),(26,'27 ≡ 3','24','autre'),(6,'53 ≡ 5','48','resultat')]:
    box(ax,4,y,36,10,r,label=l,size='l'); arrow(ax,(41,y+5),(52,y+5),r); box(ax,53,y,30,10,r,label=d,size='l')
for x in (22,68):
    text(ax,x,39,'+','varie','l'); text(ax,x,21,'=','varie','l')
save(fig,'47-097')
