import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 32, 63, r'$6(x+3)$', 'sujet', 'l'); text(ax, 68, 63, r'$6x+18$', 'sujet', 'l')
rows = [('2', r'$6\times5=30$', r'$12+18=30$'), ('5', r'$6\times8=48$', r'$30+18=48$'), ('0', r'$6\times3=18$', r'$0+18=18$')]
for i, (x, l, r) in enumerate(rows):
    y = 44 - i * 15
    box(ax, 2, y - 6, 84, 12, 'resultat')
    text(ax, 10, y, r'$x=' + x + r'$', 'varie', 'm')
    text(ax, 32, y, l, 'encre', 'm'); text(ax, 50, y, '=', 'resultat', 'l'); text(ax, 68, y, r, 'encre', 'm')
save(fig, '12-138')
