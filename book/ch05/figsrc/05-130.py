import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(50)
f=numberline(ax,4,78,24,0,26,1,labels=False)
disc(ax,f(0),24,1.8,'fixe')
for v in range(4,25,4): disc(ax,f(v),34,1.8,'sujet')
for v in range(6,25,6): disc(ax,f(v),14,1.8,'varie')
for v in (12,24):
    line(ax,[(f(v),16.2),(f(v),31.8)],'resultat',dash=True)
    text(ax,f(v),39,str(v),'resultat','m')
text(ax,4,44,'multiples de 4','sujet','s',ha='left')
text(ax,4,8,'multiples de 6','varie','s',ha='left')
text(ax,3,19.5,'0 : non retenu','fixe','s',ha='left')
text(ax,44,3,'rencontres : 12 puis 24','resultat','m')
save(fig,'05-130')
