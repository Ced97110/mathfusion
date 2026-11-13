import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
rows=[(60,r'$3/4$',r'$0$','sujet','fixe'),(44,r'$5/2$',r'$0$','sujet','fixe'),(28,r'$?$',r'$3/4$','limite','sujet')]
for y,a,b,ra,rb in rows:
    box(ax,8,y,16,10,ra,label=a,dash=(a==r'$?$'))
    arrow(ax,(26,y+5),(52,y+5),'varie'); text(ax,39,y+9,r'$\times 0$','varie','s')
    box(ax,54,y,16,10,rb,label=b)
line(ax,[(54,28),(70,38)],'limite',lw=1.4); line(ax,[(54,38),(70,28)],'limite',lw=1.4)
text(ax,44,14,r'aucun nombre ne donne $3/4$','limite','m')
save(fig,'06-078')
