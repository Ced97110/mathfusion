import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
def row(y,label,n):
    text(ax,12,y+3.5,label,'encre','s')
    for i in range(n): box(ax,24+i*7.3,y,6.5,7,'fixe',label='12',size='s')
    box(ax,24+n*7.3,y,6.5,7,'resultat',label='1',size='s')
row(34,'5 × 5 = 25',2)
row(16,'17 × 5 = 85',7)
text(ax,24+7.3*8/2+1,47,'des paquets de 12, puis il reste 1','encre','s')
text(ax,44,4,'même reste : 1','resultat','m')
save(fig,'52-004')
