import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
specs=[(2,'sujet',r'$Q(u\times v)$','46',None),(32,'varie',r'$(u\cdot v)^{2}$','4',r'$2^{2}$, car $u\cdot v=2$'),(62,'resultat',r'$Q(u)\,Q(v)$','50',r'$5\times10$')]
for x,r,n,v,sub in specs:
    text(ax,x+12,50,n,r,'m')
    box(ax,x,28,24,14,r,label=v,size='xl')
    if sub: text(ax,x+12,20,sub,r,'s')
text(ax,28.0,35,'+','encre','xl'); text(ax,58,35,'=','encre','xl')
save(fig,'78-124')
