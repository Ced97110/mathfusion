import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
xs=[14,44,74]
# upper member : (g1 g2) x, one step
text(ax,2,76,r'$(g_1g_2)\,x$','sujet','m',ha='left',weight='bold')
disc(ax,xs[0],62,4,'fixe',label='1'); disc(ax,xs[2],62,4,'resultat',label='3')
arrow(ax,(xs[0]+4.5,62),(xs[2]-4.5,62),'sujet',lw=1.6)
text(ax,44,67,r'$g_1g_2$ : demi-tour','sujet','s')
text(ax,44,49,'$=$','resultat','xl',weight='bold')
# lower member : g1 (g2 x), two steps
text(ax,2,43,r'$g_1(g_2\,x)$','varie','m',ha='left',weight='bold')
y=30
for x,l in zip(xs,'123'): disc(ax,x,y,4,'resultat' if l=='3' else 'fixe',label=l)
for i,g in enumerate([r'$g_2$',r'$g_1$']):
    arrow(ax,(xs[i]+4.5,y),(xs[i+1]-4.5,y),'varie',lw=1.3)
    text(ax,(xs[i]+xs[i+1])/2,y+4.2,f'{i+1}{"er" if i==0 else "e"} : {g}','varie','s')
    text(ax,(xs[i]+xs[i+1])/2,y-5,'quart de tour','varie','s')
text(ax,44,10,"même point d'arrivée : 3",'resultat','m',weight='bold')
save(fig,'49-100')
