import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax,x,y,r,role): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],lw=0.5,zorder=4))
fig,ax=canvas(62)
for k,x in enumerate((4,22,40)):
    box(ax,x,53.5,16.6,5,'resultat',fill=False)
    for j in range(6): dot(ax,5.3+18*k+2.8*j,56,0.9,'resultat')
text(ax,60,56,'reste 0','resultat','s',ha='left')
text(ax,4,49,'oui : 6 divise 18','resultat','m',ha='left')
text(ax,4,44,'18 ÷ 6 = 3 : un nombre','autre','s',ha='left')
line(ax,[(2,38),(86,38)],'fixe',lw=0.5)
for k,x in enumerate((4,17,30)):
    box(ax,x,27.5,11,5,'fixe',fill=False)
    for j in range(4): dot(ax,5.3+13*k+2.8*j,30,0.9,'fixe')
box(ax,44,27.5,5.4,5,'limite',fill=False,dash=True)
dot(ax,45.3,30,0.9,'limite'); dot(ax,48.1,30,0.9,'limite')
text(ax,53,30,'reste 2','limite','s',ha='left')
text(ax,4,23,'non : 4 ne divise pas 14','limite','m',ha='left')
text(ax,4,18,'4 < 14 : vrai pourtant','autre','s',ha='left')
save(fig,'03-062')
