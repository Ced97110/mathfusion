import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(58)
box(ax,2,44,40,10,'sujet',label='$\\sqrt{2}\\times1=\\sqrt{2}$',size='s')
box(ax,46,44,40,10,'varie',label='$\\sqrt{2}\\times\\sqrt{2}=2$',size='s')
mat(ax,25,10,19,11,[['0','2'],['1','0']],[['sujet','varie'],['sujet','varie']])
arrow(ax,(22,44),(33,33),'sujet'); arrow(ax,(66,44),(54,33),'varie')
text(ax,34,6,'colonne 1','sujet','s'); text(ax,53,6,'colonne 2','varie','s')
save(fig,'77-079')
