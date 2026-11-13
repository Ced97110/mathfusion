import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
text(ax,44,82,r'$n=60=p_1\times p_2\times\cdots\times p_s$','sujet','l')
w=14; g=7.5; xs=[4.75+(w+g)*i for i in range(4)]
tops=[r'$p_1$',r'$p_2$',r'$\cdots$',r'$p_s$']; vals=['2','2','3','5']
for i,x in enumerate(xs):
    if i==2: box(ax,x,58,w,11,'fixe',label=tops[i],dash=True)
    else: box(ax,x,58,w,11,'sujet',label=tops[i])
    box(ax,x,26,w,11,'autre',label=vals[i],weight='bold')
    arrow(ax,(x+w/2,57.5),(x+w/2,37.5),'varie' if i!=2 else 'fixe')
    if i<3: text(ax,x+w+g/2,63.5,r'$\times$','sujet','m')
brace(ax,xs[0],xs[3]+w,24,'autre',label=r'$s=4$ facteurs')
text(ax,44,8,r'$p_2$ : 2e facteur, pas $p^2$','limite','m')
save(fig,'05-122')
