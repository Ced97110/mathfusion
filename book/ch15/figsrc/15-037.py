import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
text(ax,44,87,r'$x=4$','fixe','l')
cx=[17,44,71]
r1=[r'$3x^2$',r'$-2x$',r'$+1$']; r2=[r'$3\times4^2$',r'$-2\times4$',r'$+1$']; r3=['48',r'$-8$',r'$+1$']
for c,a,b,d in zip(cx,r1,r2,r3):
    box(ax,c-12.5,70,25,10,'sujet',label=a); box(ax,c-12.5,48,25,10,'varie',label=b); box(ax,c-12.5,26,25,10,'resultat',label=d)
    arrow(ax,(c,70),(c,58),'varie'); arrow(ax,(c,48),(c,36),'varie')
arrow(ax,(44,26),(44,16),'resultat')
box(ax,16,4,56,12,'resultat',label=r'$48-8+1=41$',size='l',weight='bold')
save(fig,'15-037')
