import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,30,62,r'$m$','sujet','l',weight='bold')
text(ax,36.5,62,r'− $s$ = $d$','fixe','l',ha='left')
text(ax,30,49,'9','sujet','l',weight='bold'); text(ax,36.5,49,'− 4 = 5','fixe','l',ha='left')
text(ax,30,37,'52','sujet','l',weight='bold'); text(ax,36.5,37,'− 27 = 25','fixe','l',ha='left')
box(ax,24,31,11,37,'sujet',fill=False,dash=True)
numberline(ax,6,78,14,0,60,10,labels=False,role='fixe')
f=lambda v:6+1.2*v
for v in (9,52):
    disc(ax,f(v),14,1.2,'sujet'); text(ax,f(v),10.5,str(v),'sujet','s')
arrow(ax,(f(9),18),(12,18),'varie'); arrow(ax,(f(52),18),(36,18),'varie')
save(fig,'02-038')
