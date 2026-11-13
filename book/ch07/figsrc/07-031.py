import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(66)
text(ax,22,58,'1/2 + 1/3','encre','m'); text(ax,66,58,'2/5 + 1/5','encre','m')
row(ax,4,38,18,8,['sujet',None]); row(ax,4,28,12,8,['autre',None,None])
row(ax,48,38,7.2,8,['sujet']*2+[None]*3); row(ax,48,28,7.2,8,['autre']+[None]*4)
text(ax,13,20,r'$b=2$','sujet','m'); text(ax,31,20,r'$d=3$','autre','m')
text(ax,57,20,r'$b=5$','sujet','m'); text(ax,75,20,r'$d=5$','autre','m')
text(ax,22,8,r'$b\neq d$ : vrai','resultat','m'); text(ax,66,8,r'$b\neq d$ : faux','limite','m')
save(fig,'07-031')
