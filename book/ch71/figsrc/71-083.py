import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for x0,tit,ok in ((2,'produit scalaire',True),(46,'autre forme',False)):
    box(ax,x0,4,40,54,'fixe',fill=False,dash=True)
    text(ax,x0+20,53,tit,'encre','m')
    disc(ax,x0+8,30,5.5,'sujet',label=r'$x$'); disc(ax,x0+32,30,5.5,'varie',label=r'$y$')
    arrow(ax,(x0+14.5,33),(x0+25.5,33),'resultat',curve=-0.0)
    text(ax,x0+20,38.5,r'$x\perp y$','resultat','s')
    if ok:
        arrow(ax,(x0+25.5,27),(x0+14.5,27),'resultat')
        text(ax,x0+20,21,r'$y\perp x$','resultat','s'); text(ax,x0+20,11,'dans les deux sens','resultat','s')
    else:
        arrow(ax,(x0+25.5,27),(x0+14.5,27),'limite')
        line(ax,[(x0+18,24.5),(x0+22,29.5)],'limite',lw=1.4); line(ax,[(x0+22,24.5),(x0+18,29.5)],'limite',lw=1.4)
        text(ax,x0+20,21,r'$y\perp x$ ?','limite','s'); text(ax,x0+20,11,'pas assuré','limite','s')
save(fig,'71-083')
