import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'même démarche, deux fois','encre','m')
for x,s,r in ((3,r'$\mathbb{N}$','sujet'),(37,r'$\mathbb{Z}$','sujet'),(71,r'$\mathbb{Q}$','resultat')):
    box(ax,x,30,14,12,r,label=s,size='l')
for xa,bad,fix,lab in ((17,r'$3+x=1$ ?',r'$x=-2$','ajouter les négatifs'),(51,r'$3\times x=2$ ?',r'$x=\frac{2}{3}$','ajouter les fractions')):
    arrow(ax,(xa,36),(xa+20,36),'varie')
    text(ax,xa+10,46,bad,'limite','s'); text(ax,xa+10,28,fix,'varie','s'); text(ax,xa+10,20,lab,'varie','s')
save(fig,'44-282')
