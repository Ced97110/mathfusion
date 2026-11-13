import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
o=(32,38); u=8
def P(a,b,k): return (o[0]+k*a*u, o[1]+k*b*u)
line(ax,[P(-1,0,0)[:1]+(o[1],),(0,0)],'fixe') if False else None
# plan V : cadre
box(ax,3,6,58,66,'fixe',fill=False,dash=True,label=None)
text(ax,6,68,r'plan $V$ : $n=2$','fixe','s',ha='left')
arrow(ax,P(-1.5,-3,1)[0:2] if False else (o[0]-1.4*u,o[1]-2.8*u),(o[0]+1.4*u,o[1]+2.8*u),'sujet',lw=1.3)
arrow(ax,(o[0]-2.2*u,o[1]+1.1*u),(o[0]+2.2*u,o[1]-1.1*u),'resultat',lw=1.3)
# angle droit
s=3.0; a=(2/5**.5,-1/5**.5); b=(1/5**.5,2/5**.5)
line(ax,[(o[0]+s*b[0],o[1]+s*b[1]),(o[0]+s*(a[0]+b[0]),o[1]+s*(a[1]+b[1])),(o[0]+s*a[0],o[1]+s*a[1])],'fixe')
text(ax,o[0]+9,o[1]+27,r'$U$ : $k=1$','sujet','m')
text(ax,o[0]+13,o[1]-15,r'$U^{\perp}$ : $n-k=1$','resultat','m')
box(ax,64,26,22,24,'resultat')
text(ax,75,44,r'$n=2$','encre','m'); text(ax,75,38,r'$k=1$','sujet','m')
line(ax,[(66,34),(84,34)],'fixe')
text(ax,75,29.5,r'$2-1=1$','resultat','m')
save(fig,'71-081')
