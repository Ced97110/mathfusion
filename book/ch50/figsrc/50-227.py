import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$56 = 2^3 \times 7$ : $n_7$ divise 8','encre','m')
text(ax,2,38.5,'diviseur de 8','encre','s',ha='left')
text(ax,2,20.5,'reste mod 7','encre','s',ha='left')
xs=[32+14*i for i in range(4)]
for x,d,r in zip(xs,[1,2,4,8],[8%7,2%7,4%7,8%7]):
    box(ax,x,34,12,9,'fixe',label=str(d))
    ok=(r==1)
    box(ax,x,16,12,9,'resultat' if ok else 'limite',label=str(r))
    arrow(ax,(x+6,34),(x+6,25.8),'fixe')
text(ax,44,6,r'$n_7 \in \{1,\ 8\}$','resultat','l')
save(fig,'50-227')
