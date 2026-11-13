import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def plus(cx,cy):
    line(ax,[(cx-1,cy),(cx+1,cy)],'varie'); line(ax,[(cx,cy-1),(cx,cy+1)],'varie')
def rangee(y,n):
    for x in (3,16,29,55): box(ax,x,y,9,9,'sujet',label=n,size='l')
    for dx in (44,46.5,49): disc(ax,dx,y+4.5,0.5,'sujet')
    for px in (14,27,40.5,52.5): plus(px,y+4.5)
    brace(ax,3,64,y-2,'varie',label=n2,size='m')
text(ax,3,61,'Salle : 426 places, 4 €','encre','s',ha='left')
n2='426 fois'; rangee(47,'4')
text(ax,3,33,'Autre : 150 places, 6 €','encre','s',ha='left')
n2='150 fois'; rangee(19,'6')
text(ax,77,37,'même forme','resultat','m')
arrow(ax,(74,40),(66,50),'resultat',lw=0.8)
arrow(ax,(74,34),(66,25),'resultat',lw=0.8)
save(fig,'03-001')
