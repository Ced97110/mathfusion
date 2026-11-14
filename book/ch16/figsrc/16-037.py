import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,18,50,52,12,'sujet',label=r'$2\times x=10$',size='l')
for cx,v,res,role,tag in [(22,'5',r'$2\times5=10$','resultat','vrai'),(66,'4',r'$2\times4=8$','limite','faux')]:
    arrow(ax,(cx,50),(cx,40),'varie')
    box(ax,cx-11,28,22,11,'varie',label=r'$x=%s$'%v,size='m')
    arrow(ax,(cx,28),(cx,19),'varie')
    box(ax,cx-17,7,34,11,role,label=res,size='m')
    text(ax,cx,2,tag,role,'s')
save(fig,'16-037')
