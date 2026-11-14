import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,44,76,r'$(6n+40)-(4n+70)=2n-30$','encre','s')
k=0.3
for yb,n,p1,p2,d in [(56,'10',100,110,r'$2\times10-30=-10$'),(26,'25',190,170,r'$2\times25-30=20$')]:
    text(ax,9,yb+5.5,rf'$n={n}$','encre','s')
    box(ax,18,yb+6,p1*k,5,'sujet',label=f'salle 1 : {p1}',size='s')
    box(ax,18,yb,p2*k,5,'autre',label=f'salle 2 : {p2}',size='s')
    text(ax,18,yb-4,d,'resultat','s',ha='left')
save(fig,'15-111')
