import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,16,52,r'tableau $A$','sujet','s'); text(ax,42,52,'point','autre','s'); text(ax,70,52,'image','resultat','s')
for i,r in enumerate([['3','1'],['5','2']]):
    for j,v in enumerate(r): box(ax,4+j*12,32-i*14,11,11,'sujet',label=v)
for i,v in enumerate(['2','1']): box(ax,34,32-i*14,11,11,'autre',label=v)
text(ax,28.5,31,'×','encre','l'); 
for i,(s) in enumerate([r'$3\times2+1\times1=7$',r'$5\times2+2\times1=12$']):
    box(ax,50,32-i*14,36,11,'resultat',label=s,size='s')
    arrow(ax,(46,37.5-i*14),(49.2,37.5-i*14),'varie')
text(ax,44,8,r'1re ligne : 1re coordonnée','varie','s'); text(ax,44,3.5,'2e ligne : 2e coordonnée','varie','s') 
save(fig,'42-253')
