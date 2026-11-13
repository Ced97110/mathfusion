import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,23,58,'neutre pour la réunion','sujet','s'); text(ax,65,58,"absorbant pour l'inter",'varie','s')
box(ax,3,40,38,10,'sujet',label=r'$5+0=5$'); box(ax,47,40,38,10,'varie',label=r'$5\times0=0$')
def row(c,role,op,res,y=14):
    box(ax,c,y-6,9,12,role,label='A'); text(ax,c+12,y,op,'encre','l')
    box(ax,c+16,y-6,8,12,'fixe',fill=False,dash=True)
    text(ax,c+28,y,'=','encre','l')
    if res: box(ax,c+31,y-6,9,12,role,label='A')
    else: box(ax,c+31,y-6,8,12,'fixe',fill=False,dash=True)
row(2,'sujet',r'$\cup$',True); row(46,'varie',r'$\cap$',False)
text(ax,44,30,r'pointillé : $\emptyset$, rien dedans','fixe','s')
save(fig,'42-152')
