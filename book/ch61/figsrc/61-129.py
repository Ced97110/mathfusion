import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
rows=[('sujet',r'$u^3=1+\sqrt{2}$'),('varie',r'$u^3-1=\sqrt{2}$'),('varie',r'$(u^3-1)^2=2$'),('resultat',r'$u^6-2u^3-1=0$')]
for i,(r,l) in enumerate(rows):
    y=62-i*20; box(ax,2,y,44,12,r,label=l,size='s')
    if i<3: arrow(ax,(24,y),(24,y-8),'fixe')
box(ax,58,60,28,12,'sujet',label=r'$u$',size='m')
box(ax,58,32,28,12,'sujet',label=r'$K=\mathbb{Q}(\sqrt{2})$',size='s')
box(ax,58,4,28,12,'fixe',label=r'$\mathbb{Q}$',size='m')
arrow(ax,(72,60),(72,44),'fixe',both=True); text(ax,81,52,r'$\leq 3$','varie','s')
arrow(ax,(72,32),(72,16),'fixe',both=True); text(ax,81,24,'2','varie','s')
text(ax,66,77,r'$3\times2=6$','resultat','m') if False else None
save(fig,'61-129')
