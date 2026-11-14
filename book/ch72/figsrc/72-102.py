import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
xs=[4.5,26.5,48.5,70.5]; roles=['sujet','limite','autre','fixe']
names=['carré de x','2 fois B(x,y)','carré de y','carré de x+y']
for x,r,n in zip(xs,roles,names):
    box(ax,x,46,13,11,r,label='0',size='l',dash=(r=='limite')); text(ax,x+6.5,61,n,r,'s')
for x,s in zip((19,41,63),'+ + ='.split()): text(ax,x,51.5,s,'encre','l')
text(ax,33,40,'le terme croisé disparaît','limite','s')
arrow(ax,(33,45),(33,31),'varie')
box(ax,16,19,34,11,'sujet',label=r'$B(x,y)=1$',size='l')
text(ax,33.5+27,24.5,'1 + 1 = 0','varie','m')
text(ax,44,8,'les carrés l’ont perdu','limite','m')
save(fig,'72-102')
