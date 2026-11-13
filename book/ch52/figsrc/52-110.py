import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$I=\{ra+m\}$ : tout ce que M et a donnent','sujet','s')
f=numberline(ax,8,80,35,0,8,arrow_right=False)
for v in range(9):
    disc(ax,f(v),44,2.2,'resultat')
    disc(ax,f(v),22,2.2,'limite' if v%2==0 else 'fixe',fill=(v%2==0))
text(ax,44,52,'(7) et 3 : tous les entiers','resultat','s')
text(ax,44,14,'(6) et 4 : seulement les pairs','limite','s')
save(fig,'52-110')
