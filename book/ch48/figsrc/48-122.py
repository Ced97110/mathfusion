import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for i in range(6):
    box(ax,3+i*14,44,12,10,'sujet' if i<4 else 'fixe')
brace(ax,3,3+3*14+12,54,'sujet',label=r'$HN$ : 4',down=False)
brace(ax,3+4*14,3+5*14+12,54,'fixe',label='2 absents',down=False)
f=numberline(ax,8,78,20,1,6,arrow_right=False)
for v in range(1,7):
    if v==5: continue
    disc(ax,f(v),20,2.4,'limite' if v==4 else 'resultat')
text(ax,24,28,'divisent 6','resultat','s')
text(ax,58,28,'4 ne divise pas 6','limite','s')
text(ax,44,8,"nombre d'éléments",'fixe','s')
save(fig,'48-122')
