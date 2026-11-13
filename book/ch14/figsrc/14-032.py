import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,r'128 $\div$ 8 = 16','encre','l')
for i in range(7): box(ax,6+11*i,22,9,9,'varie' if i<3 else 'resultat',label='2')
brace(ax,6,81,31,'sujet',label='$n$ = 7 facteurs 2',down=False)
brace(ax,6,37,22,'varie',label='$m$ = 3 retirés')
brace(ax,39,81,22,'resultat',label=r'$n - m$ = 4 restent')
save(fig,'14-032')
