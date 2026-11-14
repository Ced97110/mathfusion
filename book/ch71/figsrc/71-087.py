import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
rows=((50,'produit scalaire','symétrique',True),(28,'aire orientée','alternée',True),(6,r'$x_1y_2$','autre forme',False))
for y0,nm,fam,ok in rows:
    r='resultat' if ok else 'limite'
    box(ax,2,y0,36,18,'sujet' if ok else 'fixe')
    text(ax,20,y0+12,nm,'sujet' if ok else 'encre','s'); text(ax,20,y0+5.5,fam,'sujet' if ok else 'encre','s')
    arrow(ax,(42,y0+12),(60,y0+12),r); 
    if ok:
        arrow(ax,(60,y0+6),(42,y0+6),r); text(ax,74,y0+9,'sans ordre','resultat','s')
    else:
        arrow(ax,(60,y0+6),(42,y0+6),'limite'); line(ax,[(49,y0+3),(53,y0+9)],'limite',lw=1.4); line(ax,[(53,y0+3),(49,y0+9)],'limite',lw=1.4)
        text(ax,74,y0+9,'ordre à préciser','limite','s')
save(fig,'71-087')
