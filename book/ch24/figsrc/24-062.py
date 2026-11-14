import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
box(ax, 14, 74, 71, 8, 'fixe', fill=True, label='énoncé en mots', size='m')
arrow(ax, (49.5, 74), (49.5, 70), 'fixe', lw=0.9)
steps = [('sujet', r'nommer : $D$ et $Q$'), ('sujet', r'écrire $D+Q=27$ ; $10D+25Q=435$'),
         ('varie', r'résoudre : $D=16$ ; $Q=11$'), ('resultat', 'vérifier les deux équations'),
         ('resultat', 'conclure par une phrase')]
for i, (r, lab) in enumerate(steps):
    y = 62 - 12 * i
    disc(ax, 7, y + 4, 3.2, r, label=str(i + 1), size='m')
    box(ax, 14, y, 71, 8, r, fill=True, label=lab, size='m')
    arrow(ax, (49.5, y), (49.5, y - 4), 'fixe', lw=0.9)
box(ax, 14, 2, 71, 8, 'fixe', fill=True, label='réponse en mots', size='m')
save(fig, '24-062')
