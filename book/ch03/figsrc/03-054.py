import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
f=numberline(ax,10,80,48,0,12,1,labels=False,arrow_right=False)
g=numberline(ax,10,80,22,0,12,1,labels=False,arrow_right=False)
for v in (0,4,8,12):
    text(ax,f(v),44,str(v),'fixe','s'); text(ax,f(v),18,str(v),'fixe','s')
for a,b in [(0,4),(4,8),(8,12)]: arrow(ax,(f(a),49),(f(b),49),'autre',curve=-0.5)
text(ax,44,62,'multiplication : + 4, 3 fois','autre','s')
for a,b in [(12,8),(8,4),(4,0)]: arrow(ax,(f(a),23),(f(b),23),'sujet',curve=0.5)
text(ax,44,8,'division : − 4, 3 fois','sujet','s')
text(ax,44,34,'3 : multiplicateur, quotient','resultat','s')
save(fig,'03-054')
