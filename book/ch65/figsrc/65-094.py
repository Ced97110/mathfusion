import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'sur $F(\sqrt{d})$ : garder les paires', 'encre', 'm')
rows = [(r'$D$', 8, 4, 'resultat', 'transitif :\n$f$ reste irréductible'), (r'$C$', 4, 2, 'varie', 'pas transitif :\n$f$ devient réductible')]
for j, (nm, n, k, role, res) in enumerate(rows):
    y = 46 - j * 24
    text(ax, 5, y + 7, nm, 'sujet', 'm')
    for i in range(n):
        box(ax, 11 + i * 4.4, y + 2, 3.8, 10, 'sujet' if i < k else 'fixe', r=0.5, lw=0.6)
    text(ax, 11 + n * 4.4 / 2 - 2, y - 2.5, f'{k} paires', 'sujet', 's')
    arrow(ax, (48, y + 7), (52, y + 7), 'fixe')
    box(ax, 54, y - 1, 32, 16, role, label=res, size='s')
text(ax, 44, 8, 'permutations paires en bleu', 'sujet', 's')
save(fig, '65-094')
