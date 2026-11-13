import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(76)
s=0.3; x0=8; y0=6
brace(ax,x0,x0+252*s,y0+198*s,'fixe',label='252',down=False)
def sqr(x,y,l,role,lab):
    rect(ax,x,y,l,l,role); text(ax,x+l/2,y+l/2,lab,role,'s')
sqr(x0,y0,198*s,'sujet','198')
xr=x0+198*s
for k in range(3): sqr(xr,y0+k*54*s,54*s,'varie','54')
yt=y0+162*s
sqr(xr,yt,36*s,'autre','36')
sqr(xr+36*s,yt,18*s,'resultat','18'); sqr(xr+36*s,yt+18*s,18*s,'resultat','18')
text(ax,44,2.5,'dernier carré : côté 18','resultat','s')
save(fig,'05-142')
