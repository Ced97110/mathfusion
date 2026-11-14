import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$k\ \mathrm{mod}\  n$ = reste de $k$ par $n$','sujet','m')
def row(y,g,k,res):
    X=lambda i:6+8*i+3*(i//g)
    for i in range(k):
        disc(ax,X(i),y,3,'varie' if i>=(k//g)*g else 'fixe')
    text(ax,(X((k//g)*g)+X(k-1))/2,y-6,f'reste {res}','varie','s')
row(44,2,5,1); row(27,3,5,2)
text(ax,70,44,r'$5\ \mathrm{mod}\ 2=1$','sujet','m'); text(ax,70,27,r'$5\ \mathrm{mod}\ 3=2$','sujet','m')
text(ax,44,10,r'$(5\ \mathrm{mod}\ 2,\ 5\ \mathrm{mod}\ 3)=(1,\,2)$','resultat','m')
save(fig,'45-185')
