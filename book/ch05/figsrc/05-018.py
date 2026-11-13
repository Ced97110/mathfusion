import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
R=1.3; DY=3.6; DX=4.4
def cols(x,y,n,role):
    for c in range(n):
        for i in range(3): disc(ax,x+c*DX,y-i*DY,R,role)
box(ax,2,8,41,68,'resultat',fill=False)
box(ax,45,8,41,68,'limite',fill=False)
text(ax,22.5,71,'Les deux : vrai','resultat','m')
text(ax,65.5,71,'Un seul : faux','limite','m')
# gauche, étape 1
cols(8,60,2,'sujet'); cols(22,60,3,'autre')
text(ax,10.2,47,r'$3\mid 6$','sujet','s'); text(ax,26.4,47,r'$3\mid 9$','autre','s')
arrow(ax,(22.5,44),(22.5,39),'varie')
x0=22.5-8.8
cols(x0,34,2,'sujet'); cols(x0+2*DX,34,3,'autre')
text(ax,22.5,22,r'$6+9=15$','encre','m'); text(ax,22.5,17,r'$3\mid 15$','resultat','l')
# droite
cols(52,60,2,'sujet'); cols(66,60,1,'autre')
for i in range(1): disc(ax,66+DX,60,R,'limite')
text(ax,54.2,47,r'$3\mid 6$','sujet','s'); text(ax,68.2,47,r'$3\nmid 4$','limite','s')
arrow(ax,(65.5,44),(65.5,39),'varie')
x1=65.5-6.6
cols(x1,34,2,'sujet'); cols(x1+2*DX,34,1,'autre'); disc(ax,x1+3*DX,34,R,'limite')
text(ax,65.5,22,r'$6+4=10$','encre','m'); text(ax,65.5,17,r'$3\nmid 10$ : reste 1','limite','m')
save(fig,'05-018')
