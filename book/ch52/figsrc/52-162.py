import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,72,'≅ : même structure','encre','m')
text(ax,20,65,'ℤ/12ℤ sur {0, 4, 8}','sujet','s')
text(ax,72,65,'ℤ/4ℤ','autre','s')
L=['{0, 4, 8}','{1, 5, 9}','{2, 6, 10}','{3, 7, 11}']
for i,s in enumerate(L):
    y=48-i*13
    box(ax,4,y,32,9,'sujet',label=s,size='s')
    box(ax,64,y,16,9,'autre',label=str(i),size='s')
    arrow(ax,(36,y+4.5),(64,y+4.5),'varie',both=True)
text(ax,50,6,'on renomme les classes','varie','s')
save(fig,'52-162')
