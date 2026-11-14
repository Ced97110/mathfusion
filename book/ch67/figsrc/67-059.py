import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, 'chaque coefficient, modulo 2', 'encre', 's')
terms = [r'$x^6$', r'$22x^5$', r'$21x^4$', r'$12x^3$', r'$-37x^2$', r'$-29x$', r'$-15$']
coef = [1, 22, 21, 12, -37, -29, -15]
for i, (t, c) in enumerate(zip(terms, coef)):
    r = c % 2
    box(ax, 2 + 12 * i, 24, 10.5, 28, 'sujet' if r else 'fixe', label=t + '\n↓\n' + str(r), size='s')
box(ax, 8, 6, 72, 12, 'resultat', label=r'$f_2=x^6+x^4+x^2+x+1$')
save(fig, '67-059')
