import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
X=[11,28,45,62,79]; Y={1:50,2:38,3:26}
text(ax,44,68,'trajet du sommet 2','sujet','m')
for k,y in Y.items(): text(ax,3,y,str(k),'fixe','s')
for x in X:
    for y in Y.values(): disc(ax,x,y,1.3,'fixe')
path=[2,3,1,3,2]
for i,(x,k) in enumerate(zip(X,path)):
    disc(ax,x,Y[k],2.1,'sujet' if i<3 else 'resultat')
for i in range(4):
    r='varie' if i<2 else 'resultat'
    p=(X[i]+2.4,Y[path[i]]+(0 if path[i]==path[i+1] else (-0.6 if Y[path[i+1]]<Y[path[i]] else 0.6)))
    arrow(ax,(X[i]+2.2,Y[path[i]]),(X[i+1]-2.2,Y[path[i+1]]),r,lw=1.1)
for t,xm in zip(['départ',r'$b$',r'$a$',r'$a^{-1}$',r'$b^{-1}$'],[11,19.5,36.5,53.5,70.5]):
    text(ax,xm,59,t,'varie' if t in (r'$b$',r'$a$') else ('resultat' if t!='départ' else 'sujet'),'s')
brace(ax,11,45,18,'varie',label=r'aller : $a\,b$'); brace(ax,45,79,18,'resultat',label=r'retour : $b^{-1}a^{-1}$')
save(fig,'44-246')
