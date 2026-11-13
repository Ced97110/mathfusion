import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
u=2.5
line(ax,[(4,14),(42,14)],'fixe'); line(ax,[(46,14),(84,14)],'fixe')
text(ax,23,66,r'3 $\times$ 4 : départ 0','encre','m'); text(ax,65,66,r'2$^{3}$ : départ 1','encre','m')
line(ax,[(6,14),(12,14)],'fixe',lw=2.2); text(ax,9,17,'0','fixe','s')
box(ax,48,14,6,1*u,'fixe',r=0.4); text(ax,51,19.5,'1','fixe','s')
for x,h,t in [(15,10,'4'),(24,20,'8')]:
    box(ax,x,14,6,h,'sujet',r=0.8); text(ax,x+3,14+h+3,t,'sujet','s')
for x,h,t in [(57,5,'2'),(66,10,'4')]:
    box(ax,x,14,6,h,'sujet',r=0.8 if h>=10 else 0.4); text(ax,x+3,14+h+3,t,'sujet','s')
box(ax,33,14,6,30,'resultat'); text(ax,36,47,'12','resultat','m')
box(ax,75,14,6,20,'resultat'); text(ax,78,37,'8','resultat','m')
for p,q in [((12,14),(15,24)),((21,24),(24,34)),((30,34),(33,44)),((54,16.5),(57,19)),((63,19),(66,24)),((72,24),(75,34))]:
    arrow(ax,p,q,'varie',curve=0.2)
text(ax,23,57,'ajouter 4, trois fois','varie','s'); text(ax,65,57,'multiplier par 2, 3 fois','varie','s')
text(ax,44,6,"départ puis 3 fois l'action",'encre','s')
save(fig,'01-190')
