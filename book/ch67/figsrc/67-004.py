import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 86, r'$p$ : premier (sommes de 1)', 'sujet', 'm')
text(ax, 44, 80, r'$n$ : taille de la base', 'varie', 'm')
labs = [r'$p$ choix', r'$p$ choix', '⋯', r'$p$ choix']
for i in range(4):
    x = 4 + i * 21
    box(ax, x, 60, 16, 12, 'fixe' if i == 2 else 'sujet', label=labs[i], size='s')
    if i < 3: text(ax, x + 18.5, 66, '×', 'encre', 'm')
brace(ax, 4, 83, 58, 'varie', label=r'$n$ coefficients')
arrow(ax, (44, 48), (44, 36), 'resultat')
box(ax, 14, 22, 60, 13, 'resultat', label=r'$q=p^n$ éléments', size='m')
text(ax, 44, 12, 'puissance d’un premier', 'resultat', 'm')
save(fig, '67-004')
