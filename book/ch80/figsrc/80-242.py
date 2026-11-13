import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lat(ax, ox, oy, dy, roles=None, hot=(), r=3.6):
    roles = roles or {}
    P = {1:(ox,oy),2:(ox-22,oy+dy),3:(ox,oy+dy),5:(ox+22,oy+dy),6:(ox-22,oy+2*dy),10:(ox,oy+2*dy),15:(ox+22,oy+2*dy),30:(ox,oy+3*dy)}
    E = [(1,2),(1,3),(1,5),(2,6),(2,10),(3,6),(3,15),(5,10),(5,15),(6,30),(10,30),(15,30)]
    for a,b in E: line(ax,[P[a],P[b]],'fixe')
    for a,b,rl in hot: line(ax,[P[a],P[b]],rl,lw=1.8)
    for n,p in P.items(): disc(ax,p[0],p[1],r,roles.get(n,'fixe'),label=str(n),size='s')
    return P
fig,ax=canvas(104)
text(ax,44,99,r'$b$ = sup des atomes sous $b$','sujet','m')
P=lat(ax,44,28,19,{2:'resultat',3:'resultat',5:'varie',6:'sujet'},[(2,6,'resultat'),(3,6,'resultat')])
text(ax,86,P[5][1],'atomes','fixe','s',ha='right',va='bottom')
text(ax,44,16,'atomes sous 6 : 2 et 3 → PPCM = 6','resultat','s')
text(ax,44,7,'avec 5 en plus : PPCM = 30, pas 6','varie','s')
[l.set_zorder(1.5) for l in ax.lines]
save(fig,'80-242')
