import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,46,r'norme $a^2-2b^2$','varie')
text(ax,44,22,r'trace $2a$','varie')
for y,a,b,c in [(34,r'$2\sqrt{2}$',r'$0^2-2\times2^2$',r'$-8$'),(10,r'$2+2\sqrt{2}$',r'$2\times2$',r'$4$')]:
    box(ax,4,y-6,26,12,'sujet',label=a); box(ax,36,y-6,26,12,'varie',label=b); box(ax,68,y-6,16,12,'resultat',label=c)
    arrow(ax,(30,y),(36,y),'varie'); arrow(ax,(62,y),(68,y),'varie')
save(fig,'77-112')
