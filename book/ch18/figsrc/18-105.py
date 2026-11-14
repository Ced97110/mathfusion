import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,71,r'$4a^4+32a^2b-64b^2$','sujet','l')
rows=[(r'$4a^4$',r'$=(2a^2)^2$','resultat','✓'),(r'$32a^2b$',r'$=2\times2a^2\times8b$','resultat','✓'),(r'$-64b^2$',r'$(8b)^2=64b^2$','limite','✗')]
for k,(a,b,r,m) in enumerate(rows):
    y=52-k*15
    box(ax,2,y-5,22,10,r,label=a,size='m'); text(ax,56,y,b,r,'m'); text(ax,84,y,m,r,'l',weight='bold')
text(ax,44,10,r'$a=b=1$ : $-28$, pas $100$','limite','m')
save(fig,'18-105')
