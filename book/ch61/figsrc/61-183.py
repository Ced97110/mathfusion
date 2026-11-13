import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
for k in range(1,9):
    ok=(k&(k-1))==0
    box(ax,44,6+(k-1)*9,12,8,'resultat' if ok else 'limite',label=str(k),size='m')
def row(k): return 6+(k-1)*9+4
text(ax,58,row(2),r'$\sqrt{2}$','encre','s',ha='left')
text(ax,58,row(4),r'$\sqrt{2}+\sqrt{3}$','encre','s',ha='left')
text(ax,58,row(3),r'$\sqrt[3]{2}$ et $\cos 20°$','encre','s',ha='left')
box(ax,3,68,5,5,'resultat'); text(ax,10,70.5,'puissance de 2','resultat','s',ha='left')
box(ax,3,58,5,5,'limite'); text(ax,10,60.5,'pas une puissance de 2','limite','s',ha='left')
save(fig,'61-183')
