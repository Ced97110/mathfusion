import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,70,r'$18=12\times1+6$','encre','l',weight='bold')
text(ax,2,60,'diviseurs communs de 18, 12','sujet','s',ha='left')
text(ax,2,19,'diviseurs communs de 12, 6','autre','s',ha='left')
for i,v in enumerate([1,2,3,6]):
    x=14+14*i
    box(ax,x,45,11,9,'sujet',label=str(v),size='l')
    box(ax,x,24,11,9,'autre',label=str(v),size='l')
    arrow(ax,(x+5.5,44),(x+5.5,34.5),'resultat',both=True)
text(ax,78,39,'=','resultat',16,weight='bold')
save(fig,'05-083')
