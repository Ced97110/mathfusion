import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
items=[(r'\sin A',r'\frac{5}{13}','sujet'),(r'\cos A',r'\frac{12}{13}','sujet'),(r'\sin B',r'\frac{3}{5}','varie'),(r'\cos B',r'\frac{4}{5}','varie')]
w,g=19,2.6
for i,(n,v,role) in enumerate(items):
    x=3+i*(w+g)
    box(ax,x,36,w,15,role,label='$'+n+'$\n$'+v+'$')
text(ax,44,57,'prémisses : 4 nombres connus','encre','s')
box(ax,14,16,60,11,'fixe',label=r'$\frac{5}{13}\times\frac{4}{5}+\frac{12}{13}\times\frac{3}{5}$')
for i in range(4):
    x=3+i*(w+g)+w/2
    arrow(ax,(x,36),(44+(i-1.5)*8,27.6),'fixe',lw=0.7)
text(ax,76.5,31.5,'2 produits','fixe','s',ha='left') if False else None
box(ax,14,0.5,60,10,'resultat',label=r'$\sin(A+B)=\frac{56}{65}$')
arrow(ax,(44,16),(44,10.6),'varie')
text(ax,62,13.3,'on additionne','varie','s')
save(fig,'34-035')
