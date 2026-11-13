import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
P=[(0,0),(1,1),(0,2),(1,0),(0,1),(1,2),(0,0)]
X=lambda i:2+12.2*i; Y=lambda i:56-8.5*i
for i,p in enumerate(P):
    role='sujet' if i==0 else ('resultat' if i==6 else 'fixe')
    box(ax,X(i),Y(i),11,6.5,role,label=rf'$({p[0]},{p[1]})$',size='s')
    if i<6: arrow(ax,(X(i)+11,Y(i)+3.25),(X(i+1)+5.5,Y(i+1)+6.5),'varie')
text(ax,X(0)+5.5,Y(0)+10,'départ','sujet','s')
text(ax,3,22,r'$+\,(1,1)$ à chaque pas','varie','m',ha='left')
text(ax,3,14,'retour en (0, 0) : on arrête','resultat','m',ha='left')
save(fig,'45-184')
