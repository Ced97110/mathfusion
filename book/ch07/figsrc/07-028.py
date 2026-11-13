import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(58)
text(ax,44,53,'multiples communs de 2 et 3','encre','s')
f=numberline(ax,22,76,22,0,18,1,labels=False)
for v in range(1,19):
    if v%2==0: ax.add_patch(Circle((f(v),30),1.3,ec=COL['sujet'],fc=FILL['sujet'],lw=0.8,zorder=3))
    if v%3==0: ax.add_patch(Circle((f(v),14),1.3,ec=COL['autre'],fc=FILL['autre'],lw=0.8,zorder=3))
for v in (6,12,18):
    line(ax,[(f(v),14),(f(v),30)],'resultat',dash=True)
    text(ax,f(v),37,str(v),'resultat','m')
text(ax,2,30,'multiples de 2','sujet','s',ha='left'); text(ax,2,14,'multiples de 3','autre','s',ha='left')
text(ax,f(6)+12,45,'le plus petit : 6','resultat','s')
save(fig,'07-028')
