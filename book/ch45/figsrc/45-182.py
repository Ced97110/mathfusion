import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=lambda v: 10+v*64/12
rows=[(2,44),(3,30),(4,16)]
for n,y in rows:
    text(ax,10,y+5.5,f'horloge de {n} heures','sujet','s',ha='left')
    line(ax,[(f(0),y),(f(12),y)],'fixe',lw=0.6)
    for v in range(0,13,n): disc(ax,f(v),y,1.8,'sujet')
ax.plot([f(12)]*2,[10,56],color=COL['resultat'],lw=1.2,ls='--',zorder=1)
text(ax,f(12)-1,58,'PPCM = 12','resultat','m',ha='right',weight='bold')
f=numberline(ax,10,74,10,0,12,step=1,every=4,arrow_right=False)
text(ax,44,2.4,'nombre d’appuis','encre','s')
save(fig,'45-182')
