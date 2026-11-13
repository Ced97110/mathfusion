import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
f=lambda n: 8+14*n
line(ax,[(4,46),(f(5)+4,46)],'fixe'); line(ax,[(4,16),(f(5)+4,16)],'fixe')
hi={2:'sujet',3:'varie',5:'resultat'}
for n in range(6):
    r=hi.get(n,'fixe')
    disc(ax,f(n),46,1.9,r); text(ax,f(n),51,str(n),r,"s")
    disc(ax,f(n),16,1.9,r)
    arrow(ax,(f(n),43.2),(f(n),19),r,lw=1.0 if n in hi else 0.6)
for n,l in [(2,r'$4\pi$'),(3,r'$6\pi$'),(5,r'$10\pi$')]:
    text(ax,f(n),11.5,l,hi[n],'s')
text(ax,4,60,r'$n\in\mathbb{Z}$','encre','s',ha='left')
text(ax,84,60,'2 + 3 = 5','resultat','s',ha='right')
text(ax,4,4,r'$n\mapsto 2\pi n$ : le noyau','encre','s',ha='left')
text(ax,84,4,r'$4\pi+6\pi=10\pi$','resultat','s',ha='right')
save(fig,'48-153')
