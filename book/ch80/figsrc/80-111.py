import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,73,'l’alignement est conservé','sujet','m')
pts=[('100','010'),('101','011'),('001','001')]
text(ax,6,56,'avant','sujet','s'); text(ax,6,26,'après','resultat','s')
line(ax,[(12,56),(76,56)],'sujet'); line(ax,[(12,26),(76,26)],'resultat')
for i,(a,b) in enumerate(pts):
    x=24+i*24
    disc(ax,x,56,1.6,'sujet'); text(ax,x,61,a,'sujet','s')
    disc(ax,x,26,1.6,'resultat'); text(ax,x,21,b,'resultat','s')
    arrow(ax,(x,54),(x,28),'varie')
t=text(ax,48,41,'échanger les 2 premiers chiffres','varie','s'); t.set_bbox(dict(fc='white',ec='none',pad=1))
box(ax,6,2,76,12,'resultat',label='vient d’une application linéaire\n(à un automorphisme près)',size='s')
save(fig,'80-111')
