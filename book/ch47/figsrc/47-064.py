import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
names=[r'$1$',r'$(1\,2)$',r'$(1\,3)$',r'$(2\,3)$',r'$(1\,2\,3)$',r'$(1\,3\,2)$']
L=['sujet','sujet','varie','autre','varie','autre']; R=['sujet','sujet','resultat','autre','autre','resultat']
text(ax,22,74,'classes à gauche','encre','m'); text(ax,66,74,'classes à droite','encre','m')
for i,n in enumerate(names):
    y=64-9.5*i
    box(ax,6,y-3.75,32,7.5,L[i],label=n,size='s'); box(ax,50,y-3.75,32,7.5,R[i],label=n,size='s')
arrow(ax,(39,64-19),(49,64-19),'limite')
save(fig,'47-064')
