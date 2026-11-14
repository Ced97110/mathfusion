import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(74)
O=(44,38); r=28
th=[i/120*2*math.pi for i in range(121)]
line(ax,[(O[0]+r*math.cos(t),O[1]+r*math.sin(t)) for t in th],'fixe')
line(ax,[(O[0]-r-3,O[1]),(O[0]+r+3,O[1])],'fixe',lw=0.7)
line(ax,[(O[0],O[1]-r-3),(O[0],O[1]+r+3)],'fixe',lw=0.7)
def pt(d,k=r): t=math.radians(d); return (O[0]+k*math.cos(t),O[1]+k*math.sin(t))
P=pt(120);Q=pt(300)
line(ax,[O,P],'sujet',lw=1.4); line(ax,[O,Q],'autre',lw=1.4)
line(ax,[P,(P[0],O[1])],'resultat',lw=1.8); line(ax,[Q,(Q[0],O[1])],'autre',lw=1.8,dash=True)
arrow(ax,pt(2,8),pt(118,8),'varie',curve=0.3)
text(ax,O[0]+13,O[1]+7.5,'120°','varie','s')
disc(ax,P[0],P[1],1.3,'sujet'); disc(ax,Q[0],Q[1],1.3,'autre')
text(ax,P[0]-3,P[1]+4,'P','sujet','m'); text(ax,Q[0]+3,Q[1]-3.5,'Q : 300°','autre','s',ha='left')
text(ax,44,5,'sans triangle : on lit la hauteur','encre','s')
save(fig,'26-047')
