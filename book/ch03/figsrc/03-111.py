import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
xs=[4,18,32]
def rangee(yb, op, texte_court):
    for x in xs: box(ax,x,yb,10,9,'fixe',label='4',size='l')
    for x in (16,30): text(ax,x,yb+4.5,op,'encre','l')
    for x in xs: disc(ax,x+5,yb+12,1.6,'sujet')
    brace(ax,4,42,yb-1,'sujet',label='3 répétitions',down=True)
    arrow(ax,(44,yb+4.5),(52,yb+4.5),'varie')
    text(ax,68,yb+4.5,texte_court,'resultat','l')
rangee(36,'+','3 × 4 = 12')
line(ax,[(3,27.5),(85,27.5)],'fixe',dash=True)
rangee(11,'×','4³ = 64')
save(fig,'03-111')
