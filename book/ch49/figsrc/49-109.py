import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
cx,cy,h=22,38,13
pts=[(cx-h,cy+h),(cx+h,cy+h),(cx+h,cy-h),(cx-h,cy-h)]
poly(ax,pts,'fixe',fill=False)
ax.plot([cx-h-3,cx+h+3],[cy+h+3,cy-h-3],color=COL['fixe'],lw=0.9,ls='--',zorder=1)
arrow(ax,(cx+h-2.5,cy+h-2.5),(cx-h+2.5,cy-h+2.5),'varie',both=True)
for p,l in zip(pts,'1234'): disc(ax,p[0],p[1],3.6,'sujet',label=l,size='s')
text(ax,22,64,'réflexion : 1↦1, 2↦4','varie','s')
text(ax,22,16,'axe : 1 et 3 fixes','fixe','s')
text(ax,66,64,'rotations seules :','encre','s')
for y,t in zip([52,42,32,22],['0° : 1↦1, 2↦2','90° : 1↦2, 2↦3','180° : 1↦3, 2↦4','270° : 1↦4, 2↦1']):
    text(ax,66,y,t,'limite','s')
text(ax,66,10,'aucune ne fait 1↦1, 2↦4','limite','s',weight='bold')
save(fig,'49-109')
