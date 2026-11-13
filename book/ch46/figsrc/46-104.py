import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(80)
xs=[13,40,70]; top=['3','4','7']; bot=['8','16','128']
for x,t,b in zip(xs,top,bot):
    box(ax,x-8,56,16,10,'sujet' if t!='7' else 'resultat',label=t,size='l')
    box(ax,x-8,18,16,10,'autre' if t!='7' else 'resultat',label=b,size='l')
    arrow(ax,(x,56),(x,29),'varie')
    text(ax,x+6,42,r'$\varphi$','varie','s')
text(ax,26.5,61,'+','encre','l'); text(ax,55,61,'=','encre','l')
text(ax,26.5,23,r'$\times$','encre','l'); text(ax,55,23,'=','encre','l')
text(ax,4,74,r'$\mathbb{Z}$ (addition)','sujet','s',ha='left')
text(ax,4,8,'puissances de 2 (produit)','autre','s',ha='left')
save(fig,'46-104')
