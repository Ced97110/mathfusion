import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(72)
text(ax,22,68,'produit des normes','fixe','s'); text(ax,66,68,'norme du produit','varie','s')
box(ax,2,52,40,9,'sujet',label='$N(1+2i)=5$',size='s')
box(ax,2,37,40,9,'autre',label='$N(3+4i)=25$',size='s')
text(ax,22,48.7,'$\\times$','fixe','m')
arrow(ax,(22,37),(22,31),'fixe')
box(ax,2,22,40,9,'resultat',label='$5\\times25=125$',size='s')
box(ax,46,52,40,9,'varie',label='$(1+2i)(3+4i)$',size='s')
box(ax,46,37,40,9,'varie',label='$=-5+10i$',size='s')
arrow(ax,(66,52),(66,46.5),'varie'); arrow(ax,(66,37),(66,31),'varie')
box(ax,46,22,40,9,'resultat',label='$25+100=125$',size='s')
text(ax,44,26.5,'$=$','resultat','l')
save(fig,'77-077')
