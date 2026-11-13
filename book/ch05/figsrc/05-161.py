import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
for i,d in enumerate([5,12,1000]):
    box(ax,2+i*29,66,26,9,'fixe',label=r'$0=%s\times0$'%(str(d)),size='s')
text(ax,44,60,'tout nombre divise 0','autre','s')
x0,x1=30,82
f=lambda v: x0+(v-1)/11*(x1-x0)
line(ax,[(f(12),12),(f(12),55)],'fixe',dash=True)
rows=[(48,'diviseurs de 0','sujet',list(range(1,13))),(36,'diviseurs de 12','autre',[1,2,3,4,6,12]),(24,'en commun','resultat',[1,2,3,4,6,12])]
for y,lab,role,vals in rows:
    text(ax,2,y,lab,role,'s',ha='left')
    for v in vals: disc(ax,f(v),y,2.0,role)
text(ax,x1+1,48,'…','sujet','l',ha='left')
disc(ax,f(12),24,3.4,'resultat',fill=False,lw=1.4)
line(ax,[(x0,12),(x1,12)])
for v in range(1,13): ax.plot([f(v)]*2,[11,13],color=COL['fixe'],lw=0.8)
text(ax,f(1),7.5,'1','fixe','s'); text(ax,f(12),7.5,'12','fixe','s')
text(ax,f(12)-5,17.5,r'$\mathrm{PGCD}(0,12)=12$','resultat','s',ha='right')
save(fig,'05-161')
