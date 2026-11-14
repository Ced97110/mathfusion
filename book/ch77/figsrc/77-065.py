import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(68)
labs=['$N(u)\\neq 0$','$\\rho(u)$ inversible','$u_L$ bijective','$uv=1$ : $u$ inversible']
for i,l in enumerate(labs):
    y=57-i*15
    box(ax,2,y,38,9,'resultat',label=l,size='s')
    if i<3: arrow(ax,(21,y),(21,y-6),'resultat')
box(ax,48,57,38,9,'limite',label='$N(\\varepsilon)=0$',size='s')
arrow(ax,(67,57),(67,50),'limite')
text(ax,67,47,'$\\rho(\\varepsilon)$','limite','s')
mat(ax,55,28,12,8,[['0','0'],['1','0']],[['limite']*2]*2,'s')
arrow(ax,(67,27),(67,20),'limite')
box(ax,48,10,38,9,'limite',label='aucun inverse',size='s')
text(ax,67,4,'$\\varepsilon\\,\\varepsilon=0$','limite','s')
save(fig,'77-065')
