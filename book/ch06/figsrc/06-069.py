import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
text(ax,44,76,r'$a \times d = b \times c$','sujet','l')
def blk(xl,xr,n,xc,role,s1,s2,sign,verdict):
    for (x,t) in [(xl,n[0]),(xr,n[1])]: text(ax,x,50,t,'sujet' if x==xl else 'autre','l')
    text(ax,xc,60,sign,role,'l')
    arrow(ax,(xl+4,52),(xr-4,48),'varie'); arrow(ax,(xl+4,48),(xr-4,52),'varie')
    text(ax,xc,34,s1,role,'m'); text(ax,xc,24,s2,role,'m')
    text(ax,xc,12,verdict,role,'m',weight='bold')
blk(8,34,(r'$\frac{3}{4}$',r'$\frac{6}{8}$'),21,'resultat',r'$3\times 8 = 24$',r'$4\times 6 = 24$','=','équivalentes')
blk(54,80,(r'$\frac{3}{4}$',r'$\frac{5}{7}$'),67,'limite',r'$3\times 7 = 21$',r'$4\times 5 = 20$',r'$\neq$','différentes')
save(fig,'06-069')
