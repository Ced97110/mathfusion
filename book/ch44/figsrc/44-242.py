import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(96)
ys=[80,58,36,14]
L=[r'$b\,a = c\,a$',r'$(b\,a)\,a^{-1} = (c\,a)\,a^{-1}$',r'$b\,(a\,a^{-1}) = c\,(a\,a^{-1})$',r'$b = c$']
R=['sujet','fixe','fixe','resultat']
for y,l,r in zip(ys,L,R): box(ax,3,y,52,10,r,label=l,size='s' if r=='fixe' else 'm')
for i,t in enumerate([r'composer par $a^{-1}$',r'associativité',r'$a\,a^{-1}=1$']):
    arrow(ax,(29,ys[i]),(29,ys[i+1]+10),'varie'); text(ax,59,ys[i]-6,t,'varie','s',ha='left')
save(fig,'44-242')
