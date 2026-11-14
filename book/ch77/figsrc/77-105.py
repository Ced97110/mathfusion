import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
c=9
for i in range(4):
    for j in range(4):
        d=(i//2==j//2); box(ax,8+j*c,16+(3-i)*c,c,c,'sujet' if d else 'fixe',r=0.4)
box(ax,8,34,18,18,'sujet',fill=False,lw=1.6); box(ax,26,16,18,18,'sujet',fill=False,lw=1.6)
text(ax,17,43,'trace 2','sujet','s'); text(ax,35,25,'trace 2','sujet','s')
text(ax,26,9,r'$4\times4$ en blocs $2\times2$','fixe','s')
text(ax,66,46,r'$T_{L/K}(u)$','sujet'); text(ax,66,34,r'$2+2=4$','resultat','l')
arrow(ax,(46,34),(54,34),'varie')
save(fig,'77-105')
