import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
base = 56.0; k = 0.9
text(ax, 44, 98, 'chaîne : vraie, la norme baisse', 'resultat', 's')
bars = [(8, '6', 36), (30, '3', 9), (52, '2', 4)]
line(ax, [(4, base), (70, base)], 'fixe')
for x, lab, n in bars:
    box(ax, x, base, 14, n * k, 'sujet', r=0.4)
    text(ax, x + 7, base - 4.5, f'{lab}\nnorme {n}', 'sujet', 's')
arrow(ax, (20, 80), (35, 66), 'varie')
arrow(ax, (20, 86), (58, 62), 'varie')
text(ax, 78, 74, r'$36=4\times9$', 'encre', 's')
line(ax, [(2, 40), (86, 40)], 'fixe', lw=0.4)
text(ax, 44, 34, 'primalité : fausse pour 2', 'limite', 's')
box(ax, 2, 20, 84, 9, 'fixe', label='2 ∣ 6 = (1 + √−5)(1 − √−5)', size='s')
box(ax, 2, 5, 84, 10, 'limite', label='mais 2 ne divise aucun des facteurs', size='s')
save(fig, '56-075')
