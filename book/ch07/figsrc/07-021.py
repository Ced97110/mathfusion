import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(70)
row(ax,14,44,15,9,['sujet']*4)
text(ax,44,63,r'$d=4$ : 3/4 existe','resultat','m')
brace(ax,14,74,44,'sujet',r'$d=4$ parts')
ax.add_patch(Rectangle((14,8),60,9,ec=COL['limite'],fc=FILL['limite'],lw=0.8,ls='--',zorder=2))
line(ax,[(14,8),(74,17)],'limite'); line(ax,[(14,17),(74,8)],'limite')
text(ax,44,24,r'$d=0$ : 3/0 n’existe pas','limite','m')
text(ax,44,3.5,'aucune coupure, aucune part','limite','s')
save(fig,'07-021')
