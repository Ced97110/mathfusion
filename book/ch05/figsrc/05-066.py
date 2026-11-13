import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
f=numberline(ax,8,80,14,0,9,1,arrow_right=False)
data=[(2,'1 premier : au moins 2',48),(4,'2 premiers : au moins 4',36),(8,'3 premiers : au moins 8',24)]
for v,lab,y in data:
    text(ax,20,y+4,lab,'sujet','s',ha='left')
    line(ax,[(f(v),y),(f(9),y)],'sujet',lw=2.0)
    disc(ax,f(v),y,1.6,'sujet')
line(ax,[(f(1),16),(f(1),58)],'limite',dash=True)
disc(ax,f(1),14,1.8,'limite')
text(ax,f(1)+2,60,'1 : aucun produit','limite','s',ha='left')
text(ax,44,2,'les produits valent 2 ou plus','sujet','s')
save(fig,'05-066')
