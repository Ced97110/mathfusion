import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
xs=[24+i*18 for i in range(4)]
text(ax,6,50,r'$H$','sujet','l'); text(ax,6,16,r'$gH$','resultat','m')
for x,h,c in zip(xs,[0,3,6,9],[7,10,1,4]):
    box(ax,x-6,46,12,8,'sujet',label=str(h),r=0.5); box(ax,x-6,12,12,8,'resultat',label=str(c),r=0.5)
    arrow(ax,(x,46),(x,20.5),'varie',lw=1.0)
text(ax,15,33,r'$+\,7$','varie','m')
brace(ax,xs[0]-6,xs[-1]+6,57,'sujet',label=r'$|H|=4$',down=False)
brace(ax,xs[0]-6,xs[-1]+6,10,'resultat',label=r'$|gH|=4$')
save(fig,'47-070')
