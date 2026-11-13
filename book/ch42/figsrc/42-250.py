import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
def table(x0,top,bot,role,name):
    for i,(a,b) in enumerate(zip(top,bot)):
        box(ax,x0+i*10,28,9,9,'fixe',label=a); box(ax,x0+i*10,18,9,9,role,label=b)
    text(ax,x0+14.5,45,name,role,'l')
table(4,'123','231','sujet',r'$\pi$'); table(54,'123','312','resultat',r'$\pi^{-1}$')
arrow(ax,(37,28),(52,28),'varie')
text(ax,44.5,36,'échanger','varie','s'); text(ax,44.5,21,'et ranger','varie','s')
text(ax,44,6,'encore une permutation','resultat','s')
save(fig,'42-250')
