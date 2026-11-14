import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
brace(ax, 3, 83, 52, 'fixe', label='même lettre, numéros 0 à 3', down=False)
tags = ['sans symbole', r'avec $i$', r'avec $j$', r'avec $k$']
reads = ['alpha zéro', 'alpha un', 'alpha deux', 'alpha trois']
for i in range(4):
    x = 3 + 20 * i
    box(ax, x, 34, 17, 13, 'sujet', label=rf'$\alpha_{i}$', size='l')
    text(ax, x + 8.5, 29, tags[i], 'fixe' if i == 0 else 'varie', 's')
    text(ax, x + 8.5, 20, reads[i], 'sujet', 's')
save(fig, '51-172')
