import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
Y=36
b=box(ax,20.5,Y-3,66.5,5.4,'sujet',dash=True,lw=0.7,r=1.5); b.set_zorder(1)
f=numberline(ax,16,84,Y,0,17,1,labels=False,arrow_right=False)
arrow(ax,(84,Y),(85.5,Y),'fixe',lw=0.9)
for v,x in [(0,16),(2,24),(7,44),(12,64),(17,84)]:
    text(ax,x,Y-5,str(v),'fixe','s')
for x in (84,64,44): disc(ax,x,Y,1.6,'sujet')
for a,c in [(84,64),(64,44),(44,24)]:
    arrow(ax,(a,Y+2),(c,Y+2),'varie',curve=0.5)
    text(ax,(a+c)/2,Y+9,'retirer 5','varie','s')
disc(ax,24,Y,2.0,'resultat')
text(ax,24,Y-10,'plus petit : 2\nexiste (bon ordre)','resultat','s')
ax.add_patch(FancyArrowPatch((24,Y+2),(4.8,Y+0.6),arrowstyle='-|>',mutation_scale=7,lw=1.0,color=COL['limite'],ls='--',connectionstyle='arc3,rad=0.5',zorder=4,shrinkA=0,shrinkB=0))
line(ax,[(3,Y-1),(5,Y+1)],'limite',lw=1.0); line(ax,[(3,Y+1),(5,Y-1)],'limite',lw=1.0)
text(ax,3,Y+15,'on ne peut plus retirer 5','limite','s',ha='left')
text(ax,64,Y-9.5,'collection : 17, 12, 7, 2','sujet','s')
brace(ax,24,84,22,'varie',label='3 paquets de 5')
text(ax,44,8,r'17 = 5 $\times$ 3 + 2 (reste 2 < 5)','encre','m')
save(fig,'01-191')
