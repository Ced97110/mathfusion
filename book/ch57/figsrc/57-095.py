import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 54, 62, 'départ : (2 ; 1)', 'encre', 'm')
cols = [('quart de tour', '(−2 ; 4)', '(−2 ; 4)', True),
        ('décaler de 1', '(5 ; 2)', '(6 ; 2)', False),
        ('doubler', '(8 ; 4)', '(8 ; 4)', True)]
text(ax, 11, 39, '× 2 puis\nla règle', 'fixe', 's')
text(ax, 11, 15, 'la règle\npuis × 2', 'fixe', 's')
for i, (h, a, b, ok) in enumerate(cols):
    x = 22 + 22 * i
    role = 'resultat' if ok else 'limite'
    box(ax, x, 48, 20, 9, 'sujet', label=h, size='s')
    box(ax, x, 34, 20, 10, role, label=a)
    box(ax, x, 10, 20, 10, role, label=b)
    xc = x + 10
    line(ax, [(xc - 3, 28), (xc + 3, 28)], role, lw=1.2)
    line(ax, [(xc - 3, 26), (xc + 3, 26)], role, lw=1.2)
    if not ok:
        line(ax, [(xc - 1.6, 24.4), (xc + 1.6, 29.6)], role, lw=1.2)
save(fig, '57-095')
