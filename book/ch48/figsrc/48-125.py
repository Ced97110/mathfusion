import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,15,51,r'$HN/N$','resultat','m',weight='bold'); text(ax,15,25,r'$H/(H\cap N)$','sujet','m',weight='bold')
text(ax,15,38,r'$\cong$','resultat','l')
top=['0 4 8','3 7 11','2 6 10','1 5 9']; bot=['0','3','6','9']
for i in range(4):
    x=30+i*14
    box(ax,x,46,12,10,'resultat',label=top[i],size='s'); box(ax,x,20,12,10,'sujet',label=bot[i],size='s'); line(ax,[(x+6,46),(x+6,30)],'fixe')
text(ax,57,60,r'$12\div3=4$','resultat','s'); text(ax,57,14,r'$4\div1=4$','sujet','s')
save(fig,'48-125')
