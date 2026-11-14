import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 20, 84, 'morceau', 'sujet', 'm', weight='bold'); text(ax, 62, 84, 'étape de la preuve', 'varie', 'm', weight='bold')
P = [(r'$-b$', r'on a retiré $\frac{b}{2a}$'), (r'$2a$', r'dénominateur de $\frac{b}{2a}$'), (r'$b^2$', 'carré de la moitié'), (r'$-4ac$', r'$-\frac{c}{a}=-\frac{4ac}{4a^2}$')]
for i, (a, b) in enumerate(P):
    y = 60 - i*19
    box(ax, 4, y, 32, 14, 'sujet', label=a, size='l'); box(ax, 46, y, 40, 14, 'varie', label=b, size='s')
    arrow(ax, (45.5, y+7), (36.5, y+7), 'fixe')
save(fig, '23-061')
