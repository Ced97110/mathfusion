import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
X0, S = 12.5, 13
for i in range(5): box(ax, X0 + i*S, 22, 11, 10, 'varie' if i < 2 else 'resultat', label=r'$a$')
brace(ax, X0, X0 + 4*S + 11, 33, 'sujet', label=r'$n$ = 5 facteurs', down=False)
brace(ax, X0, X0 + S + 11, 21, 'varie', label=r'$m$ = 2 barrés')
brace(ax, X0 + 2*S, X0 + 4*S + 11, 21, 'resultat', label=r'$n-m$ = 3 restent')
save(fig, '14-035')
