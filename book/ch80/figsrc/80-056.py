import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
ox,oy,s=24,36,13
P=lambda a,b:(ox+a*s,oy+b*s)
line(ax,[P(-1.5,0),P(1.8,0)],'sujet',lw=2.2); line(ax,[P(0,-1.5),P(0,1.8)],'autre',lw=2.2)
disc(ax,*P(1,0),1.3,'sujet'); disc(ax,*P(0,1),1.3,'autre')
disc(ax,*P(1,1),1.6,'limite',fill=False,lw=1.2)
line(ax,[P(1,0),P(1,1)],'fixe',dash=True); line(ax,[P(0,1),P(1,1)],'fixe',dash=True)
text(ax,P(1,1)[0]+3,P(1,1)[1]+4,'(1, 1)','limite','s')
text(ax,P(1,0)[0]+2,P(1,0)[1]-4,'(1, 0)','sujet','s'); text(ax,P(0,1)[0]-7,P(0,1)[1]+3,'(0, 1)','autre','s')
rows=[('1. un vecteur de chaque axe','fixe'),('2. on les additionne','varie'),('3. (1, 1) n’est sur aucun axe','limite')]
for i,(t,r) in enumerate(rows):
    box(ax,50,52-i*17,36,12,r,label=None); text(ax,68,58-i*17,t,r,'s')
arrow(ax,(68,52),(68,47),'fixe'); arrow(ax,(68,35),(68,30),'fixe')
text(ax,44,6,'la réunion n’est pas un sous-espace','limite','s')
save(fig,'80-056')
