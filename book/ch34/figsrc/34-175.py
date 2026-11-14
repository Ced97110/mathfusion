import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(70)
O=(10,8); R=50; d=lambda a,r:(O[0]+r*math.cos(math.radians(a)),O[1]+r*math.sin(math.radians(a)))
arc=lambda a0,a1,r:[d(a,r) for a in np.linspace(a0,a1,60)]
line(ax,[O,(O[0]+60,O[1])],'fixe'); line(ax,[O,(O[0],O[1]+55)],'fixe')
line(ax,arc(0,90,R),'fixe',dash=True,lw=0.7)
for a,role,t in [(30,'sujet','premier : 30°'),(45,'autre','second : 45°'),(75,'resultat','produit : 75°')]:
    arrow(ax,O,d(a,R),role,lw=1.4); text(ax,d(a,R)[0]+2,d(a,R)[1]+(2.2 if a==75 else 0),t,role,'s',ha='left')
line(ax,arc(30,75,34),'autre',lw=1.2); text(ax,d(60,41)[0],d(60,41)[1],'+ 45°','autre','s')
p=d(75,R); line(ax,[p,(p[0],O[1])],'resultat',dash=True,lw=0.9); line(ax,[p,(O[0],p[1])],'resultat',dash=True,lw=0.9)
text(ax,p[0],O[1]-3.2,'0,2588','resultat','s'); text(ax,O[0]+7.5,p[1]+3,'0,9659','resultat','s')
save(fig,'34-175')
