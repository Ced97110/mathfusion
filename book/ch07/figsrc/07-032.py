import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(60)
text(ax,44,54,'1/2 + 3/4 : seconde fraction','encre','s')
text(ax,14,41,r'$c$','sujet','xl'); line(ax,[(8,35),(20,35)],'encre',lw=1.2); text(ax,14,29,r'$d$','fixe','xl')
row(ax,30,26,12,9,['sujet']*3+[None])
brace(ax,30,66,35,'sujet',r'$c=3$ parts prises',down=False)
brace(ax,30,78,26,'fixe',r'$d=4$ parts de l’unité')
save(fig,'07-032')
