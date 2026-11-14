import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,r'$Q(s_1u_1+s_2u_2)$','encre','l')
xs=[4.5+21*i for i in range(4)]
labs=[r'$2s_1^2$',r'$0\cdot s_1s_2$',r'$0\cdot s_2s_1$',r'$2s_2^2$']
roles=['sujet','limite','limite','sujet']
for i in range(4):
    box(ax,xs[i],28,16,12,roles[i],label=labs[i],dash=(i in (1,2)))
    if i<3: text(ax,xs[i]+18.5,34,'+','encre','l')
brace(ax,xs[1],xs[2]+16,26,'limite',label='termes croisés : 0')
box(ax,22,2,44,10,'resultat',label=r'$Q=2s_1^2+2s_2^2$',weight='bold')
arrow(ax,(xs[0]+8,28),(28,12),'sujet'); arrow(ax,(xs[3]+8,28),(60,12),'sujet')
save(fig,'71-151')
