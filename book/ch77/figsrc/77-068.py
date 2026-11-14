import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(52)
for k,(x,top,v,name) in enumerate([(3,'4','4','$3+4i$'),(49,'1','1','$3+i$')]):
    text(ax,x+17,46,name,'sujet','m')
    mat(ax,x,22,17,10,[['3','−'+top],[v,'3']],[['resultat','fixe'],['fixe','resultat']])
    text(ax,x+17,15,'$3+3=6$','resultat','m')
text(ax,44,4,'trace $T=2a$ : la diagonale','encre','s')
save(fig,'77-068')
