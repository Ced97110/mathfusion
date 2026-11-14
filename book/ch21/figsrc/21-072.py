import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for y, s, r, q, L in [(32, [r'$x-1$', r'$x-1$', r'$x+3$'], 'sujet', r'$D_1$', r'PPCM $\div D_1$'), (10, [r'$x-1$', r'$x+3$', r'$x-1$'], 'autre', r'$D_2$', r'PPCM $\div D_2$')]:
    for i in range(3):
        box(ax, 4 + 16 * i, y, 14, 8, r if i < 2 else 'resultat', label=s[i])
    brace(ax, 4, 34, y, r, q); brace(ax, 36, 50, y, 'resultat', 'reste')
    text(ax, 76, y + 4, L, 'encre', 's')
save(fig, '21-072')
