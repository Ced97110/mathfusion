import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[20+i*18 for i in range(4)]
Hs=[0,3,6,9]; C=[4,7,10,1]
text(ax,6,48,r'$H$','fixe','l'); text(ax,6,16,r'$4+H$','sujet','s')
for x,h,c,i in zip(xs,Hs,C,range(4)):
    box(ax,x-6,44,12,8,'varie' if i==0 else 'fixe',label=str(h),r=0.5)
    box(ax,x-6,12,12,8,'resultat' if i==0 else 'sujet',label=str(c),r=0.5)
    arrow(ax,(x,44),(x,20.5),'varie' if i==0 else 'fixe',lw=1.2 if i==0 else 0.8)
text(ax,xs[0],57,'neutre 0','varie','s')
text(ax,(xs[0]+xs[1])/2,32,'0 + 4 = 4','varie','s')
text(ax,48,4,'4 est dans sa propre ligne','resultat','m')
save(fig,'47-066')
