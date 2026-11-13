import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
def bx(x,y,w,h,ec,fc,lab,lw=0.8,size='l'):
    ax.add_patch(FancyBboxPatch((x+.8,y+.8),w-1.6,h-1.6,boxstyle='round,pad=0.8',lw=lw,ec=COL[ec],fc=FILL[fc],zorder=2))
    text(ax,x+w/2,y+h/2,lab,ec if ec!='limite' else 'encre',size)
text(ax,23,82,'dizaines','encre','m'); text(ax,41,82,'unités','encre','m')
bx(14,64,18,12,'sujet','sujet','5'); bx(32,64,18,12,'limite','sujet','2',lw=1.4)
text(ax,69,70,'2 − 7 : impossible','limite','s')
arrow(ax,(23,64),(41,48),'varie'); text(ax,69,56,'1 dizaine → 10 unités','varie','s')
bx(14,36,18,12,'varie','varie','4'); bx(32,36,18,12,'varie','varie','12')
text(ax,69,42,'12 − 7 = 5','resultat','s')
text(ax,22,24,'avant : 50 + 2 = 52','sujet','s'); text(ax,64,24,'après : 40 + 12 = 52','sujet','s')
text(ax,44,12,'même nombre : 52','resultat','l')
save(fig,'02-051')
