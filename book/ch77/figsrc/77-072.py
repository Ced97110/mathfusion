import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(60)
text(ax,22,54,'$\\lambda-$ tableau de $z$','fixe','s')
mat(ax,3,26,19,11,[['$\\lambda-3$','4'],['−4','$\\lambda-3$']],[['sujet','varie'],['varie','sujet']],'s')
arrow(ax,(44,31),(50,31),'fixe')
box(ax,51,36,35,9,'sujet',label='$(\\lambda-3)^2$',size='m')
box(ax,51,23,35,9,'varie',label='$+\\ 16$',size='m')
arrow(ax,(68,23),(68,17),'resultat')
box(ax,51,6,35,10,'resultat',label='$\\lambda^2-6\\lambda+25$',size='s')
text(ax,22,18,'déterminant','fixe','s')
save(fig,'77-072')
