import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
u=3.0; x0=6
text(ax,x0,69,'23 billes, tas de 5 (bleu)','encre','m',ha='left')
rows=[(46,3,8,False),(29,4,3,False),(12,4,3,True)]
eqs=[r'$23=5\times3+8$',r'$23=5\times4+3$',r'$23=5\times5-2$']
for (y,nf,rem,over),eq in zip(rows,eqs):
    for k in range(nf): box(ax,x0+k*5*u+0.3,y,5*u-0.6,8,'sujet')
    s=x0+nf*5*u
    if not over:
        box(ax,s+0.3,y,rem*u-0.6,8,'varie',label=str(rem),size='s')
    else:
        box(ax,s+0.3,y,3*u-0.6,8,'sujet')
        box(ax,s+3*u+0.3,y,2*u-0.6,8,'limite',label='−2',size='s')
    text(ax,x0,y+11.5,eq,'sujet','m',ha='left')
text(ax,x0+23*u,6,'23','encre','s')
line(ax,[(x0+23*u,9.5),(x0+23*u,58)],'encre',dash=True)
text(ax,x0,2.5,'trois restes : 8, 3, −2','limite','s',ha='left')
save(fig,'05-033')
