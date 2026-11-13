import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, r'$I$ : multiples de 4', 'fixe', 'm')
text(ax, 44, 52, r'$3+I$ : la classe de 3', 'sujet', 'm')
f = numberline(ax, 8, 72, 33, -4, 12, labels=False, arrow_right=False)
for v in (-4, 0, 4, 8, 12):
    disc(ax, f(v), 33, 1.7, 'fixe')
    text(ax, f(v), 40, f'{v}'.replace('-', '−'), 'fixe', 's')
for v in (-4, 0, 4, 8):
    arrow(ax, (f(v) + 1.5, 31.5), (f(v + 3) - 1.5, 31.5), 'varie', curve=0.5)
for v in (-1, 3, 7, 11):
    disc(ax, f(v), 33, 1.7, 'sujet')
    text(ax, f(v), 17, f'{v}'.replace('-', '−'), 'sujet', 's')
text(ax, f(5.5), 23.5, r'$+\,3$', 'varie', 's')
save(fig, '52-065')
