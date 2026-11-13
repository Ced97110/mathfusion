import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
u=4; x0=8
text(ax,44,72,'le segment de 6 mesure les deux','encre','m')
def row(y,n,w,role,lab):
    for i in range(n): box(ax,x0+i*w*u,y,w*u,9,role,label=lab)
text(ax,x0,62,'12 : 2 fois 6','sujet','s',ha='left'); row(51,2,6,'resultat','6')
text(ax,x0,45,'18 : 3 fois 6','autre','s',ha='left'); row(34,3,6,'resultat','6')
line(ax,[(4,28),(84,28)],'fixe',dash=True)
text(ax,x0,23,'essai avec 9 dans 12','limite','s',ha='left')
box(ax,x0,12,9*u,9,'fixe',label='9')
box(ax,x0+9*u,12,3*u,9,'limite',label='reste')
text(ax,x0+9*u+3*u+14,16.5,'9 échoue','limite','s')
save(fig,'05-074')
