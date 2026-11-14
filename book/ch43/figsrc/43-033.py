import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
box(ax, 4, 14, 34, 20, 'fixe'); box(ax, 50, 14, 34, 20, 'sujet')
text(ax, 21, 40, 'avec la lettre', 'fixe', 's'); text(ax, 67, 40, 'avec le signe', 'sujet', 's')
for x, s, r in [(10, r'$x$', 'encre'), (21, r'$E$', 'varie'), (32, r'$y$', 'encre'),
                (56, r'$x$', 'encre'), (67, r'$\sim$', 'varie'), (78, r'$y$', 'encre')]:
    text(ax, x, 24, s, r, 'l')
arrow(ax, (39, 24), (49, 24), 'resultat', both=True)
text(ax, 44, 9, 'même sens', 'resultat', 's')
text(ax, 68, 9, '« est équivalent à »', 'sujet', 's')
save(fig, '43-033')
