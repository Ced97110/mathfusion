import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def grid(n,x0,y0,c):
    for i in range(n):
        for j in range(n):
            d=(i==j)
            box(ax,x0+j*c,y0+(n-1-i)*c,c,c,'sujet' if d else 'fixe',label='1' if d else None,r=0.4)
grid(2,6,21,9); grid(4,46,12,9)
text(ax,44,62,r'$T(1)=n$','sujet','l')
text(ax,15,54,r'$\mathbb{C}\ :\ n=2$','encre'); text(ax,64,54,r'$\mathbb{H}\ :\ n=4$','encre')
text(ax,35,30,'gris : 0','fixe','s')
text(ax,15,12,r'$T(1)=2$','resultat'); text(ax,64,6,r'$T(1)=4$','resultat')
save(fig,'77-097')
