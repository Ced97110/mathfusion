import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(50)
text(ax,44,45,'2/5 + 1/5 = 3/5','encre','l')
C=8
row(ax,10,22,C,9,['sujet']*2); row(ax,34,22,C,9,['autre']); row(ax,58,22,C,9,['resultat']*3)
text(ax,26,26.5,'+','encre','l'); text(ax,50,26.5,'=','encre','l')
text(ax,18,15,'2 cinquièmes','sujet','s'); text(ax,38,8,'1 cinquième','autre','s'); text(ax,70,15,'3 cinquièmes','resultat','s')
save(fig,'07-023')
