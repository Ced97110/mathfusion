import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
s=0.018; w,h=1000*s,800*s
x0,y0=5,27
poly(ax,[(x0,y0),(x0+w,y0),(x0+w,y0+h),(x0,y0+h)],'sujet')
text(ax,x0+w/2,y0+h/2,'800 000 px','sujet','s')
text(ax,x0+w/2,y0+h+4,'photo','sujet','s')
x1=46
poly(ax,[(x1,46),(x1+2*w,46),(x1+2*w,46+h),(x1,46+h)],'limite')
text(ax,x1+w,46+h/2,'1 600 000 px','limite','s')
text(ax,x1+w,46+h+4,'dilatation : aire × 2','limite','s')
sh=7.2
poly(ax,[(x1,6),(x1+w,6),(x1+w+sh,6+h),(x1+sh,6+h)],'resultat')
text(ax,x1+(w+sh)/2,6+h/2,'800 000 px','resultat','s')
text(ax,x1+(w+sh)/2,6+h+4,'cisaillement : aire gardée','resultat','s')
arrow(ax,(x0+w+1.5,y0+h*0.8),(x1-1.5,46+h/2),'limite')
arrow(ax,(x0+w+1.5,y0+h*0.2),(x1-1.5,6+h/2),'resultat')
save(fig,'73-008')
