import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 86, r'$p=2$ divise 12 et 4, pas 3', 'encre', 's')
labs = ['{0, 4, 8}', '{1, 5, 9}', '{2, 6, 10}', '{3, 7, 11}']
roles = ['sujet', 'fixe', 'resultat', 'fixe']
for i in range(4):
    box(ax, 2 + i * 21.5, 54, 20, 10, roles[i], label=labs[i], size='s')
brace(ax, 2, 2 + 3 * 21.5 + 20, 54, 'sujet', label=r'quotient : $12/3=4$ éléments', depth=1.6)
text(ax, 12, 70, r'$\langle 4\rangle$', 'sujet', 's')
text(ax, 55, 70, r'classe de $b=2$ : ordre 2', 'resultat', 's')
arrow(ax, (82, 43), (82, 52), 'varie', curve=0.0)
text(ax, 58, 38, 'on remonte dans A', 'varie', 's', ha='center')
text(ax, 44, 29, "2 divise 6, l'ordre de 2", 'encre', 's')
text(ax, 44, 20, "2 répété 3 fois : 6", 'varie', 's')
box(ax, 20, 4, 48, 10, 'resultat', label="6 est d'ordre 2")
arrow(ax, (44, 17), (44, 14), 'resultat')
save(fig, '50-142')
