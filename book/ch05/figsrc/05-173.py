import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
x0,x1=6,70
f=numberline(ax,x0,x1,34,0,10,every=5)
for n in range(5): disc(ax,f(n),34,1.9,'resultat')
disc(ax,f(5),34,1.9,'limite')
text(ax,f(5),43,'n = 5 : faux','limite','s')
text(ax,84,34,r'$n$','fixe','m')
brace(ax,f(0)-2,f(4)+2,27,'resultat','5 cas vérifiés')
brace(ax,f(0)-2,x1+5,17,'sujet','un raisonnement couvre tout')
save(fig,'05-173')
