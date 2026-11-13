import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# (a+b)^5 : coefficients 1, 5, 10, 10, 5, 1 ; modulo 5 : 1, 0, 0, 0, 0, 1
coef = [1, 5, 10, 10, 5, 1]
text(ax, 1.5, 38, 'coefficients', 'encre', 's', ha='left')
text(ax, 1.5, 15, 'modulo 5', 'encre', 's', ha='left')
for i, c in enumerate(coef):
    x = 17 + i * 11.6
    end = i in (0, 5)
    box(ax, x, 32, 10, 12, 'resultat' if end else 'varie', label=str(c))
    box(ax, x, 9, 10, 12, 'resultat' if end else 'fixe', label=str(c % 5))
    arrow(ax, (x + 5, 31.5), (x + 5, 22), 'resultat' if end else 'varie')
save(fig, '62-113')
