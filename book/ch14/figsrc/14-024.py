import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
xs=[4,30,56]
for x in xs: box(ax,x,48,9,9,'sujet',label='$a$')
for x,l in zip(xs,['$n$','$m$','$n+m$']): text(ax,x+12,56,l,'fixe','s')
text(ax,24,52.5,r'$\times$'); text(ax,50,52.5,'=')
for x in xs:
    arrow(ax,(x+4.5,47),(x+4.5,33),'varie')
    box(ax,x,22,9,9,'sujet',label='2')
brace(ax,4,65,22,'sujet',label='même nombre des deux côtés')
save(fig,'14-024')
