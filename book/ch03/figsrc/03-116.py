import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
def grille(x0,y0,cols,rows):
    for c in range(cols):
        for r in range(rows): box(ax,x0+4*c,y0+4*r,4,4,'fixe',r=0.3,lw=0.5)
text(ax,3,85,'Deux morceaux','encre','s',ha='left')
grille(8,66,4,3); brace(ax,8,24,65.5,'fixe',label='x = 4',down=True)
text(ax,16,56,'3 × x = 3x = 12','encre','s')
grille(36,66,2,3); brace(ax,36,44,65.5,'fixe',label='2',down=True)
text(ax,40,56,'3 × 2 = 6','encre','s')
for x,tx in ((6.5,3.5),(34,31.5)):
    arrow(ax,(x,66),(x,78),'sujet',both=True); text(ax,tx,72,'3','sujet','m')
arrow(ax,(28,52),(28,44),'varie'); text(ax,31,48,'recoller','varie','s',ha='left')
grille(8,28,6,3)
line(ax,[(24,28),(24,40)],'varie',lw=1.2,dash=True)
arrow(ax,(6.5,28),(6.5,40),'sujet',both=True); text(ax,3.5,34,'3','sujet','m')
brace(ax,8,32,27.5,'fixe',label='x + 2 = 6',down=True)
text(ax,61,34,'3 × (x + 2) = 18','resultat','m')
text(ax,44,10,'3x + 6 = 3(x + 2)','resultat','l')
save(fig,'03-116')
