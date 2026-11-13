import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(78)
O=(12,8); r=60; c,s_=0.8,0.6
P=(O[0]+r*c,O[1]+r*s_); F=(P[0],O[1])
th=[i/60*math.pi/2 for i in range(61)]
line(ax,[(O[0]+r*math.cos(t),O[1]+r*math.sin(t)) for t in th],'fixe')
arrow(ax,(O[0]-3,O[1]),(O[0]+r+4,O[1]),'fixe',lw=0.8)
arrow(ax,(O[0],O[1]-3),(O[0],O[1]+r+4),'fixe',lw=0.8)
line(ax,[O,P],'sujet',lw=1.4)
line(ax,[O,F],'resultat',lw=1.8)
line(ax,[F,P],'autre',lw=1.8)
a=math.atan2(s_,c)
line(ax,[(O[0]+9*math.cos(t),O[1]+9*math.sin(t)) for t in [a*i/20 for i in range(21)]],'varie')
text(ax,O[0]+13,O[1]+3.4,r'$\theta$','varie','m')
disc(ax,P[0],P[1],1.3,'sujet')
text(ax,P[0]-9,P[1]+4,r'$P(0{,}8\,;\,0{,}6)$','sujet','s')
text(ax,O[0]+19,O[1]+25,'1','sujet','s')
text(ax,O[0]+r*c/2,O[1]-3.3,r'$\cos\theta=x=0{,}8$','resultat','s')
text(ax,P[0]+11,O[1]+r*s_/2,r'$\sin\theta=y$'+'\n0,6','autre','s')
save(fig,'26-045')
