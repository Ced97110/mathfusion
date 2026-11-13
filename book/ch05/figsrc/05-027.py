import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,59,'$a$ : n’importe quel entier','sujet','m')
y=44
f=numberline(ax,8,76,y,-30,45,step=5,labels=False,arrow_right=False)
text(ax,f(0),y-3.6,'0','fixe','s')
for v in (-23,23,41):
    disc(ax,f(v),y,1.8,'sujet'); text(ax,f(v),51,rf'$a={v}$'.replace('=-','=-'),'sujet','s')
box(ax,6,20,11,10,'sujet',label=r'$a$',size='l'); text(ax,21,25,'=','encre','l')
box(ax,25,20,30,10,'fixe',label=r'$b\times q+r$')
text(ax,3,14,'nombre de départ','sujet','s',ha='left'); text(ax,40,14,'reconstruit $a$','fixe','s')
save(fig,'05-027')
