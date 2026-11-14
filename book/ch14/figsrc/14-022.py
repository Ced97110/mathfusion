import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
box(ax,6,68,26,10,'sujet',fill=True,dash=True,label=r'$a \times a$')
box(ax,44,68,38,10,'varie',fill=True,dash=True,label=r'$a \times a \times a$')
text(ax,38,73,r'$\times$')
text(ax,19,83,r'$a^2$','sujet','l'); text(ax,63,83,r'$a^3$','varie','l')
arrow(ax,(44,66),(44,50),'encre')
text(ax,48,58,'on retire les parenthèses','encre','s',ha='left')
roles=['sujet']*2+['varie']*3
for i,r in enumerate(roles): box(ax,20+10*i,40,8,8,r,label='$a$')
brace(ax,20,68,40,'resultat',label='5 facteurs')
arrow(ax,(44,33),(44,21),'resultat')
box(ax,34,8,20,12,'resultat',label=r'$a^5$',size='l')
save(fig,'14-022')
