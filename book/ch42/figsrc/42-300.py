import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,2,4,84,70,'fixe',fill=False)
text(ax,44,69,'applications de $S$ vers $S$ : monoïde','fixe','s')
box(ax,6,8,38,54,'resultat'); box(ax,48,8,36,54,'limite')
def mini(x,ys_r,col):
    for y in (46,36): disc(ax,x,y,1.5,col)
    for y in (46,36): disc(ax,x+18,y,1.5,col)
    for ya,yb in ys_r: arrow(ax,(x+2,ya),(x+16,yb),col)
mini(14,[(46,46),(36,36)],'resultat')
for y in (46,36): disc(ax,58,y,1.5,'limite'); 
disc(ax,76,46,1.5,'limite'); disc(ax,76,36,1.5,'fixe')
arrow(ax,(60,46),(74,46),'limite'); arrow(ax,(60,36),(74.5,45),'limite')
text(ax,25,25,'bijections','resultat','m',weight='bold'); text(ax,25,17,'inverse : oui','resultat','s'); text(ax,25,12,'groupe','resultat','s')
text(ax,66,25,'tout sur un seul','limite','s'); text(ax,66,17,'inverse : non','limite','s')
save(fig,'42-300')
