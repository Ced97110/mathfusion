import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
coefs = ['1', '−12', '104', '−768', '2 640', '−2 882']
degs = [r'$x^5$', r'$x^4$', r'$x^3$', r'$x^2$', r'$x$', '1']
w, g = 12.5, 1.5
for i, (c, d) in enumerate(zip(coefs, degs)):
    x = 3 + i * (w + g)
    role = 'fixe' if i == 0 else 'resultat'
    if i == 5: role = 'varie'
    box(ax, x, 36, w, 11, role, label=c, size='s')
    text(ax, x + w / 2, 30, d, 'encre', 's')
text(ax, 44, 66, 'coefficients de la recette', 'encre', 's')
brace(ax, 3 + w + g, 3 + 4 * (w + g) + w, 51, 'resultat', label=None, down=False)
text(ax, 44, 59, 'pairs', 'resultat', 's')
text(ax, 80, 59, 'pair aussi', 'varie', 's')
text(ax, 44, 16, r'$2\,882\div4=720{,}5$', 'varie', 's')
text(ax, 44, 8, 'ne tombe pas juste : Eisenstein', 'resultat', 's')
save(fig, '65-143')
