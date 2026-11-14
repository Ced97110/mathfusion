import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
xs=(4,24,44,64)
for i,x in enumerate(xs):
    n=i+1; ok=n<=3
    box(ax,x,52,18,10,'fixe',label=f'$y$ = {n}',size='s')
    arrow(ax,(x+9,52),(x+9,46),'fixe',0.8)
    box(ax,x,34,18,10,'resultat' if ok else 'fixe',label=(r'$\zeta(%d,3)=1$' % n) if ok else r'$\zeta(4,3)=0$',size='s')
    box(ax,x,10,18,10,'resultat' if ok else 'fixe',label=f'$f$({n})' if ok else '0',size='s',dash=not ok)
text(ax,44,27,r'$\zeta(y,3)\,f(y)$ : on garde ou on efface','encre','s')
text(ax,44,3.5,r'$g(3)=f(1)+f(2)+f(3)$','sujet','s')
save(fig,'80-264')
