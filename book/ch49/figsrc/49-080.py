import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,45,r'$D_n=\langle x,\,y\ |\ x^n,\ y^2,\ xyxy\rangle$','encre','l')
box(ax,3,20,20,12,'sujet',label=r'$x,\ y$',size='l')
line(ax,[(26,18),(26,34)],'encre',lw=1.2)
xs=[29,48,67]; labs=[r'$x^n$',r'$y^2$',r'$xyxy$']
caps=['$x$ répété\n$n$ fois = 1','$y$ deux\nfois = 1','$x,y,x,y$ de\nsuite = 1']
for x,l,c in zip(xs,labs,caps):
    box(ax,x,20,17,12,'fixe',label=l,size='l')
    text(ax,x+8.5,14.5,c,'fixe','s')
text(ax,13,36.5,'deux lettres','sujet','s')
brace(ax,29,84,33,'fixe',label='trois relations',down=False)
text(ax,13,14.5,'avant la barre','sujet','s')
save(fig,'49-080')
