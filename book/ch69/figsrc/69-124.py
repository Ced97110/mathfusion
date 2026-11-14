import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
labs = [r'$x^3+x+1$', r'$3x^2+1$', r'$-6x-9$', r'$-279$']
degs = ['degré 3', 'degré 2', 'degré 1', 'degré 0']
for i in range(4):
    x = 3 + 21 * i
    box(ax, x, 28, 17, 12, 'resultat' if i == 3 else 'sujet', label=labs[i], size='s')
    text(ax, x + 8.5, 23, degs[i], 'fixe', 's')
    if i < 3:
        arrow(ax, (x + 17.3, 34), (x + 20.7, 34), 'varie')
brace(ax, 3, 83, 44, 'sujet', label='4 termes', down=False)
text(ax, 71.5, 17.5, r'$=-9\times31$', 'resultat', 's')
text(ax, 24, 8, r'$p=q=1$ : $27q^2+4p^3=31$', 'encre', 's')
text(ax, 66, 8, r'$p\times31=31\neq0$', 'encre', 's')
save(fig, '69-124')
