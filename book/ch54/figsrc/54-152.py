import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$x^2$ divisé par $2x-1$ : on multiplie par $b_m=2$', 'encre', 's')
# k = 2 multiplications : 2 cases orange comptées
for i in range(2):
    box(ax, 14 + i * 34, 36, 26, 12, 'varie', label=r'$\times 2$', size='l')
    text(ax, 27 + i * 34, 30, f'étape {i + 1}', 'varie', 's')
text(ax, 44, 42, r'puis', 'fixe', 's')
text(ax, 44, 18, r'$k=2$ étapes : $b_m^{\,k}=2\times2=4$', 'sujet', 'm')
text(ax, 44, 8, r'$k$ dépend de $f$ et de $g$', 'fixe', 's')
save(fig, '54-152')
