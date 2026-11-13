import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
bx=[25,39,53]; roles=['sujet','varie','autre']; heads=[r'$a^2$',r'$2ab$',r'$b^2$']
for x,r,h in zip(bx,roles,heads): text(ax,x+6.5,44,h,r,'m')
text(ax,77,44,r'$(a+b)^2$','resultat','s')
rows=[(26,r'$a=3,\ b=2$',['9','12','4'],r'$25=5^2$'),(10,r'$a=10,\ b=1$',['100','20','1'],r'$121=11^2$')]
for y,lab,nums,res in rows:
    text(ax,12,y+5,lab,'encre','s')
    for x,r,n in zip(bx,roles,nums): box(ax,x,y,13,10,r,label=n)
    box(ax,68,y,18,10,'resultat',label=res,size='s')
save(fig,'15-098')
