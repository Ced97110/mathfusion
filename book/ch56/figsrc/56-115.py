import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
assert 3 * 10 == 30 and 30 % 5 == 0 and 3 % 5 != 0 and 10 % 5 == 0
labs = [r'$p = 5$ irréductible', '(5) maximal', '(5) premier']
for i, (x, lab) in enumerate(zip([1, 31, 61], labs)):
    box(ax, x, 66, 26, 11, 'sujet' if i == 0 else 'fixe' if i == 1 else 'resultat', label=lab, size='s')
    if i < 2:
        arrow(ax, (x + 26.5, 71.5), (x + 30.5, 71.5), 'fixe')
arrow(ax, (72, 66), (60, 51), 'resultat')
text(ax, 44, 48, r'5 ∣ 30 = $a \times b$', 'encre', 'l')
box(ax, 14, 24, 22, 11, 'autre', label=r'$a = 3$', size='m')
text(ax, 44, 29.5, '×', 'fixe', 'm')
box(ax, 52, 24, 22, 11, 'sujet', label=r'$b = 10$', size='m')
text(ax, 25, 18, r'$5 \nmid 3$', 'limite', 'm')
text(ax, 63, 18, r'$5 \mid 10$', 'resultat', 'm')
text(ax, 44, 7, r'$5 \mid a$ ou $5 \mid b$', 'resultat', 'm')
save(fig, '56-115')
