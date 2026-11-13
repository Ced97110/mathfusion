import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
y=20
f=numberline(ax,8,76,y,-12,24,6)
for v in (0,-12,6):
    line(ax,[(f(v),y),(f(v),38+ (8 if v!=0 else 0))],'fixe',lw=0.5,dash=True) if v!=0 else None
arrow(ax,(f(0),30),(f(-12),30),'varie')
text(ax,f(-6),34,r'$12\times(-1)$','varie','s')
arrow(ax,(f(-12),41),(f(6),41),'autre')
text(ax,f(-3),45,r'$+\ 18\times 1$','autre','s')
disc(ax,f(6),y,1.6,'resultat'); text(ax,f(6),y+5,'6','resultat','m',weight='bold')
text(ax,f(-6)-6,54,r'$u=-1$ : on recule','varie','m')
text(ax,44,5,'sans négatif : 12, 18, 24…','limite','s')
save(fig,'05-099')
