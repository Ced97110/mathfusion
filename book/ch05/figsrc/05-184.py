import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cw=SIZE['l']*0.2124
s1='2 × 2 × 3 × 5 = 5 × 3 × 2 × 2'
s2=' '*4+s1[4:25]+' '*4
n=len(s1); x0=44-n*cw/2
def mono(y,s):
    ax.text(x0,y,s,color=COL['encre'],fontsize=SIZE['l'],family='DejaVu Sans Mono',ha='left',va='center',zorder=5)
y1,y2=52,22
for (a,b) in [(0,4),(25,4)]:
    ax.add_patch(Rectangle((x0+a*cw-0.3,y1-3.5),b*cw+0.6,7,ec=COL['varie'],fc=FILL['varie'],lw=0.8,zorder=2))
ax.add_patch(Rectangle((x0+27*cw-0.3,y1-3.5),2*cw+0.6,7,ec=COL['varie'],fc=FILL['varie'],lw=0.8,zorder=2)) if False else None
ax.add_patch(Rectangle((x0-0.3,y2-3.5),4*cw+0.6,7,ec=COL['varie'],fc='none',lw=0.8,ls='--',zorder=2))
ax.add_patch(Rectangle((x0+25*cw-0.3,y2-3.5),4*cw+0.6,7,ec=COL['varie'],fc='none',lw=0.8,ls='--',zorder=2))
mono(y1,s1); mono(y2,s2)
c=lambda i: x0+i*cw
brace(ax,c(0),c(13),y1-4.5,'sujet',label='60')
brace(ax,c(16),c(29),y1-4.5,'autre',label='60')
brace(ax,c(4),c(13),y2-4.5,'sujet',label='30')
brace(ax,c(16),c(25),y2-4.5,'autre',label='30')
arrow(ax,(8,y1-14),(8,y2+6),'varie')
text(ax,12,37,r'$\div 2$ des deux côtés','varie','m',ha='left')
text(ax,44,8,r'2 $\neq 0$ : la division existe','resultat','m')
save(fig,'05-184')
