import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
rows = [('fixe', r'le corps $F$ : les nombres', "d'abord"), ('sujet', r"l'espace $V$ sur $F$", 'puis'),
        ('varie', r"l'aire $B$ sur $V$", 'puis'), ('resultat', r'le groupe $Sp_{2n}(F)$', 'enfin')]
for i, (role, lab, step) in enumerate(rows):
    y = 4 + i * 22
    box(ax, 22, y, 62, 13, role, label=lab)
    text(ax, 11, y + 6.5, step, role, 's')
    if i < 3: arrow(ax, (53, y + 13.5), (53, y + 21.5), 'encre')
save(fig, '75-066')
