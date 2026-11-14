import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
for x,t,r in [(22,'[','varie'),(32,r'$G$','fixe'),(42,':','encre'),(52,r'$H$','sujet'),(62,']','varie')]:
    text(ax,x,70,t,r,'xl')
text(ax,32,60,'grand groupe','fixe','s'); text(ax,52,60,'sous-groupe','sujet','s')
text(ax,42,53,'= nombre de lignes','varie','s')
text(ax,10,41,r'$|H|\to[G:H]$','encre','s',ha='left')
cs=2.4
def g(x0,cols,rows,cap):
    for c in range(cols):
        for r in range(rows): box(ax,x0+c*cs,14+r*cs,cs-0.4,cs-0.4,'varie',r=0.2)
    text(ax,x0+cols*cs/2,8,cap,'varie','s')
g(10,4,3,'4 → 3'); g(36,2,6,'2 → 6'); g(54,12,1,'12 → 1')
save(fig,'47-075')
