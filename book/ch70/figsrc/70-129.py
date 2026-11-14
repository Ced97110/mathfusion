import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 24, 86, 'méthode générale', 'fixe', 's')
text(ax, 64, 86, r'cas avec le paramètre $c$', 'sujet', 's')
rows = [(64, r'$F_1=\ldots=F_m=0$' + '\n' + r'$G\neq0$', r'$x^2-c=0$' + '\n' + r'$x\neq0$'),
        (38, 'abaisser les degrés\nen $x$, à chaque étape', r'$x^2$ remplacé par $c$'),
        (12, 'condition sur\nles paramètres seuls', r'$c\neq0$')]
for i, (y, a, b) in enumerate(rows):
    box(ax, 3, y, 42, 16, 'fixe', label=a, size='s')
    box(ax, 47, y, 38, 16, 'resultat' if i == 2 else 'sujet', label=b, size='s')
    if i < 2:
        arrow(ax, (24, y), (24, y - 10), 'varie', lw=1.0)
        arrow(ax, (66, y), (66, y - 10), 'varie', lw=1.0)
text(ax, 66, 6, r'$c=-1$ : $x=i$ convient', 'resultat', 's')
save(fig, '70-129')
