import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def frac(cx,top,bot,y):
    text(ax,cx,y+6,top,'sujet','l'); line(ax,[(cx-4,y+1.5),(cx+4,y+1.5)],'sujet')
    return
for cx,top in ((18,'3'),(50,'4')):
    frac(cx,top,'5',50)
    disc(ax,cx,46,3.2,'varie',label='5',size='m')
text(ax,34,52,r'$\div$','encre','l')
text(ax,34,38.5,'hypoténuse 5','varie','s')
arrow(ax,(34,34),(34,25),'varie')
text(ax,38,29,'les 5 s’annulent','varie','s',ha='left')
text(ax,34,18,'3','resultat','l'); line(ax,[(30,13.5),(38,13.5)],'resultat'); text(ax,34,9,'4','resultat','l')
text(ax,44,13.5,'= tangente','resultat','m',ha='left')
save(fig,'26-038')
