import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'un polynôme en $y$ : $(1+x)+2x\,y$', 'sujet', 'm')
data = [(r'terme sans $y$', r'$1+x$'), (r'terme en $y$', r'$2x$')]
for i, (outer, inner) in enumerate(data):
    x0 = 5 + i * 42
    box(ax, x0, 14, 36, 34, 'sujet')
    text(ax, x0 + 18, 43, outer, 'sujet', 's')
    box(ax, x0 + 6, 19, 24, 14, 'varie', label=inner, size='l')
text(ax, 44, 7, r'chaque coefficient est un polynôme en $x$', 'varie', 's')
save(fig, '54-117')
