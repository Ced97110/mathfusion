import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
coefs = ['1', '0', '0', '0', r'$-4$', '2']
degs = [r'$x^5$', r'$x^4$', r'$x^3$', r'$x^2$', r'$x$', '1']
w, g = 12, 2.4
x0 = 3
for i, (c, d) in enumerate(zip(coefs, degs)):
    x = x0 + i * (w + g)
    role = 'fixe' if i == 0 else 'resultat'
    box(ax, x, 30, w, 11, role, label=c)
    text(ax, x + w / 2, 24, d, 'encre', 's')
text(ax, x0 + w / 2, 47, '2 ne divise pas 1', 'fixe', 's', ha='left')
brace(ax, x0 + w + g, x0 + 5 * (w + g) + w, 44, 'resultat', label=None, down=False)
text(ax, 54, 52, '2 divise ces cinq', 'resultat', 's')
text(ax, 44, 59, 'critère avec le premier 2', 'sujet', 's')
text(ax, 44, 12, r'terme constant $2$ : $4$ ne le divise pas', 'resultat', 's')
save(fig, '65-137')
