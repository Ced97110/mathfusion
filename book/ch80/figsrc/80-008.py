import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
y0,s=16,0.8
tot=[0,30,15,5,-1,4,7,9,8]
labs=['30','−15','−10','−6','+5','+3','+2','−1']
roles=['sujet','varie','varie','varie','autre','autre','autre','varie']
bw,p,x0=7,8.6,3
line(ax,[(2,y0),(86,y0)],'fixe',lw=0.6)
for i in range(8):
    a,b=tot[i],tot[i+1]; lo,hi=min(a,b),max(a,b)
    x=x0+i*p
    ax.add_patch(Rectangle((x,y0+lo*s),bw,(hi-lo)*s,ec=COL[roles[i]],fc=FILL[roles[i]],lw=0.8,zorder=2))
    text(ax,x+bw/2,y0+hi*s+2.4,labs[i],roles[i],'s')
x=x0+8*p
ax.add_patch(Rectangle((x,y0),bw,8*s,ec=COL['resultat'],fc=FILL['resultat'],lw=0.8,zorder=2))
text(ax,x+bw/2,y0+8*s+3,'= 8','resultat','l',weight='bold')
text(ax,x0+3*p+bw/2,y0-4.2,'−1','varie','s')
text(ax,x0+2*p+bw/2,6,'retraits','varie','s'); text(ax,x0+5*p+bw/2,6,'remises','autre','s')
text(ax,x+bw/2,6,'résultat','resultat','s')
save(fig,'80-008')
