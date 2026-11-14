import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,46,r'$I$ contient 4 et 6','sujet','m')
y=24; f=numberline(ax,8,76,y,0,12,step=1,every=2,arrow_right=False)
for v in range(0,13,2): disc(ax,f(v),y,1.8,{4:'sujet',6:'sujet',2:'varie'}.get(v,'resultat'))
brace(ax,f(4),f(6),y+3,'varie',label=r'2 = 6 − 4',down=False)
text(ax,44,5,r'puis tous les multiples de 2','resultat','s')
save(fig,'52-048')
