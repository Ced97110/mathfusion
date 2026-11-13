import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
u=5.5; cx,cy=44,34
pt=lambda x,y:(cx+x*u,cy+y*u)
t=[math.radians(d) for d in range(0,361,4)]
line(ax,[(cx+5*u*math.cos(a),cy+5*u*math.sin(a)) for a in t],'fixe',lw=0.6,dash=True)
line(ax,[(cx,cy-5*u-2),(cx,cy+5*u+2)],'fixe',lw=0.6,dash=True)
arrow(ax,(cx-5*u-4,cy),(cx+5*u+6,cy),'fixe',lw=0.6)
r=12
a0,a1=math.radians(56),math.radians(140)
line(ax,[(cx+r*math.cos(a0+(a1-a0)*i/20),cy+r*math.sin(a0+(a1-a0)*i/20)) for i in range(21)],'varie',lw=1.2)
q=a1-0.08
arrow(ax,(cx+r*math.cos(q),cy+r*math.sin(q)),(cx+r*math.cos(a1),cy+r*math.sin(a1)),'varie',lw=1.2)
arrow(ax,(pt(3,4)[0]-1.5,pt(3,4)[1]),(pt(-3,4)[0]+1.5,pt(-3,4)[1]),'autre',lw=1.1)
disc(ax,*pt(3,4),1.3,'sujet'); disc(ax,*pt(-4,3),1.3,'resultat'); disc(ax,*pt(-3,4),1.3,'autre')
text(ax,pt(3,4)[0]+3,pt(3,4)[1],'(3, 4)','sujet','s',ha='left')
text(ax,pt(-4,3)[0]-3,pt(-4,3)[1],'(−4, 3)','resultat','s',ha='right')
text(ax,pt(-3,4)[0],pt(-3,4)[1]+4,'(−3, 4)','autre','s')
text(ax,33,38,'quart de tour','varie','s')
text(ax,54,52.5,'miroir','autre','s')
text(ax,44,3,'tous à la distance 5','resultat','s')
save(fig,'73-010')
