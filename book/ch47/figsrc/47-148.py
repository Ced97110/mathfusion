import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 20, 57, r'$G$', 'sujet', 'xl'); line(ax, [(10, 52), (30, 52)], 'encre', lw=1.4); text(ax, 20, 46.5, r'$N$', 'varie', 'xl')
box(ax, 38, 52, 46, 9, 'sujet', label='G : 12 heures', size='s')
box(ax, 38, 38, 46, 9, 'varie', label='3, 6, 9 comptent comme 0', size='s')
arrow(ax, (33, 56), (38, 56.5), 'fixe'); arrow(ax, (33, 44), (38, 42.5), 'fixe')
for i, (s, r) in enumerate([('{0, 3, 6, 9}', 'varie'), ('{1, 4, 7, 10}', 'sujet'), ('{2, 5, 8, 11}', 'sujet')]):
    box(ax, 4 + i * 27.5, 12, 26, 10, r, label=s, size='s')
arrow(ax, (20, 38), (20, 23), 'fixe')
brace(ax, 4, 83, 10, 'resultat', label='G/N : 3 éléments', size='m')
save(fig, '47-148')
