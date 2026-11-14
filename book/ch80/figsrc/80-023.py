import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
d=26
line(ax,[(10,36+d),(25,36+d)],'fixe'); line(ax,[(34,36+d),(47,36+d)],'fixe'); line(ax,[(56,36+d),(78,36+d)],'fixe')
for x in (25,34,47,56): disc(ax,x,36+d,0.9,'sujet')
line(ax,[(25,36+d),(32,41+d)],'sujet',lw=1.2); line(ax,[(47,36+d),(54,41+d)],'autre',lw=1.2)
text(ax,29.5,44+d,r'$a$','sujet','m'); text(ax,51.5,44+d,r'$b$','autre','m')
line(ax,[(10,12+d),(78,12+d)],'fixe'); line(ax,[(10,12+d),(10,21+d)],'fixe'); line(ax,[(10,27+d),(10,36+d)],'fixe')
line(ax,[(5.5,27+d),(14.5,27+d)],'encre',lw=1.4); line(ax,[(7.5,21+d),(12.5,21+d)],'encre',lw=1.4)
line(ax,[(78,36+d),(78,28+d)],'fixe'); line(ax,[(78,12+d),(78,20+d)],'fixe')
disc(ax,78,24+d,4,'varie'); line(ax,[(75.2,21.2+d),(80.8,26.8+d)],'varie'); line(ax,[(75.2,26.8+d),(80.8,21.2+d)],'varie')
text(ax,24,24+d,'pile','encre','s'); text(ax,64,24+d,'lampe','varie','s')
disc(ax,14,36+d,1.2,'encre'); disc(ax,70,36+d,1.2,'encre')
text(ax,14,31+d,'A','encre','m'); text(ax,70,31+d,'B','encre','m')
# quatre positions : 1 = fermé, 0 = ouvert ; la lampe est allumée si a et b sont fermés
for i,(pa,pb) in enumerate([(0,0),(0,1),(1,0),(1,1)]):
    x=2+i*21.5; lit=(pa==1 and pb==1)
    box(ax,x,4,19,26,'varie' if lit else 'fixe',fill=lit,dash=not lit)
    text(ax,x+9.5,24,r'$a$ %d  $b$ %d'%(pa,pb),'encre','s')
    disc(ax,x+9.5,13,3.2,'varie' if lit else 'fixe',fill=lit)
    text(ax,x+9.5,6.8,'allumée' if lit else 'éteinte','varie' if lit else 'fixe','s')
save(fig,'80-023')
