import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
eq=[r'$120=102\times 1+18$',r'$102=18\times 5+12$',r'$18=12\times 1+6$',r'$12=6\times 2+0$']
rem=[18,12,6,0]; ys=[54,42,30,18]
text(ax,2,66,'divisions','fixe','s',ha='left'); text(ax,54,66,'reste','fixe','s',ha='left')
line(ax,[(54,14),(54,62)],'fixe')
box(ax,1,26,86,8,'resultat',fill=False,dash=True,lw=1.2)
for t,r,y in zip(eq,rem,ys):
    text(ax,3,y,t,'encre','m',ha='left')
    if r>0:
        role='resultat' if r==6 else 'varie'
        ax.add_patch(Rectangle((54,y-2.5),r*1.2,5,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
        text(ax,54+r*1.2+2.5,y,str(r),role,'m')
    else:
        text(ax,56,y,'0 : arrêt','fixe','s',ha='left')
text(ax,44,8,'dernier reste non nul : 6','resultat','m')
save(fig,'05-116')
