import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(95)
text(ax, 44, 90, '8 éléments en 3 classes égales ?', 'limite', 's')
x = 3
for n in (3, 3, 2):
    w = n * 7 + 1
    box(ax, x, 70, w, 12, 'limite')
    for k in range(n): disc(ax, x + 4.5 + 7 * k, 76, 2.5, 'limite')
    x += w + 3
text(ax, 44, 63, 'tailles 3, 3, 2 : inégales', 'limite', 's')
text(ax, 44, 50, "tailles d'orbite possibles", 'encre', 's')
f = numberline(ax, 8, 80, 30, 1, 8, arrow_right=False)
for v in range(1, 9):
    ok = v in (1, 2, 4, 8)
    disc(ax, f(v), 38, 2.8, 'resultat' if ok else 'limite', fill=ok)
text(ax, 44, 14, '1, 2, 4, 8 divisent 8', 'resultat', 's')
text(ax, 44, 7, '3, 5, 6, 7 : impossibles', 'limite', 's')
save(fig, '49-168')
