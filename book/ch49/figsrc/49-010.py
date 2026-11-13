import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
def mini(x,y,s,cols):
    ax.add_patch(Rectangle((x,y),s,s,ec=COL['fixe'],fc=FILL['fixe'],lw=0.6,zorder=2))
    for (a,b),c in zip(((.25,.75),(.75,.75),(.25,.25),(.75,.25)),cols):
        ax.add_patch(Circle((x+a*s,y+b*s),s*0.17,ec=COL[c],fc=FILL[c],lw=0.6,zorder=3))
text(ax,18,58,'16 ÷ 4 = 4','limite','l')
for bx,by in ((6,38),(19,38),(6,25),(19,25)):
    box(ax,bx,by,11,11,'limite',fill=False)
    for i in range(2):
        for j in range(2): disc(ax,bx+3+i*5,by+3+j*5,1.6,'fixe')
text(ax,18,19,'4 paquets de 4 : faux','limite','s')
text(ax,63,58,'en réalité','resultat','l')
mini(46,41,10,['sujet']*4); mini(64,41,10,['varie']*4)
text(ax,51,37,'tout bleu : 1','sujet','s'); text(ax,69,37,'tout orange : 1','varie','s')
box(ax,40,6,46,24,'fixe',fill=False,dash=True)
for k in range(14): disc(ax,46+(k%7)*5.7,24-(k//7)*5.5,1.8,'fixe')
text(ax,63,9.5,'14 autres : tailles 4 et 2','fixe','s')
save(fig,'49-010')
