import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66); y=34
f=numberline(ax,12,76,y,-4,4,labels=False,arrow_right=False)
line(ax,[(f(0),y-9),(f(0),y+24)],'fixe',dash=True)
text(ax,f(0),y-12,'miroir en 0','fixe','s')
for v in (-3,-1,0,1,3): text(ax,f(v),y-4,f'{v}'.replace('-','−'),'fixe','s')
for v,r,l in ((1,'sujet','A'),(3,'autre','B'),(-1,'sujet',"A'"),(-3,'autre',"B'")):
    disc(ax,f(v),y,1.6,r); text(ax,f(v),y+4.2,f'${l}$' if "'" not in l else f"${l[0]}'$",r,'s')
arrow(ax,(f(1),y+7),(f(-1),y+7),'varie',curve=0.45)
arrow(ax,(f(3),y+7),(f(-3),y+7),'varie',curve=0.3)
text(ax,44,y-21,r'$1<3$  devient  $-1>-3$','resultat','m')
save(fig,'17-065')
