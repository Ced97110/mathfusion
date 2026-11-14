import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
k=80/97.5; x0=4; y0=30; hb=9
a,b,c=30*k,54*k,13.5*k
box(ax,x0,y0,a,hb,'sujet',label='30',r=0.4)
box(ax,x0+a,y0,b,hb,'varie',label='54',r=0.4)
box(ax,x0+a+b,y0,c,hb,'fixe',label='13,5',r=0.4)
brace(ax,x0,x0+80,y0+hb+1,'fixe',label=r'$\frac{1}{2}rp=97{,}5$',down=False)
text(ax,x0+a/2,y0-5,r'$\frac{30}{97{,}5}\approx0{,}3077$','sujet','s')
text(ax,x0+a/2,y0-12,r'$\sin A\cos B$','sujet','s')
text(ax,x0+a+b/2,y0-5,r'$\frac{54}{97{,}5}\approx0{,}5538$','varie','s')
text(ax,x0+a+b/2,y0-12,r'$\cos A\sin B$','varie','s')
box(ax,4,2,80,10,'resultat',label=r'$0{,}3077+0{,}5538=0{,}8615=\sin(A+B)$',size='s')
save(fig,'34-044')
