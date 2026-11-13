import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)

# en-têtes
text(ax, 10, 84, 'calcul', 'fixe', 's')
text(ax, 39, 84, 'mot', 'fixe', 's')
text(ax, 73.5, 84, 'figure', 'fixe', 's')

# le mot, à deux rangées
box(ax, 24, 62, 30, 8, 'sujet', label='« 3 au carré »', size='m')
box(ax, 24, 26, 30, 8, 'sujet', label='« 4 au carré »', size='m')

# le calcul qu'il nomme
text(ax, 10, 66, '3 × 3', 'encre', 'm')
text(ax, 10, 30, '4 × 4', 'encre', 'm')
arrow(ax, (23.5, 66), (16.5, 66), 'encre')
arrow(ax, (23.5, 30), (16.5, 30), 'encre')

# la figure qu'il rappelle
for i in range(3):
    for j in range(3):
        box(ax, 66 + 5*i, 58.5 + 5*j, 5, 5, 'fixe', lw=0.6, r=0)
for i in range(4):
    for j in range(4):
        box(ax, 64 + 5*i, 20 + 5*j, 5, 5, 'fixe', lw=0.6, r=0)
arrow(ax, (54.5, 66), (65, 66), 'fixe')
arrow(ax, (54.5, 30), (63, 30), 'fixe')

# résultat commun
text(ax, 10, 60, '= 9', 'resultat', 'm')
text(ax, 10, 24, '= 16', 'resultat', 'm')
text(ax, 73.5, 54, '9 carreaux', 'resultat', 's')
text(ax, 74, 15, '16 carreaux', 'resultat', 's')

# limite
text(ax, 44, 6, "3 × 4 : pas « au carré »", 'limite', 's')

save(fig, '04-010')
