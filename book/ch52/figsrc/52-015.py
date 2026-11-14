import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
rows=[('sujet','0','…, −4, 0, 4, 8, …'),('varie','1','…, −3, 1, 5, 9, …'),('resultat','2','…, −6, −2, 2, 6, …'),('autre','3','…, −5, −1, 3, 7, …')]
text(ax,44,63,'chaque entier a un seul reste','encre','s')
for i,(r,k,s) in enumerate(rows):
    y=50-i*13
    box(ax,3,y-5,18,10,r,label=f'reste {k}',size='s',weight='bold')
    box(ax,25,y-5,60,10,r,fill=False,lw=0.6)
    text(ax,55,y,s,r,'m')
save(fig,'52-015')
