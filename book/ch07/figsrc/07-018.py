import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(64)
text(ax,44,59,'on coupe l’unité (le mur)','encre','m')
row(ax,14,36,12,9,['sujet']*5)
brace(ax,14,74,36,'sujet',r'$d=5$ parts égales')
row(ax,14,10,7.5,9,['sujet']*8)
brace(ax,14,74,10,'sujet',r'$d=8$ parts égales')
save(fig,'07-018')
