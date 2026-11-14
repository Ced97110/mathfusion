import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cl = ['sujet', 'varie', 'resultat']
def row(y, m, n, head, cap1, cap2):
    text(ax, 44, y + 18, head, 'encre', 'm')
    N = m * n; w = 6.2; g = 0.5; x0 = 44 - (N * (w + g) - g) / 2
    for i in range(N):
        box(ax, x0 + i * (w + g), y, w, 9, cl[i % m], r=0.5, lw=0.7)
    text(ax, 44, y - 5, cap1, 'sujet', 's'); text(ax, 44, y - 11, cap2, 'encre', 's')
row(56, 3, 4, r'$m = 3$, $n = 4$ : 12 positions', r'bleu : 4 cases ($n$ éléments)', r'couleurs : 3 ($m$ éléments)')
row(16, 2, 5, r'$m = 2$, $n = 5$ : 10 positions', r'bleu : 5 cases ($n$ éléments)', r'couleurs : 2 ($m$ éléments)')
save(fig, '48-171')
