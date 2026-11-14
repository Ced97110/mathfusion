import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'deux nombres, trois cas', 'encre', 'm')
for y, a, b, lab in ((46, 5, 5, '$a = b$'), (28, 7, 4, '$a > b$'), (10, 4, 7, '$a < b$')):
    f = numberline(ax, 4, 52, y, 0, 8, labels=False, arrow_right=False, tick=0.8)
    disc(ax, f(a), y + 4, 2.4, 'sujet', label='$a$', size='s')
    disc(ax, f(b), y - 4, 2.4, 'autre', label='$b$', size='s')
    box(ax, 62, y - 5, 22, 10, 'fixe', label=lab)
save(fig, '12-030')
