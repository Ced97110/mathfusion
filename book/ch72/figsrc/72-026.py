import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, vals, name):
    text(ax, 16, y + 5, name, 'encre', 's')
    x0 = 40
    for i, v in enumerate(vals): box(ax, x0 + i*14, y, 12, 10, 'sujet', label=v, size='l')
    return x0, len(vals)
x0, n = row(50, ['2', '1'], 'plan'); brace(ax, x0, x0 + 14*n - 2, 48, 'sujet', r'$n=2$ nombres')
x0, n = row(18, ['2', '1', '5'], 'espace'); brace(ax, x0, x0 + 14*n - 2, 16, 'sujet', r'$n=3$ nombres')
text(ax, 62, 66, r'chaque case : un nombre de $F$', 'varie', 's')
save(fig, '72-026')
