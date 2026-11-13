import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)

# sept disques « 3 » alignés, avec six signes × entre eux
for i in range(7):
    disc(ax, 11 + 11*i, 56, 3.5, 'sujet', label='3', size='m')
for i in range(6):
    xc = 16.5 + 11*i
    line(ax, [(xc-1.2, 54.8), (xc+1.2, 57.2)], 'sujet', lw=1.0)
    line(ax, [(xc-1.2, 57.2), (xc+1.2, 54.8)], 'sujet', lw=1.0)
# compter un par un : six sauts d'un disque au suivant
for i in range(6):
    arrow(ax, (11 + 11*i + 1.5, 59.4), (11 + 11*(i+1) - 1.5, 59.4), 'varie', lw=0.8, curve=-0.7)

text(ax, 44, 67, 'un lecteur compte 6 : faux', 'limite', 's')
brace(ax, 7.5, 80.5, 51, 'fixe', label='7 facteurs à compter', down=True, size='s')

arrow(ax, (44, 43), (44, 33), 'varie')
text(ax, 47, 38, 'calcul inchangé : même valeur', 'varie', 's', ha='left')

# écriture cherchée : le 3 et le 7 écrits une seule fois
box(ax, 30, 16, 10, 12, 'sujet', label='3', size='l', weight='bold')
box(ax, 48, 16, 10, 12, 'varie', dash=True, label='7', size='l', weight='bold')
text(ax, 53, 12.5, 'exposant : combien de 3', 'varie', 's')

text(ax, 44, 5, 'le 3 une fois, le 7 une fois', 'encre', 's')

save(fig, '04-004')
