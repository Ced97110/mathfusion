import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
X=lambda v:10+v*1.15
numberline(ax,10,79,6,0,60,step=5,every=12,arrow_right=False)
rows=[(15,'sujet',48,'multiples de 15 : 4 éléments'),(20,'autre',34,'multiples de 20 : 3 éléments'),(12,'varie',20,'multiples de 12 : 5 éléments')]
for st,r,y,t in rows:
    line(ax,[(X(0),y),(X(60),y)],'fixe',lw=0.5)
    for v in range(0,60,st): disc(ax,X(v),y,2.3,r)
    text(ax,10,y+6,t,r,'s',ha='left')
text(ax,44,62,'4 × 3 × 5 = 60','resultat','m')
save(fig,'45-254')
