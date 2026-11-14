import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
u=12
def frame(o,vs,role,lab):
    line(ax,[(o[0]-14,o[1]),(o[0]+14,o[1])],'fixe',lw=0.5); line(ax,[(o[0],o[1]-4),(o[0],o[1]+16)],'fixe',lw=0.5)
    for (x,y),(dx,dy),l in zip(vs,[(5,0),(0,3.5)] if role=='sujet' else [(5,2),(-5,2)],lab):
        arrow(ax,o,(o[0]+x*u,o[1]+y*u),role,lw=1.3)
        text(ax,o[0]+x*u+dx,o[1]+y*u+dy,l,role,'s')
o1,o2=(20,22),(68,22)
frame(o1,[(1,0),(0,1)],'sujet',[r'$(1,0)$',r'$(0,1)$'])
frame(o2,[(1,1),(-1,1)],'autre',[r'$(1,1)$',r'$(-1,1)$'])
text(ax,20,52,'première base','sujet','m'); text(ax,68,52,'seconde base','autre','m')
text(ax,44,32,'=','resultat','xl')
text(ax,20,10,'2 éléments','sujet','m'); text(ax,68,10,'2 éléments','autre','m')
text(ax,44,10,r'$2=2$','resultat','l')
save(fig,'76-115')
