import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
R=9; cy=36
def pos(cx,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a),cy+R*math.sin(a))
def dial(cx,n,role_map):
    ax.add_patch(Circle((cx,cy),R,ec=COL['fixe'],fc='none',lw=0.8,zorder=1))
    for k in range(n):
        x,y=pos(cx,n,k); disc(ax,x,y,2.7,role_map.get(k,'sujet'),label=str(k),size='s')
    text(ax,cx,cy-R-6,f'$n={n}$','sujet','m')
cs=[16,44,72]
dial(cs[0],1,{}); dial(cs[1],2,{0:'resultat'}); dial(cs[2],3,{1:'resultat'})
# 1 + 1 = 0 on dial 2: step from 1 to 0
p,q=pos(cs[1],2,1),pos(cs[1],2,0)
arrow(ax,(p[0]+3.4,p[1]+2.5),(q[0]+3.4,q[1]-2.5),'varie',curve=0.9)
# 2 + 2 = 1 on dial 3: 2 -> 0 -> 1
a,b,c=pos(cs[2],3,2),pos(cs[2],3,0),pos(cs[2],3,1)
arrow(ax,(a[0]+0.5,a[1]+3),(b[0]-3,b[1]-0.8),'varie',curve=-0.35)
arrow(ax,(b[0]+3,b[1]-0.8),(c[0]-0.5,c[1]+3),'varie',curve=-0.35)
text(ax,cs[0],18,'1 retombe sur 0','fixe','s')
text(ax,cs[1],18,r'$1+1=0$','varie','m'); text(ax,cs[2],18,r'$2+2=1$','varie','m')
text(ax,44,57,r'$\mathbb{Z}/n$ : $n$ éléments','sujet','m')
save(fig,'51-080')
