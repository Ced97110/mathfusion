import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'F[λ] : λ² − 2λ + 1', 'encre', 'l')
y = 30
terms = [('1', 'λ²'), ('−2', 'λ'), ('1', None)]
x = 10
for i, (c, p) in enumerate(terms):
    if i:
        text(ax, x + 3, y + 5, '+', 'encre', 'l')
        x += 8
    box(ax, x, y, 9, 10, 'sujet', label=c, size='m')
    x += 9
    if p:
        box(ax, x, y, 9, 10, 'varie', label=p, size='m')
        x += 9
    x += 3
text(ax, 26, 18, 'coefficients dans F', 'sujet', 's')
text(ax, 62, 18, 'puissances de λ', 'varie', 's')
save(fig, '60-083')
