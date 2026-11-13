import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(48)
text(ax,44,42,'multiples communs de 4 et 6','encre','m')
x0=3; bw=14; g=3.5
items=[('0','limite',True),('12','resultat',False),('24','sujet',False),('36','sujet',False),('…','sujet',False)]
cx={}
for i,(t,r,d) in enumerate(items):
    x=x0+i*(bw+g); cx[t]=x+bw/2
    box(ax,x,24,bw,12,r,fill=not d,label=t,size='l',dash=d)
text(ax,x0,19,'0 exclu','limite','s',ha='left')
text(ax,cx['12'],8,'PPCM = 12','resultat','l')
arrow(ax,(cx['12'],11),(cx['12'],23),'resultat')
text(ax,63,8,'le plus petit, autre que 0','encre','s')
save(fig,'05-128')
