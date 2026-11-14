import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$L$ d’indice 2, $h\notin L$', 'encre', 's')
def row(y):
    for i in range(3):
        box(ax, 8 + 11 * i, y, 10.4, 8, 'sujet', r=0.4)
        box(ax, 45 + 11 * i, y, 10.4, 8, 'varie', r=0.4, lw=1.8 if i == 1 else 0.8, label=r'$h$' if i == 1 else None)
row(40); row(14)
brace(ax, 8, 40.4, 49.5, 'sujet', label=r'$L$', down=False)
brace(ax, 45, 77.4, 49.5, 'varie', label=r'$hL$ = le reste', down=False)
brace(ax, 8, 40.4, 12.5, 'sujet', label=r'$L$', down=True)
brace(ax, 45, 77.4, 12.5, 'varie', label=r'$Lh$ = le reste', down=True)
text(ax, 61, 31, '=', 'resultat', 'xl', weight='bold')
save(fig, '50-235')
