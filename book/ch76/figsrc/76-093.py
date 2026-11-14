import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
A=[[2,1],[1,3]]
def mat(x0,picks,role):
    for i in range(2):
        for j in range(2):
            box(ax,x0+j*13,40+(1-i)*13,13,13,role if (i,j) in picks else 'fixe',label=str(A[i][j]),size='l')
mat(10,[(0,0),(1,1)],'sujet'); mat(54,[(1,0),(0,1)],'varie')
text(ax,23,72,'rangement 1, 2','sujet','m'); text(ax,67,72,'rangement 2, 1','varie','m')
text(ax,23,32,r'$+\,2\times3=6$','sujet','l'); text(ax,67,32,r'$-\,1\times1=-1$','varie','l')
text(ax,44,14,r'$\det A=6-1=5$','resultat','xl')
save(fig,'76-093')
