import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(76)
text(ax,44,71,'7/8 − 3/8','encre','l')
row(ax,14,48,7.5,9,['resultat']*4+['varie']*3+[None])
brace(ax,14,44,48,'resultat',r'$a-b=4$ restent')
brace(ax,44,66.5,57,'varie',r'$b=3$ retirées',down=False)
text(ax,44,34,'5/6 − 1/6','encre','l')
row(ax,14,10,10,9,['resultat']*4+['varie']+[None])
brace(ax,14,54,10,'resultat',r'$a-b=4$ restent')
brace(ax,54,64,19,'varie',r'$b=1$',down=False)
save(fig,'07-020')
