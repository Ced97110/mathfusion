import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$a\,\sin x+b\,\cos x=R\,\sin(x+\alpha)$', 'encre', 'm')
text(ax, 22, 63, 'la somme', 'sujet', 's'); text(ax, 66, 63, r'la forme $R\sin(x+\alpha)$', 'autre', 's')
rows = ((44, '$x=0°$', '$b=4$', r'$R\sin\alpha=4$'), (26, '$x=90°$', '$a=3$', r'$R\cos\alpha=3$'))
for y, xl, l, r in rows:
    box(ax, 4, y, 34, 12, 'sujet', label=l, size='m'); box(ax, 50, y, 34, 12, 'autre', label=r, size='m')
    text(ax, 44, y + 6, '=', 'resultat', 'l', weight='bold')
    text(ax, 44, y + 15, xl.replace('$', ''), 'fixe', 's')
text(ax, 44, 13, r'$R=5$ et $\alpha=53{,}13°$', 'resultat', 'm')
text(ax, 44, 5, 'les deux écritures doivent être égales', 'fixe', 's')
save(fig, '35-016')
