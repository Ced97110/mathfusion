import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,30.5,44,r'$a^2$','sujet','m'); text(ax,45,44,'milieu','fixe','s'); text(ax,59.5,44,r'$-b^2$','autre','m'); text(ax,77,44,r'$(a+b)(a-b)$','resultat','s')
rows=[(26,r'$a=5,\ b=2$','25','− 4','21 = 7 × 3'),(10,r'$a=10,\ b=1$','100','− 1','99 = 11 × 9')]
for y,lab,p,q,res in rows:
    text(ax,11,y+5,lab,'encre','s')
    box(ax,24,y,13,10,'sujet',label=p); box(ax,38.5,y,13,10,'fixe',fill=False,dash=True,label='aucun',size='s')
    box(ax,53,y,13,10,'autre',label=q); box(ax,68,y,18,10,'resultat',label=res,size='s')
save(fig,'15-106')
