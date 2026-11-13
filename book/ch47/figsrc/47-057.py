import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
def grid(x0,nc,nr):
    for r in range(nr):
        for c in range(nc):
            box(ax,x0+6*c,22+6*r,5.6,5.6,'sujet' if r==nr-1 else 'fixe',r=0.3)
grid(10,4,3); grid(58,2,6)
text(ax,44,79,r'$|G|=|H|\times[G:H]$','encre','l')
text(ax,22,68,r'$H=\{0,3,6,9\}$','sujet','m'); text(ax,64,68,r'$H=\{0,6\}$','sujet','m')
brace(ax,10,33.6,41,'sujet',label=r'$|H|=4$',down=False); brace(ax,58,69.6,58.6,'sujet',label=r'$|H|=2$',down=False)
text(ax,22,16,r'$[G:H]=3$ lignes','resultat','m'); text(ax,64,16,r'$[G:H]=6$ lignes','resultat','m')
text(ax,22,8,r'$12=4\times3$','encre','s'); text(ax,64,8,r'$12=2\times6$','encre','s')
save(fig,'47-057')
