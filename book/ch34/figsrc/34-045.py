import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
s=2.5
ox,oy=3,12
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'fixe')
text(ax,ox+2.8*s,oy+3*s,'30','sujet','m',weight='bold')
text(ax,ox+7*s,oy-4,'triangle bleu','sujet','s')
box(ax,42,32,44,16,'sujet',label='aire bleue ÷ référence\n'+r'$\frac{30}{97{,}5}\approx0{,}3077$')
text(ax,64,28.5,'=','resultat','xl')
box(ax,42,6,44,18,'sujet',label=r'$\sin A=\frac{5}{13}\approx0{,}3846$'+'\n'+r'$\cos B=0{,}8$'+'\n'+r'$\mathrm{produit}\approx0{,}3077$')
save(fig,'34-045')
