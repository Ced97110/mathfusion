import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$M_n(R)$ avec $n=2$, $R=\mathbb{R}$', 'sujet', 'l')
cw, ch, x0, y0 = 15, 11, 14, 18
for i in range(2):
    for j in range(2):
        box(ax, x0 + j * cw, y0 + (1 - i) * ch, cw, ch, 'sujet', label=r'$\in\mathbb{R}$', size='m')
brace(ax, x0, x0 + 2 * cw, y0, 'varie', label='2 colonnes', down=True)
x1 = x0 + 2 * cw
line(ax, [(x1 + 2, y0 + ch), (x1 + 8, y0 + ch)], 'varie')
text(ax, x1 + 9, y0 + ch, '2 lignes', 'varie', 's', ha='left')
text(ax, 44, 46, 'les cases viennent de $R$ : 4 réels', 'autre', 'm')
save(fig, '51-049')
