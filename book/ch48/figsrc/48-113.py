import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,18,56,r'$H/(H\cap N)$','sujet','m',weight='bold')
text(ax,69,56,r'$HN/N$','resultat','m',weight='bold')
text(ax,43,56,r'$\cong$','resultat','l')
for i,(a,b) in enumerate([('0','{0, 6}'),('4','{4, 10}'),('8','{2, 8}')]):
    y=38-i*14
    box(ax,8,y,20,9,'sujet',label=a)
    box(ax,56,y,26,9,'resultat',label=b)
    arrow(ax,(28,y+4.5),(56,y+4.5),'varie')
text(ax,42,47,r"$h\mapsto hN$",'varie','s')
save(fig,'48-113')
