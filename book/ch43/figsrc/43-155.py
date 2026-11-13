import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, '3 classes de conjugaison', 'encre', 'm')
x = 2.0
for n in (1, 2, 3):
    w = 8 * n + 6
    box(ax, x, 26, w, 16, 'sujet')
    for k in range(n): disc(ax, x + 7 + 8 * k, 34, 3, 'sujet')
    text(ax, x + w / 2, 21, str(n), 'sujet', 'm')
    if n < 3: text(ax, x + w + 4.5, 34, '+', 'encre', 'l')
    x += w + 9
brace(ax, 2, 86, 18, 'resultat', None, depth=2.4)
text(ax, 44, 7, r'$6=1+2+3$', 'resultat', 'l')
save(fig, '43-155')
