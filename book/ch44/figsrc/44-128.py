import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
rows = [('ℤ', '5', '−5'), ('ℚ', r'$\frac{1}{2}$', r'$-\frac{1}{2}$'), ('ℝ', r'$a$', r'$-a$')]
for k, (S, a, o) in enumerate(rows):
    y = 30 - k * 15
    box(ax, 2, y, 12, 11, 'fixe', label=S, size='l')
    box(ax, 22, y, 14, 11, 'sujet', label=a)
    text(ax, 42, y + 5.5, '+', 'encre', 'l')
    box(ax, 48, y, 16, 11, 'varie', label=o)
    text(ax, 69, y + 5.5, '=', 'encre', 'l')
    box(ax, 74, y, 12, 11, 'resultat', label='0')
text(ax, 29, 46, 'nombre', 'sujet', 's'); text(ax, 56, 46, 'son opposé', 'varie', 's'); text(ax, 80, 46, 'neutre', 'resultat', 's')
save(fig, '44-128')
