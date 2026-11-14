import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
O=(12,8); s=7
P=lambda x,y:(O[0]+s*x,O[1]+s*y)
poly(ax,[P(0,0),P(4,0),P(3,2),P(0,5)],'resultat')
arrow(ax,P(0,0),P(5,0),'fixe',lw=0.6); arrow(ax,P(0,0),P(0,6),'fixe',lw=0.6)
text(ax,P(5,0)[0]+1,P(5,0)[1]-3.5,'cafés','fixe','s'); text(ax,P(0,6)[0]+6,P(0,6)[1]+1,'croissants','fixe','s')
pts=[(x,y) for x in range(6) for y in range(6) if x+y<=5 and 2*x+y<=8]
assert len(pts)==19
hl={(1,1):'5 €',(3,1):'11 €',(3,2):'13 €'}
for p in pts:
    if p in hl: disc(ax,*P(*p),1.3,'varie')
    else: disc(ax,*P(*p),0.8,'sujet')
for p,t in hl.items():
    text(ax,P(*p)[0]+3.5,P(*p)[1]+2.5,t,'varie','s',ha='left')
text(ax,69,52,'19 commandes','sujet','m')
text(ax,69,45,'coût : $3x + 2y$','varie','s')
box(ax,52,14,34,14,'resultat',label='lequel est\nle meilleur ?',size='s')
save(fig,'24-079')
