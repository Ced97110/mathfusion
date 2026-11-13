import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [('1  Nommer', 'h = la taille cherchée', 'sujet'), ('2  Lister', r'$5$ ; $3\frac{1}{3}$ ; $3$ (pieds)', 'sujet'),
        ('3  Écrire', r'$\frac{5}{3\frac{1}{3}}=\frac{h}{3}$', 'sujet'), ('4  Calculer', r'$h = 4{,}5$', 'varie'),
        ('5  Répondre', '« la taille est 4,5 pieds »', 'resultat')]
for i, (a, b, r) in enumerate(rows):
    y = 69 - 16 * i
    box(ax, 3, y, 29, 12, r, label=a, size='m', weight='bold')
    text(ax, 36, y + 6, b, 'encre', 'm' if i != 2 else 'l', ha='left')
    if i < 4: arrow(ax, (17.5, y), (17.5, y - 4), 'fixe', lw=1.2)
save(fig, '09-098')
