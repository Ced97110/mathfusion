import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, r'$p$ de degré 4 se casse en deux facteurs ?', 'sujet', 's')
u = 12.0
x0 = 6
def bar(y, a, b, lab):
    for i in range(a):
        box(ax, x0 + i * u, y, u - 1, 9, 'sujet')
    for i in range(b):
        box(ax, x0 + (a + i) * u, y, u - 1, 9, 'autre')
    text(ax, x0 + a * u / 2 - 0.5, y + 13, f'degré {a}', 'sujet', 's')
    text(ax, x0 + a * u + b * u / 2 - 0.5, y + 13, f'degré {b}', 'autre', 's')
bar(42, 1, 3, '')
bar(14, 2, 2, '')
text(ax, 44, 63, r'$4 = 1+3$ ou $4 = 2+2$', 'varie', 's')
text(ax, 76, 46.5, 'cas 1', 'fixe', 's', ha='center')
text(ax, 76, 18.5, 'cas 2', 'fixe', 's', ha='center')
text(ax, 44, 4, 'deux cas seulement à éliminer', 'resultat', 's')
save(fig, '54-252')
