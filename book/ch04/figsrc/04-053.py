import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
def mw(s, size='l', weight='normal'):
    t=fig.text(0,0,s,fontsize=SIZE[size],fontweight=weight)
    w=t.get_window_extent(fig.canvas.get_renderer()).width
    t.remove(); return w*25.4/fig.dpi
text(ax,44,67,'trois aspects, un seul sens','encre','s')
# trois lignes : même partie 2 + 3 entourée par trois signes différents
for y,p1 in [(58,'(2 + 3)'),(47,'[2 + 3]'),(36,'{2 + 3}')]:
    p2='× 4'; Wp=mw(p1); Wq=mw(p2); gap=2.2
    left=28-(Wp+gap+Wq)/2
    text(ax,left,y,p1,'encre','l',ha='left')
    text(ax,left+Wp+gap,y,p2,'encre','l',ha='left')
    box(ax,left-1.1,y-3.5,Wp+2.2,7,'sujet',fill=False,lw=0.6)
    text(ax,56,y,'= 20','resultat','l')
line(ax,[(64,34),(64,60)],'resultat',lw=0.6)
text(ax,75,47,'même sens','resultat','s')
# écriture refusée
line(ax,[(6,28),(82,28)],'fixe',lw=0.5)
text(ax,28,18,'(2 + 3] × 4','limite','l')
line(ax,[(16,15),(40,21)],'limite',lw=0.8)
text(ax,66,18,'ouvre ( , ferme ] : non','limite','s')
save(fig,'04-053')
