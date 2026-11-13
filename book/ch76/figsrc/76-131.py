import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
def blk(yc,fw,col):
    a=(14,yc+8); b=(14,yc-8); p=(66,yc)
    disc(ax,*a,1.2,'sujet'); disc(ax,*b,1.2,'autre'); disc(ax,*p,1.4,'resultat')
    text(ax,a[0]+9,a[1]+3,'(2, 0)','sujet','s'); text(ax,b[0]+9,b[1]-3,'(0, 1)','autre','s'); text(ax,p[0]+1,p[1]-5,'(4, 2)','resultat','s')
    return a,b,p
a,b,p=blk(62,True,'varie')
arrow(ax,(a[0]+2,a[1]-0.3),(p[0]-2,p[1]+0.8),'varie'); arrow(ax,(b[0]+2,b[1]+0.3),(p[0]-2,p[1]-0.8),'varie')
text(ax,6,76,'T : deux points, un seul résultat','varie','s',ha='left')
a,b,p=blk(22,False,'limite')
arrow(ax,(p[0]-2,p[1]+0.8),(a[0]+2,a[1]-0.3),'limite'); arrow(ax,(p[0]-2,p[1]-0.8),(b[0]+2,b[1]+0.3),'limite')
text(ax,40,38,'retour : deux chemins ?','limite','s')
text(ax,44,4,'pas d’inverse','limite','l')
save(fig,'76-131')
