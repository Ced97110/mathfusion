import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
for i in range(3):
    for j in range(4): box(ax,8+4*i,30+4*j,4,4,'sujet',r=0.3,lw=0.5)
text(ax,14,50,r'$d$ $\times$ $q$ = 12','sujet','m')
brace(ax,8,20,29,'fixe',label=r'$d$')
text(ax,4.5,38,r'$q$','fixe','s')
arrow(ax,(24,38),(34,38),'varie')
text(ax,29,42,r'$d$ = 0','varie','s')
for x,top,l in ((42,34,r'$q$ = 5'),(58,50,r'$q$ = 100'),(74,66,r'$q$ = 1 000')):
    line(ax,[(x,24),(x,top)],'limite',lw=1.6)
    text(ax,x,top+(7 if top==66 else 3),l,'limite','s')
    text(ax,x,20,'0 carreau','limite','s')
line(ax,[(74,66),(74,70)],'limite',lw=1.6,dash=True)
text(ax,40,76,'largeur 0 = un trait','limite','s')
box(ax,4,3,80,11,'resultat',label='aucune hauteur ne donne 12',size='m')
save(fig,'03-105')
