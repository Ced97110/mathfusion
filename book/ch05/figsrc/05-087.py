import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cx=lambda i: 10+11*i
text(ax,2,56,'diviseurs de 0 : tous les nombres','autre','s',ha='left')
for i in range(6): box(ax,cx(i)-4.5,40,9,9,'autre',label=str(i+1),size='m')
text(ax,cx(6),44.5,'…','autre','l')
for i,v in enumerate([1,2,3,4,5,6]):
    if v in (1,2,3,6):
        line(ax,[(cx(i),39.5),(cx(i),28.5)],'fixe',dash=True)
        box(ax,cx(i)-4.5,19,9,9,'resultat' if v==6 else 'sujet',label=str(v),size='m',lw=1.6 if v==6 else 0.8)
text(ax,2,14.5,'diviseurs communs de 6 et 0','sujet','s',ha='left')
text(ax,44,6,'PGCD(6, 0) = 6','resultat','l',weight='bold')
save(fig,'05-087')
