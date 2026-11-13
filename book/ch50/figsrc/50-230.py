import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
box(ax,2,38,84,12,'varie',label="48 éléments d'ordre 7")
for i in range(8):
    box(ax,4+10*i,18,9.4,8,'sujet',r=0.4,lw=0.6)
box(ax,2,15,84,14,'resultat',fill=False,dash=True)
arrow(ax,(22,37.5),(22,30.5),'limite')
text(ax,26,34,"aucun n'y entre",'limite','s',ha='left')
text(ax,44,9,'les 8 restants = le 2-Sylow','resultat','s')
text(ax,44,3.5,r'$n_2 = 1$','resultat','l')
save(fig,'50-230')
