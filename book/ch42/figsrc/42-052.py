import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,8,74,12,0,3,labels=False)
poly(ax,[(8,12),(30,12),(30,34),(8,34)],'fixe')
line(ax,[(8,12),(30,34)],'varie')
text(ax,12.5,28.5,'diagonale','varie','s',rot=45)
R=22*math.sqrt(2)
arc=[(8+R*math.cos(math.radians(a)),12+R*math.sin(math.radians(a))) for a in range(45,-1,-3)]
line(ax,arc,'varie',dash=True)
line(ax,[(8,12),(79,12)],'sujet',lw=2.2)
for v,l,r in [(0,'0','fixe'),(0.5,'1/2','sujet'),(1,'1','fixe'),(math.sqrt(2),'√2','resultat'),(2,'2','sujet')]:
    disc(ax,f(v),12,1.9,r)
    text(ax,f(v),6.5,l,r,'s')
text(ax,62,30,'ℝ = tous les points','sujet','l')
save(fig,'42-052')
