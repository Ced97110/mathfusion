import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$n$ est-il premier ?','encre','m')
box(ax,4,24,18,16,'sujet',label=r'$n$',size='l')
text(ax,13,18,'le nombre étudié','sujet','s')
for y,v,verd,role in [(40,'7','premier','resultat'),(26,'12','pas premier','limite'),(12,'47','premier','resultat')]:
    box(ax,30,y,24,11,'fixe',label=r'$n=%s$'%v,size='m')
    box(ax,58,y,26,11,role,label=verd,size='m')
    arrow(ax,(22,32),(30,y+5.5),'varie')
save(fig,'05-047')
