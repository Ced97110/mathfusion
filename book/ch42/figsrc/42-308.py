import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 19, 63, 'méthode de preuve', 'sujet', 's'); text(ax, 67, 63, 'sert plus tard', 'resultat', 's')
rows = [('unicité', r'ch. 44 : neutre, inverse'), ('absurde', r'ch. 43 : $\mathbb{R}$ non numérotable'),
        (r'même image $\Rightarrow$ égaux', 'ch. 48 : injective')]
for i, (a, b) in enumerate(rows):
    y = 44 - 17 * i + 6
    y = [46, 29, 12][i]
    box(ax, 3, y, 32, 11, 'sujet', label=a, size='s'); box(ax, 49, y, 37, 11, 'resultat', label=b, size='s')
    arrow(ax, (35.8, y + 5.5), (48.2, y + 5.5), 'varie')
save(fig, '42-308')
