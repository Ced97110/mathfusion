import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
labs=[-3,-2,-1,0,1,2,3]; w,g=8,1.2; x0=(88-(7*w+6*g))/2
for i,v in enumerate(labs):
    box(ax,x0+i*(w+g),24,w,9,'varie' if v<0 else 'sujet',label=(f'$-{-v}$' if v<0 else str(v)))
text(ax,x0-5,28.5,r'$\cdots$','fixe','l'); text(ax,x0+7*w+6*g+5,28.5,r'$\cdots$','fixe','l')
brace(ax,x0,x0+3*w+2*g,35,'varie',label='opposés ajoutés',down=False)
brace(ax,x0+3*(w+g),x0+7*w+6*g,35,'sujet',label=r'$\mathbb{N}$',down=False)
brace(ax,x0,x0+7*w+6*g,22,'resultat',label=r'$\mathbb{Z}=\mathbb{N}$ + opposés')
text(ax,44,6,r'chaque $n$ reçoit son opposé $-n$','encre','s')
save(fig,'44-262')
