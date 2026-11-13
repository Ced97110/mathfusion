import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
c=7.5; x0,y0=2,6
for r in range(7):
    for k in range(8):
        box(ax,x0+k*c,y0+r*c,c-0.4,c-0.4,'sujet' if r==0 else 'varie',r=0.3,lw=0.5)
text(ax,x0+(c-0.4)/2,y0+(c-0.4)/2,r'$e$','sujet','m',weight='bold')
yb=y0+c-0.4
line(ax,[(63,y0+7*c-0.4),(64,y0+7*c-0.4),(64,y0+c),(63,y0+c)],'varie')
line(ax,[(63,yb),(64,yb),(64,y0),(63,y0)],'sujet')
text(ax,66,(y0+c+y0+7*c)/2,"48 d'ordre 7",'varie','s',ha='left')
text(ax,66,y0+(c-0.4)/2,'8 restantes','sujet','s',ha='left')
text(ax,31,63,'56 éléments','encre','s')
save(fig,'50-228')
