import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
def mw(s, size='l', weight='normal'):
    t=fig.text(0,0,s,fontsize=SIZE[size],fontweight=weight)
    w=t.get_window_extent(fig.canvas.get_renderer()).width
    t.remove(); return w*25.4/fig.dpi
# exemple avec groupement
text(ax,22,66,'avec groupement','encre','s')
part1='(2 + 3)'; part2='× 4'
Wp=mw(part1); Wq=mw(part2); gap=2.2
left=18-(Wp+gap+Wq)/2
text(ax,left,58,part1,'encre','l',ha='left')
text(ax,left+Wp+gap,58,part2,'encre','l',ha='left')
box(ax,left-1.1,54.5,Wp+2.2,7,'sujet',fill=False)
brace(ax,9,20,53.5,'varie',label='vaut 5',down=True,size='s')
text(ax,36,58,'= 20','resultat','l')
# sans groupement
text(ax,66,66,'sans groupement','encre','s')
text(ax,66,58,'2 + 3 × 4 = 14','autre','m')
line(ax,[(6,42),(82,42)],'fixe',lw=0.5)
# la famille des quatre signes
for x,sym,name in [(4,'( )','parenthèses'),(25,'[ ]','crochets'),(46,'{ }','accolades')]:
    box(ax,x,6,17,22,'sujet',fill=False)
    text(ax,x+8.5,22,sym,'sujet','l')
    text(ax,x+8.5,10,name,'fixe','s')
box(ax,67,6,17,22,'sujet',fill=False)
line(ax,[(70,22),(81,22)],'sujet',lw=1.4)
ax.add_patch(Rectangle((72,24),7,3,fc=COL['fixe'],ec='none',zorder=3))
ax.add_patch(Rectangle((72,17),7,3,fc=COL['fixe'],ec='none',zorder=3))
text(ax,75.5,10,'barre','fixe','s')
save(fig,'04-048')
