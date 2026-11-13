import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 17, 56, 'préfixe + base', 'sujet', 's')
text(ax, 66, 56, 'valeur + base', 'resultat', 's')
rows = [('1 km', '1 000', 'm'), ('1 cm', '0,01', 'm'), ('1 mg', '0,001', 'g')]
for i, (a, v, b) in enumerate(rows):
    y = 38 - i * 16
    box(ax, 4, y, 26, 10, 'sujet', label=a)
    text(ax, 38, y + 5, '=', 'encre', 'l')
    box(ax, 46, y, 24, 10, 'varie', label=v)
    box(ax, 72, y, 12, 10, 'fixe', label=b)
save(fig, '11-044')
