import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(94)
def row(y,items,x0):
    for i,(s,r) in enumerate(items): box(ax,x0+10*i,y,9,9,r,label=s)
Y1,Y2,Y3=82,56,30
row(Y1,[('x','sujet'),('y','sujet')],20.5)
row(Y1,[(r'$y^{-1}$','autre'),(r'$x^{-1}$','autre')],57.5)
arrow(ax,(30,Y1-3),(39,Y2+12),'varie',lw=1.3); arrow(ax,(77,Y1-3),(68,Y2+12),'varie',lw=1.3)
text(ax,53.5,Y1-5,'à la suite','varie','s')
row(Y2,[('x','sujet'),('y','sujet'),(r'$y^{-1}$','autre'),(r'$x^{-1}$','autre')],33.5)
line(ax,[(53,Y2-1.5),(53,Y2+11)],'varie',lw=1.2,dash=True)
text(ax,53,Y2+14,'jonction','varie','s')
arrow(ax,(53,Y2-3),(53,Y3+13),'varie',lw=1.3); text(ax,58,Y3+17,'effacer','varie','s',ha='left')
row(Y3,[('x','sujet'),(r'$x^{-1}$','autre')],43.5)
arrow(ax,(53,Y3-3),(53,16),'varie',lw=1.3)
box(ax,43,3,20,9,'resultat',label='mot vide',dash=True)
save(fig,'49-053')
