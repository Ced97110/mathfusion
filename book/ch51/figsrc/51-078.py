import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,24,60,'formule','fixe','s'); text(ax,68,60,'au point 0','fixe','s')
rows=[(r'$f(x)=x^2$',r'$0$','sujet'),(r'$g(x)=\cos x$',r'$1$','varie'),(r'$(f+g)(x)=x^2+\cos x$',r'$0+1=1$','resultat'),(r'$(fg)(x)=x^2\cos x$',r'$0\times1=0$','resultat')]
for i,(f,v,role) in enumerate(rows):
    y=44-i*14
    box(ax,3,y,52,11,role,label=f,size='s'); box(ax,59,y,26,11,role,label=v,size='m')
    arrow(ax,(55.5,y+5.5),(58.5,y+5.5),role,lw=0.8)
save(fig,'51-078')
