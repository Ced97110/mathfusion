import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$a \leq a$', 'sujet', 'l')
for x, node, head, cap in [(15, '5', 'divisibilité', '5 = 5 × 1'), (44, 'bleu', 'inclusion', '{bleu} ⊆ {bleu}'), (73, '7', 'réels', '7 ≤ 7')]:
    y, r = 24, 6
    text(ax, x, 39, head, 'fixe', 's')
    disc(ax, x, y, r, 'sujet', label=node)
    arrow(ax, (x - 3, y + 5.2), (x + 3, y + 5.2), 'varie', curve=-1.3)
    text(ax, x, 12, cap, 'resultat', 's')
save(fig, '79-017')
