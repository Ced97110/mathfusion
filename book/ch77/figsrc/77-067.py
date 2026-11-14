import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(56)
box(ax,2,38,40,10,'varie',label='$z\\times i=-4+3i$',size='s')
box(ax,2,14,40,10,'sujet',label='$z\\times1=3+4i$',size='s')
mat(ax,50,24,18,10,[['3','−4'],['4','3']],[['sujet','varie'],['sujet','varie']])
arrow(ax,(42,47),(74,45.4),'varie')
arrow(ax,(42,19),(59,23.5),'sujet')
text(ax,22,31,'coordonnées en colonnes','fixe','s')
save(fig,'77-067')
