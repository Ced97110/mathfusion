import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
cw=9.5; x0=6
for i in range(8):
    box(ax,x0+i*cw,38,cw,8,'sujet' if i%2==1 else 'fixe',label=str(i),size='s')
    box(ax,x0+i*cw,26,cw,8,'autre' if i%4==0 else 'fixe',label=str(i) if i%4==0 else None,size='s')
text(ax,x0,50,'reste 1 par 2 : impairs','sujet','s',ha='left')
text(ax,x0,22,'reste 0 par 4 : multiples de 4','autre','s',ha='left')
box(ax,x0,4,8*cw,10,'limite',label='aucun nombre dans les deux',size='s')
save(fig,'52-195')
