import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$|A^*| = q^n - 1$','sujet','l')
w=14;g=3;x0=(88-(4*w+3*g))/2
for k in range(4):
    x=x0+k*(w+g)
    if k==0: box(ax,x,30,w,10,'limite',label='0',dash=True)
    else: box(ax,x,30,w,10,'sujet',label=r'$\neq 0$')
xe=x0+4*w+3*g
brace(ax,x0,xe,41,'fixe',label=r'$q^n=2\times2=4$ éléments',down=False)
brace(ax,x0+w+g,xe,29,'resultat',label='3 éléments non nuls')
text(ax,x0+w/2,25.3,'retiré','limite','s')
box(ax,14,5,60,10,'resultat',label=r'$|A^*| = 2\times2-1 = 3$')
arrow(ax,(44,22),(44,16),'varie')
save(fig,'78-161')
