import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
o=(10,12); s=15
arrow(ax,o,(o[0]+s,o[1]),'sujet',lw=1.5); arrow(ax,o,(o[0],o[1]+s),'autre',lw=1.5); arrow(ax,o,(o[0]+s,o[1]+s),'varie',lw=1.5)
line(ax,[(o[0]+s,o[1]),(o[0]+s,o[1]+s),(o[0],o[1]+s)],'fixe',dash=True)
text(ax,o[0]+s+3,o[1]-3,r'$e_1$','sujet','m'); text(ax,o[0]-1,o[1]+s+3,r'$e_2$','autre','m'); text(ax,o[0]+s+7,o[1]+s+3,r'$e_1+e_2$','varie','m')
text(ax,24,50,'plan : volume 0','limite','m'); text(ax,24,44,r'$u\wedge v\wedge w=0$','limite','m')
og=(58,10); u=16
cubes(ax,[(0,0,0)],og,u,'resultat')
for (d,r,l) in [((1.3,0,0),'sujet',r'$e_1$'),((0,1.3,0),'autre',r'$e_2$'),((0,0,1.3),'varie',r'$e_3$')]:
    q=iso(*d,origin=og,u=u); arrow(ax,og,q,r,lw=1.3)
    text(ax,q[0]+(4 if d[0] else -4 if d[1] else 3),q[1]+(0 if d[2]==0 else 2),l,r,'m')
text(ax,66,56,'espace : volume 1','resultat','m')
save(fig,'76-135')
