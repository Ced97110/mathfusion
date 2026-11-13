import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,R=28,34,18
line(ax,[(cx-R-3,cy),(cx+R+3,cy)],'fixe',lw=0.5); line(ax,[(cx,cy-R-3),(cx,cy+R+3)],'fixe',lw=0.5)
disc(ax,cx,cy,R,'fixe',fill=False,lw=1.0)
disc(ax,cx-R,cy,1.5,'resultat'); disc(ax,cx,cy+R,1.5,'limite')
text(ax,cx-R+7,cy+3,'180°','resultat','s'); text(ax,cx+6,cy+R-3,'90°','limite','s')
text(ax,68,55,'cos 90° = 0','limite','s'); box(ax,50,44,36,8,'limite',label='0 + 0 + 1 = 1 ≠ 0',size='s')
text(ax,68,33,'cos 180° = −1','resultat','s'); box(ax,50,22,36,8,'resultat',label='1 + (−2) + 1 = 0',size='s')
text(ax,44,6,'une seule solution : 180°','resultat','m')
save(fig,'32-103')
