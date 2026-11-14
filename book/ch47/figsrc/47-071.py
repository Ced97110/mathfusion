import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
xs=[22+i*14 for i in range(4)]
text(ax,6,76,r'$H$','sujet','l'); text(ax,6,44,r'$gH$','resultat','m')
for x,h,c in zip(xs,[0,3,6,9],[7,10,1,4]):
    box(ax,x-6,72,12,8,'sujet',label=str(h),r=0.5); box(ax,x-6,40,12,8,'resultat',label=str(c),r=0.5)
    arrow(ax,(x-2,72),(x-2,48.5),'varie'); arrow(ax,(x+2,48.5),(x+2,72),'resultat')
text(ax,72,64,r'$h\mapsto gh$','varie','s',ha='left')
text(ax,72,56,r'$y\mapsto g^{-1}y$','resultat','s',ha='left')
for x in [24,44,64]:
    box(ax,x-6,12,12,7,'limite',label=str(int((x-24)/20*4)),r=0.5)
    arrow(ax,(x,11.5),(44,3.2),'limite',lw=0.8)
disc(ax,44,2,1.2,'limite')
text(ax,86,4,'×3 : on ne\nrevient pas','limite','s',ha='right')
save(fig,'47-071')
