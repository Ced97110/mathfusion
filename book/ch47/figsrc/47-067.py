import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
cx=[14,44,74]
for x,lab,r,t in zip(cx,[r'$g$',r'$g\cdot1$',r'$g\in gH$'],['sujet','varie','resultat'],['départ','étape clé','arrivée']):
    box(ax,x-11,58,22,12,r,label=lab); text(ax,x,75,t,r,'s')
arrow(ax,(25.5,64),(32.5,64),'fixe'); arrow(ax,(55.5,64),(62.5,64),'fixe')
text(ax,44,51,r'$1\in H$','varie','m')
text(ax,44,43,r'$4=4+0$','fixe','m')
text(ax,44,31,'sans 0 dans H','limite','s')
box(ax,3,14,26,10,'limite',label='3, 6, 9'); box(ax,59,14,26,10,'limite',label='7, 10, 1')
arrow(ax,(30,19),(58,19),'limite'); text(ax,44,10,'4 absent','limite','s')
save(fig,'47-067')
