import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, 'rang 2 du produit de deux suites', 'encre', 'm')
text(ax, 11, 26, r'$\sum$', 'sujet', 32)
text(ax, 11, 8, 'somme', 'sujet', 's')
terms = [r'$a_0b_2$', r'$a_1b_1$', r'$a_2b_0$']
x0, w, gap = 26, 16, 6
for i, t in enumerate(terms):
    x = x0 + i * (w + gap)
    box(ax, x, 22, w, 10, 'varie', label=t, size='m')
    if i < 2:
        text(ax, x + w + gap / 2, 27, '+', 'encre', 'l')
brace(ax, x0, x0 + 3 * w + 2 * gap, 20, 'varie', label=r'$j+k=2$', depth=2.0)
text(ax, 56, 7, r'une ligne pour tout rang $i$ :', 'encre', 's')
text(ax, 56, 2.5, r'$\sum a_jb_k$ avec $j+k=i$', 'sujet', 's')
save(fig, '54-088')
