import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 6, 70, 76, 10, 'sujet', label=r'$\ker f$ est un sous-groupe de $\mathbb{Z}/7\mathbb{Z}$', size='m')
arrow(ax, (44, 70), (44, 62), 'fixe')
box(ax, 6, 48, 76, 14, 'varie', label=r'Lagrange : $|\ker f|$ divise 7', size='l', lw=1.6)
text(ax, 44, 42, '7 premier : diviseurs 1 et 7', 'encre', 's')
arrow(ax, (30, 38), (24, 31), 'fixe'); arrow(ax, (58, 38), (64, 31), 'fixe')
for cx, k, t in [(24, 1, r'$\{0\}$ : 1 élément'), (64, 7, r'tout : 7 éléments')]:
    box(ax, cx - 19, 8, 38, 23, 'resultat')
    text(ax, cx, 24, t, 'resultat', 's')
    for i in range(7):
        x = cx - 14.4 + i * 4.8
        disc(ax, x, 14, 1.9, 'sujet' if i < k else 'fixe', fill=(i < k), lw=0.7)
save(fig, '48-166')
