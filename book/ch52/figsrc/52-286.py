import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'restes par 5 : $x^5-x$','sujet','m')
text(ax,9,44,r'$x$','sujet','m'); text(ax,9,30,r'$x^5-x$','varie','s')
for i,v in enumerate(['0','0','30','240','1 020']):
    x=20+i*12.6
    box(ax,x,40,11,8,'sujet',label=str(i))
    arrow(ax,(x+5.5,40),(x+5.5,37),'varie',lw=0.8)
    box(ax,x,27,11,8,'varie',label=v,size='s')
box(ax,20,8,62,10,'resultat',label='tous multiples de 5 : reste 0')
arrow(ax,(51,27),(51,18),'resultat')
save(fig,'52-286')
