import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# essais ratés (faux) puis formules non essayées
for i in range(5):
    x = 2 + 9 * i
    box(ax, x, 44, 7, 8, 'limite')
    line(ax, [(x + 1.8, 45.8), (x + 5.2, 50.2)], 'limite', lw=1.1)
    line(ax, [(x + 1.8, 50.2), (x + 5.2, 45.8)], 'limite', lw=1.1)
for j in range(4):
    box(ax, 47 + 9 * j, 44, 7, 8, 'fixe', fill=False, dash=True)
brace(ax, 2, 43, 42, 'limite', label='1 000 essais ratés')
brace(ax, 47, 83, 42, 'fixe', label='une infinité non essayée')
text(ax, 68, 30, 'prouvé par Abel et Galois', 'resultat', 's')
box(ax, 2, 12, 36, 12, 'fixe', label="« on n'a pas trouvé »", size='s')
text(ax, 44, 18, '≠', 'encre', 'xl')
box(ax, 50, 12, 36, 12, 'resultat', label='« rien à trouver »', size='s')
save(fig, '64-008')
