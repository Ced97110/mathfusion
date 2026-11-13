import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(66)
x0,L=24,60
for k,(n,d,lab) in enumerate([(3,4,r'$3/4$'),(6,8,r'$6/8$'),(75,100,r'$75/100$')]):
    y=42-k*14; c=L/d
    for i in range(d): cell(ax,x0+i*c,y,c,9,'sujet',fill=i<n,lw=0.6 if d<10 else 0.15)
    text(ax,2,y+4.5,lab,'sujet','m',ha='left')
xe=x0+L*0.75
line(ax,[(xe,10),(xe,58)],'resultat',lw=1.0,dash=True)
text(ax,xe,62,'même part','resultat','s')
save(fig,'06-068')
