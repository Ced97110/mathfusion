import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
def row(y,title,steps,res,role):
    text(ax,44,y+22,title,role,'l')
    f=numberline(ax,8,72,y,0,8,1,labels=True,every=4,arrow_right=False)
    for (a,b) in steps: arrow(ax,(f(a),y+3),(f(b),y+3),role,lw=1.2,curve=0.5)
    disc(ax,f(res),y,1.4,role)
    return f
f=row(46,r'$(8-4)-2$',[(8,4),(4,2)],2,'sujet')
text(ax,f(2),55,'2','sujet','m')
f=row(12,r'$8-(4-2)$',[(8,6)],6,'varie')
text(ax,f(6),21,'6','varie','m')
text(ax,44,72,r'$2\neq 6$','limite','l')
save(fig,'76-144')
