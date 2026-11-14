import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
xa=[30,46]; xb=[46,62]
box(ax,xa[0]-9,48,34,14,'sujet',fill=False); box(ax,xb[0]-9,18,34,14,'autre',fill=False)
for x,n in zip(xa,[0,1]): disc(ax,x,55,4.5,'sujet',label=str(n))
for x,n in zip(xb,[1,2]): disc(ax,x,25,4.5,'autre',label=str(n))
line(ax,[(46,50.5),(46,29.5)],'limite',lw=1.2,dash=True)
text(ax,50,40,'1 en commun','limite','s',ha='left')
text(ax,44,67,r'$H+0=\{0,1\}$','sujet','m'); text(ax,44,12,r'$H+1=\{1,2\}$','autre','m')
text(ax,44,4,'ni égales, ni séparées','limite','m')
save(fig,'47-068')
