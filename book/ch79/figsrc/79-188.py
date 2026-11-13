import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'$\max+\min=a+b$, premier par premier', 'encre', 's')
data = [('2','12 : 2 ; 20 : 2', r'$2+2=2+2$'), ('3','12 : 1 ; 20 : 0', r'$1+0=1+0$'), ('5','12 : 0 ; 20 : 1', r'$1+0=0+1$')]
for i, (p, ex, eq) in enumerate(data):
    x = 2 + i * 29
    box(ax, x, 8, 27, 34, 'resultat', fill=True)
    text(ax, x + 13.5, 36, 'premier ' + p, 'resultat', 's', weight='bold')
    text(ax, x + 13.5, 25, ex, 'encre', 's')
    text(ax, x + 13.5, 14, eq, 'encre', 's')
text(ax, 44, 2, '', 'encre', 's')
save(fig, '79-188')
