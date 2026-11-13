import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(108)
text(ax,44,103,'parts de tailles différentes','encre','s')
row(ax,14,88,24,7,['sujet',None]); text(ax,6,91.5,'1/2','sujet','m')
row(ax,14,79,16,7,['autre',None,None]); text(ax,6,82.5,'1/3','autre','m')
arrow(ax,(68,77),(68,68),'varie'); text(ax,71,72.5,'recouper','varie','s',ha='left')
row(ax,14,57,8,7,['sujet']*3+[None]*3); text(ax,6,60.5,'3/6','sujet','m')
row(ax,14,48,8,7,['autre']*2+[None]*4); text(ax,6,51.5,'2/6','autre','m')
text(ax,76,56,r'$D=6$','encre','m')
arrow(ax,(68,46),(68,37),'varie'); text(ax,71,41.5,'additionner','varie','s',ha='left')
row(ax,14,25,8,7,['resultat']*5+[None]); text(ax,6,28.5,'5/6','resultat','m')
text(ax,44,15,'même taille : on additionne','encre','s')
save(fig,'07-027')
