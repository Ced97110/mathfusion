import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
pick = [1, 0, 0, 1, 1, 0, 1, 0]
x0, dx = 14, 9
text(ax, 44, 74, '8 suites d’entrée', 'sujet', 'm')
for i in range(8):
    x = x0 + dx * i
    box(ax, x - 3.5, 40, 7, 26, 'fixe', fill=False, lw=0.6, r=0.6)
    for v, y in [(1, 58), (0, 46)]:
        disc(ax, x, y, 2.6, 'varie' if pick[i] == v else 'fixe')
text(ax, 5, 58, '1', 'encre', 'm'); text(ax, 5, 46, '0', 'encre', 'm')
brace(ax, x0 - 3.5, x0 + dx * 7 + 3.5, 38, 'varie', r'$2\times2\times\cdots\times2$ (8 facteurs)')
text(ax, 44, 22, r'2 choix par suite : $2^{8}=256$', 'resultat', 'l')
text(ax, 44, 10, r'4 fils : 16 suites, $2^{16}=65\,536$', 'autre', 'm')
save(fig, '49-260')
