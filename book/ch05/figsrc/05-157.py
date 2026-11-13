import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
v0,v1=-3,7
def row(y,vals,role,odd_open):
    f=numberline(ax,6,76,y,v0,v1,labels=False,arrow_right=False)
    for v in vals: disc(ax,f(v),y,1.4,role)
    text(ax,f(0),y-5,'0','encre','s'); text(ax,f(1),y-5,'1','encre','s')
    return f
text(ax,2,57,r'valeurs de $9u + 7v$','sujet','m',ha='left')
f=row(42,range(v0,v1+1),'resultat',False)
disc(ax,f(1),42,2.6,'resultat',fill=False,lw=1.2)
text(ax,f(1),49,r'$9 \times 4 + 7 \times (-5) = 1$','resultat','s')
text(ax,70,35.5,'tout est multiple de 1','resultat','s',ha='right')
text(ax,2,30,r'valeurs de $6u + 4v$','autre','m',ha='left')
g=row(15,[v for v in range(v0,v1+1) if v%2==0],'fixe',True)
disc(ax,g(1),15,1.8,'limite',fill=False,lw=1.2)
text(ax,70,21.5,'tout est multiple de 2','fixe','s',ha='right')
text(ax,g(1),5,'1 : jamais atteint','limite','s')
save(fig,'05-157')
