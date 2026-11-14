import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 3, 6, 82, 40, 'sujet', fill=False, dash=True)
text(ax, 44, 59, r'$R/I$ : « $R$ modulo $I$ »', 'sujet', 'l')
text(ax, 44, 52, r'avec $R=\mathbb{Z}$ et $I=4\mathbb{Z}$', 'fixe', 's')
for i in range(4):
    x = 6 + i * 20.2
    box(ax, x, 14, 17, 26, 'sujet', label=None)
    text(ax, x + 8.5, 34, r'$\bar{%d}$' % i, 'sujet', 'l')
    for j, v in enumerate((i, i + 4, i + 8)):
        text(ax, x + 8.5, 27 - j * 5, str(v), 'fixe', 's')
text(ax, 44, 9.5, 'l’ensemble de toutes les classes', 'sujet', 's')
save(fig, '52-067')
