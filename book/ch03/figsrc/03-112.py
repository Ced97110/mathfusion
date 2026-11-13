import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,3,64,'Avant : lu dans un produit','encre','s',ha='left')
box(ax,8,50,8,8,'autre',label='3',size='l',r=0.8)
text(ax,20,54,'×','encre','l')
box(ax,24,50,8,8,'autre',label='5',size='l')
text(ax,54,54,'facteurs : 3 et 5','autre','s')
line(ax,[(3,46),(85,46)],'fixe',dash=True)
text(ax,3,42,'Après : 18 ÷ 6, reste 0','encre','s',ha='left')
for c in range(6):
    for r in range(3):
        box(ax,4+4*c,18+4*r,4,4,'fixe',r=0.3,lw=0.5)
brace(ax,4,28,31,'sujet',label='6',down=False,size='m')
text(ax,37,24,'3 rangées','encre','s')
box(ax,4,8,24,6,'resultat',fill=False,dash=True,label='reste : 0',size='s')
arrow(ax,(45,24),(52,24),'varie')
text(ax,69,28,'18 = 6 × 3','encre','l')
box(ax,53,14,32,8,'sujet',label='6 : facteur de 18',size='s')
save(fig,'03-112')
