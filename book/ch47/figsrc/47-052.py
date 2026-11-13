import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,r'$\varphi(n)$ : taille de $U(n)$','encre','m')
rows=[(46,10,[1,3,7,9]),(28,12,[1,5,7,11]),(10,7,[1,2,3,4,5,6])]
for y,n,u in rows:
    text(ax,2,y,r'$n=%d$'%n,'fixe','m',ha='left')
    x0=26
    for k in range(len(u)): disc(ax,x0+7*k,y,2.8,'sujet')
    text(ax,x0+3.5*(len(u)-1),y-6.5,', '.join(map(str,u)),'sujet','s')
    text(ax,86,y,r'$\varphi(%d)=%d$'%(n,len(u)),'resultat','m',ha='right')
save(fig,'47-052')
