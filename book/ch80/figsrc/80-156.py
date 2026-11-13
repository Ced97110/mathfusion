import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,20,74,r'parties de $S$','sujet','m'); text(ax,68,74,'nombres','autre','m')
for y,l,r in ((52,r'$\emptyset$','0'),(32,r'$S$','1')):
    box(ax,8,y,24,11,'sujet',label=l); box(ax,56,y,24,11,'autre',label=r)
    arrow(ax,(33,y+5.5),(55,y+5.5),'varie'); text(ax,44,y+9.5,r'$\varphi$','varie','m')
box(ax,3,14,82,9,'resultat',label=r'$\varphi(a\vee b)=\varphi(a)\vee\varphi(b)$',size='s')
box(ax,3,2,82,9,'resultat',label=r'$\varphi(a\wedge b)=\varphi(a)\wedge\varphi(b)$',size='s')
save(fig,'80-156')
