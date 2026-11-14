import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
c=15; x0=6; y0=40
text(ax,4,y0+2*c+9,'matrice de colonnes $x$ et $y$','encre','s',ha='left')
text(ax,x0+c/2,y0+2*c+3,r'$x$','sujet','m'); text(ax,x0+c*1.5,y0+2*c+3,r'$y$','varie','m')
box(ax,x0,y0,c,2*c,'sujet'); box(ax,x0+c,y0,c,2*c,'varie')
pos={'a':(x0+c/2,y0+c*1.5),'b':(x0+c/2,y0+c*0.5),'c':(x0+c*1.5,y0+c*1.5),'d':(x0+c*1.5,y0+c*0.5)}
for k,s,r in (('a','3','sujet'),('b','1','sujet'),('c','1','varie'),('d','2','varie')): text(ax,*pos[k],s,r,'l')
off=3.2
line(ax,[(pos['a'][0]+off,pos['a'][1]-off+1),(pos['d'][0]-off,pos['d'][1]+off-1)],'resultat',lw=1.2)
line(ax,[(pos['b'][0]+off,pos['b'][1]+off-1),(pos['c'][0]-off,pos['c'][1]-off+1)],'varie',lw=1.2)
text(ax,62,y0+c*1.6,r'$x_1y_2=3\times2=6$','resultat','s'); text(ax,62,y0+c*0.5,r'$x_2y_1=1\times1=1$','varie','s')
box(ax,4,4,80,26,'resultat')
text(ax,44,24,'$B(x,y)$ = déterminant de $(x\\ y)$','resultat','m')
text(ax,44,16,r'$=x_1y_2-x_2y_1$','resultat','m'); text(ax,44,9,r'$=6-1=5$','resultat','m')
save(fig,'71-088')
