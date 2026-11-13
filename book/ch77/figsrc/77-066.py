import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(62)
text(ax,16,56,'$1+3\\sqrt{2}$','sujet','m')
mat(ax,3,28,13,10,[['1','6'],['3','1']],[['sujet','varie'],['varie','sujet']])
text(ax,16,22,'tableau de $u$','fixe','s')
arrow(ax,(32,33),(40,33),'fixe')
box(ax,41,28,45,10,'fixe',label='$1\\times1-6\\times3$',size='m')
arrow(ax,(63,28),(63,22),'fixe')
box(ax,41,12,45,10,'resultat',label='$-17\\neq0$',size='m')
arrow(ax,(63,12),(63,8),'resultat')
text(ax,63,4,'l’inverse existe','resultat','s')
save(fig,'77-066')
