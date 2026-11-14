import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,r'$p=7$ premier','sujet','l')
text(ax,22,50,'classe','sujet','s'); text(ax,66,50,'inverse','resultat','s')
text(ax,44,50,r'$a\times b=\bar1$','varie','s')
for i,(a,b) in enumerate([(1,1),(2,4),(3,5),(6,6)]):
    y=34-i*10
    box(ax,12,y,20,8,'sujet',label=rf'$\bar{a}$',size='m')
    box(ax,56,y,20,8,'resultat',label=rf'$\bar{b}$',size='m')
    arrow(ax,(33,y+4),(55,y+4),'varie',both=True)
save(fig,'52-082')
