import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, 'taille ÷ taille du bloc = nombre de blocs', 'fixe', 's')
rows = [(36, 2, '12', '24 ÷ 12 = 2 : ℤ/2'),
        (21, 3, '4', '12 ÷ 4 = 3 : ℤ/3'),
        (6, 4, '1', r'4 ÷ 1 = 4 : $V$')]
for y, n, size, right in rows:
    w = 48 / n
    for i in range(n):
        box(ax, 3 + w * i + 0.4, y, w - 0.8, 10, 'sujet', label=size, size='s', r=0.6, lw=0.7)
    text(ax, 55, y + 5, right, 'resultat', 's', ha='left')
save(fig, '64-021')
