import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
items=[(r'$x^2+(x+1)^2=4$','sujet'),(r'$2x^2+2x-3=0$','varie'),(r'$\Delta=2^2-4\cdot2\cdot(-3)=28$','fixe'),(r'$x=\frac{-1\pm\sqrt{7}}{2}$','varie'),(r'$x\in\mathbb{Q}(\sqrt{7})$','resultat')]
notes=['développer','discriminant','résoudre','une seule racine : √7']
ys=[84-18*i for i in range(5)]
for (l,r),y in zip(items,ys):
    box(ax,8,y,72,12,r,label=l)
for i in range(4):
    arrow(ax,(30,ys[i]),(30,ys[i+1]+12),'fixe')
    text(ax,34,ys[i]-3,notes[i],'fixe','s',ha='left')
save(fig,'61-178')
