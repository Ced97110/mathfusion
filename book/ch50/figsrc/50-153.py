import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$A_4$ : 12 éléments, $H$ en a 6', 'encre', 's')
for y, r, lab in [(36, 'sujet', r'$H$ : 6 éléments'), (13, 'varie', r'$gH$ : 6 éléments')]:
    box(ax, 6, y - 6.5, 76, 13, r)
    text(ax, 44, y + 9.5, lab, r, 's')
    for i in range(6): disc(ax, 16 + i * 12, y, 3, r, fill=False)
disc(ax, 16, 13, 3, 'varie', label=r'$g$', size='s')
text(ax, 44, 3.5, r'$12 / 6 = 2$ classes seulement', 'resultat', 'm', weight='bold')
save(fig, '50-153')
