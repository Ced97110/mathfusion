import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 3, 80, 48, 9, 'sujet', label=r'$f=x^3-2x^2+4$')
box(ax, 55, 80, 30, 9, 'autre', label=r'$g=x-1$')
text(ax, 44, 74, r'sur $\mathbb{Q}$ : cinq effets', 'fixe', 's')
rows = [('division', r'$q=x^2-x-1,\ r=3$'),
        ('reste', r'$f(1)=3$'),
        ('facteur', r'$x-1$ ne divise pas $f$'),
        ('PGCD', r'$1$'),
        ('racines', r'aucune rationnelle')]
for i, (name, res) in enumerate(rows):
    y = 60 - i * 13
    box(ax, 3, y, 24, 9, 'fixe', label=name)
    arrow(ax, (27, y + 4.5), (31, y + 4.5), 'varie')
    box(ax, 31, y, 54, 9, 'resultat', label=res)
save(fig, '54-243')
