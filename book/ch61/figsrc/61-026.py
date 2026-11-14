import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
labs=[('fixe',r'$a$'),('sujet',r'$b\sqrt{2}$'),('autre',r'$c\sqrt{3}$'),('resultat',r'$d\sqrt{6}$')]
for i,(role,lab) in enumerate(labs):
    x=2+i*22; box(ax,x,32,17,14,role,label=lab,size='l')
    if i: text(ax,x-2.5,39,'+','encre','m')
text(ax,44,50,'quatre morceaux','encre','s')
box(ax,17,6,34,12,'encre',label=r'$\sqrt{2}\times\sqrt{3}=\sqrt{6}$',size='s')
arrow(ax,(51,12),(71,31),'varie',curve=0.25)
arrow(ax,(23,19),(25,31),'sujet') if False else None
save(fig,'61-026')
