import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$\mu(k)$ vaut 1, $-1$ ou 0', 'sujet', 'm')
rows = [('6', r'$2\times3$ : deux premiers', r'$\mu(6)=1$'),
        ('7', 'un seul premier', r'$\mu(7)=-1$'),
        ('12', r'divisible par $4=2^2$', r'$\mu(12)=0$')]
for i, (n, d, v) in enumerate(rows):
    y = 38 - 16 * i
    box(ax, 3, y, 12, 11, 'fixe', label=n)
    arrow(ax, (15, y + 5.5), (22, y + 5.5), 'fixe')
    box(ax, 22, y, 36, 11, 'fixe', label=d, size='s')
    arrow(ax, (58, y + 5.5), (66, y + 5.5), 'sujet')
    box(ax, 66, y, 20, 11, 'sujet', label=v, size='s')
save(fig, '67-056')
