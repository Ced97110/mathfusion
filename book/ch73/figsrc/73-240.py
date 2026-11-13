import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
o=(10,8); u=8.0
P=lambda x,y:(o[0]+x*u,o[1]+y*u)
arrow(ax,P(-0.5,0),P(4,0),'fixe',lw=0.6); arrow(ax,P(0,-0.5),P(0,3.8),'fixe',lw=0.6)
arrow(ax,P(1,0),P(3,0),'sujet',lw=1.3); arrow(ax,P(3,0),P(0,3),'sujet',lw=1.3,curve=0.35)
arrow(ax,P(1,0),P(0,1),'autre',lw=1.3,curve=-0.35); arrow(ax,P(0,1),P(2,1),'autre',lw=1.3)
for p in (P(3,0),P(0,3)): disc(ax,*p,1.0,'sujet')
for p in (P(0,1),P(2,1)): disc(ax,*p,1.0,'autre')
disc(ax,*P(1,0),1.3,'fixe')
text(ax,P(1,0)[0],P(1,0)[1]-4,r'$P$','fixe','s')
text(ax,P(3,0)[0]+3,P(3,0)[1]+3.5,r'$(3,0)$','sujet','s',ha='left')
text(ax,P(0,3)[0]+3,P(0,3)[1]+1,r'$(0,3)$','sujet','s',ha='left')
text(ax,P(2,1)[0]+3,P(2,1)[1]+1,r'$(2,1)$','autre','s',ha='left')
text(ax,P(0,1)[0]-3,P(0,1)[1]+3.5,r'$(0,1)$','autre','s',ha='left') if False else None
text(ax,66,38,r'$rt$ : $(0,3)$','sujet','m'); text(ax,66,28,r'$tr$ : $(2,1)$','autre','m')
text(ax,66,18,r'$rt\neq tr$','limite','m')
save(fig,'73-240')
