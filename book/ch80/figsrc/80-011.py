import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
P={1:(44,6,'+30'),2:(16,30,'−15'),3:(44,30,'−10'),5:(72,30,'−6'),6:(16,54,'+5'),10:(44,54,'+3'),15:(72,54,'+2'),30:(44,78,'−1')}
E=[(1,2),(1,3),(1,5),(2,6),(2,10),(3,6),(3,15),(5,10),(5,15),(6,30),(10,30),(15,30)]
chain={(1,2),(2,6),(6,30)}
for a,b in E:
    line(ax,[(P[a][0],P[a][1]+11),(P[b][0],P[b][1])],'encre' if (a,b) in chain else 'fixe',lw=1.6 if (a,b) in chain else 0.8)
for d,(x,y,t) in P.items():
    box(ax,x-7,y,14,11,'sujet' if t[0]=='+' else 'varie',label=f'{d}\n{t}',size='m')
text(ax,14,11,'chaque case :\ndiviseur de 30,\npuis son terme','encre','s')
text(ax,74,86,'1 divise 2,\nqui divise 6,\nqui divise 30','encre','s')
save(fig,'80-011')
