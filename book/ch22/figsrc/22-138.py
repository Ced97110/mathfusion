import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
def row(y,mid,tail,r2):
    box(ax,3,y,32,12,'sujet',label='$\\sqrt{2m+3}$',size='m')
    text(ax,41,y+6,mid,'encre','l')
    box(ax,47,y,28,12,r2,label='$\\sqrt{m-8}$',size='m')
    if tail: text(ax,81,y+6,tail,'encre','m')
row(38,'$-$','$=0$','autre')
row(8,'$=$',None,'autre')
arrow(ax,(44,36),(44,22),'varie')
text(ax,66,29,'revient à','varie','s')
text(ax,19,52,'radical','sujet','s'); text(ax,61,52,'radical','autre','s')
save(fig,'22-138')
