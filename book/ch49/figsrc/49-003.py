import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[4,36,68]
for k,x in enumerate(xs):
    poly(ax,[(x,38),(x+16,38),(x+16,54),(x,54)],'fixe')
    line(ax,[(x+8,36),(x+8,56)],'fixe',dash=True)
    cx=x+3.5 if k!=1 else x+12.5
    disc(ax,cx,50.5,2.4,'sujet',label='1' if k==0 else None,size='s')
arrow(ax,(23,46),(33,46),'varie'); text(ax,28,50,r'$s$','varie','m')
arrow(ax,(55,46),(65,46),'varie'); text(ax,60,50,r'$s$','varie','m')
f=numberline(ax,10,70,16,1,7,arrow_right=False)
for v in range(1,8):
    disc(ax,f(v),23,2.4,'resultat' if v%2==0 else 'varie')
text(ax,44,5,'nombre de $s$','encre','s')
text(ax,22,31,'pair : carré en place','resultat','s')
text(ax,66,31,'impair : retourné','varie','s')
save(fig,'49-003')
