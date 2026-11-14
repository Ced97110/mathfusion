import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 2, 76, 40, 11, 'sujet', label='message de Bob')
arrow(ax, (22, 75.5), (22, 62), 'fixe')
box(ax, 2, 42, 40, 19, 'varie', label='1. signer\navec la clé privée\nde Bob')
arrow(ax, (22, 41.5), (22, 28), 'fixe')
box(ax, 2, 8, 40, 19, 'varie', label='2. chiffrer\navec la clé publique\nd’Alice')
for y, t in ((51.5, 'preuve :\nc’est bien Bob'), (17.5, 'secret :\nseule Alice lit')):
    arrow(ax, (43, y), (51, y), 'resultat')
    box(ax, 52, y - 7, 34, 14, 'resultat', label=t)
save(fig, '53-153')
