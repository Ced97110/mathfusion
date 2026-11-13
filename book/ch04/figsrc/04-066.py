import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# petit cas : 3 facteurs 2, 5 cases
text(ax, 4, 76, '3 facteurs 2', 'fixe', 's', ha='left')
for k, x in enumerate([4, 7.5, 11, 14.5, 18]):
    box(ax, x, 68, 3, 4, 'sujet' if k % 2 == 0 else 'fixe', r=0.2)
text(ax, 24, 70, '= 5 caractères', 'encre', 's', ha='left')
text(ax, 52, 70, '2³', 'resultat', 'l')
text(ax, 57, 70, '2 caractères', 'resultat', 's', ha='left')
line(ax, [(4, 62), (84, 62)], 'fixe', dash=True)
# grand cas : 20 facteurs 2, 39 cases
text(ax, 4, 56, '20 facteurs 2', 'fixe', 's', ha='left')
for i in range(39):
    box(ax, 4 + 2 * i, 44, 1.8, 6, 'sujet' if i % 2 == 0 else 'fixe', r=0.1)
brace(ax, 4, 81.8, 42.5, 'fixe', label='39 caractères', down=True, size='s')
# écriture courte
text(ax, 30, 22, '2', 'sujet', 'l')
text(ax, 32.6, 25.3, '20', 'varie', 's', ha='left')  # exposant : collé en haut à droite du 2
text(ax, 42, 22, '3 caractères', 'resultat', 's', ha='left')
text(ax, 44, 12, '2¹⁰⁰ : 4 caractères', 'varie', 's')
text(ax, 44, 5, 'le livre dit 60 ; ici 39', 'fixe', 's')
save(fig, '04-066')
