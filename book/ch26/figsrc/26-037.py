import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
w_,h_=24,12; xs=[2,32,62]; y=22
box(ax,xs[0],y,w_,h_,'sujet',label=r'$\sin A=0{,}6$')
box(ax,xs[1],y,w_,h_,'sujet',label=r'$\cos A=0{,}8$')
box(ax,xs[2],y,w_,h_,'resultat',label=r'$\tan A=0{,}75$')
text(ax,xs[0]+w_+3,y+h_/2,r'$\div$','varie','l')
text(ax,xs[1]+w_+3,y+h_/2,r'$=$','varie','l')
text(ax,xs[0]+w_/2,y+h_+3,'d’abord','sujet','s')
text(ax,xs[1]+w_/2,y+h_+3,'ensuite','sujet','s')
text(ax,xs[2]+w_/2,y+h_+3,'enfin','resultat','s')
text(ax,44,8,r'$\frac{3}{4}=0{,}75$ : côté opposé $\div$ adjacent','resultat','s')
save(fig,'26-037')
