import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,18,79,r'$H$','sujet','l',weight='bold')
text(ax,66,79,r'image : $HN/N$','resultat','m',weight='bold')
text(ax,42,79,r"$\nu'$",'varie','l')
for i,(a,b,ra,rb) in enumerate([('0','{0, 6}','autre','autre'),('4','{4, 10}','sujet','resultat'),('8','{2, 8}','sujet','resultat')]):
    y=60-i*14
    box(ax,8,y,20,9,ra,label=a); box(ax,52,y,28,9,rb,label=b)
    arrow(ax,(28,y+4.5),(52,y+4.5),'varie')
text(ax,24,26,r'noyau : $H\cap N=\{0\}$','autre','s')
text(ax,44,19,'théorème fondamental','fixe','s')
box(ax,6,4,76,10,'resultat',label=r'$H/(H\cap N)\ \cong\ HN/N$')
save(fig,'48-116')
