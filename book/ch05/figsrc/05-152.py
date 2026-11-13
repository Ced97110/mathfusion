import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,2,56,'diviseurs communs de 12 et 0','sujet','m',ha='left')
f=numberline(ax,6,76,44,0,14,labels=False,arrow_right=False)
for d in [1,2,3,4,6,12]:
    disc(ax,f(d),44,1.7,'resultat' if d==12 else 'sujet')
    text(ax,f(d),39.5,str(d),'resultat' if d==12 else 'sujet','s')
text(ax,f(12)+1,50,'plus grand : |12| = 12','resultat','s',ha='right')
text(ax,2,30,'diviseurs communs de 0 et 0','limite','m',ha='left')
g=numberline(ax,6,76,20,0,14,labels=False,arrow_right=True)
for d in range(1,15): disc(ax,g(d),20,1.7,'limite')
text(ax,44,11,"aucun n'est le plus grand",'limite','m')
save(fig,'05-152')
