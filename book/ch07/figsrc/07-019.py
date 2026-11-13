import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(80)
text(ax,44,75,'3/5 + 2/5','encre','l')
row(ax,14,50,12,9,['sujet']*3+['autre']*2)
text(ax,32,64,r'$a=3$','sujet','m'); text(ax,62,64,r'$b=2$','autre','m')
brace(ax,14,74,50,'resultat',r'$a+b=5$ parts réunies')
text(ax,44,32,'2/9 + 3/9','encre','l')
row(ax,14,8,60/9,9,['sujet']*2+['autre']*3+[None]*4)
brace(ax,14,14+60*5/9,8,'resultat',r'$a+b=5$ parts')
save(fig,'07-019')
