import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def chart(x0,vals,role,title,coord):
    base=36; u=7; w=8
    line(ax,[(x0-2,base),(x0+3*w+1,base)],'fixe',lw=0.7)
    for i,(v,l) in enumerate(zip(vals,[r'$e_{12}$',r'$e_{13}$',r'$e_{23}$'])):
        x=x0+i*(w+1)
        if v>0: poly(ax,[(x,base),(x+w-1,base),(x+w-1,base+v*u),(x,base+v*u)],role)
        elif v<0: poly(ax,[(x,base),(x+w-1,base),(x+w-1,base+v*u),(x,base+v*u)],role)
        else: line(ax,[(x,base),(x+w-1,base)],role,lw=1.6)
        text(ax,x+(w-1)/2,15,l,'fixe','s')
    text(ax,x0+13,54,coord,role,'m'); text(ax,x0+13,60,title,role,'s')
chart(4,[1,0,-1],'sujet','base 1','(1, 0, −1)')
chart(51,[2,0,-2],'autre','base 2','(2, 0, −2)')
arrow(ax,(36,36),(48,36),'varie'); text(ax,42,41,r'$\times\,2$','varie','m')
text(ax,44,6,'même plan, nombres × 2','resultat','m')
save(fig,'76-138')
