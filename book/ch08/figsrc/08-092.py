import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
c=4.0
for i in range(10):
    for j in range(10):
        n=i*10+j
        r='sujet' if n<37 else 'fixe'
        ax.add_patch(Rectangle((4+i*c,10+j*c),c,c,ec='white',fc=FILL[r] if r=='fixe' else COL[r],lw=0.6,zorder=2))
brace(ax,4,44,10,'fixe',label='100 cases')
text(ax,66,44,'37 %','sujet','xl',weight='bold')
text(ax,66,34,'37 sur 100','sujet','m')
text(ax,66,26,'= 37 centièmes','sujet','m')
text(ax,66,16,'= 0,37','resultat','l',weight='bold')
save(fig,'08-092')
