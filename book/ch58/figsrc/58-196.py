import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# η(e_i) = a_1i f_1 + a_2i f_2 : même forme, nombres qui changent
text(ax, 44, 51, r'$\eta(e_i) = a_{1i} f_1 + a_{2i} f_2$', 'encre', 'm', weight='bold')
rows = [(r'$\eta(e_1)$', '2', '1'), (r'$\eta(e_2)$', '1', '3')]
y = 28
for lab, c1, c2 in rows:
    box(ax, 2, y, 20, 10, 'sujet', label=lab, size='m', r=0.6)
    text(ax, 25, y + 5, '=', 'encre', 'm')
    box(ax, 29, y + 1, 9, 8, 'varie', label=c1, size='m', r=0.5, weight='bold')
    box(ax, 38.5, y + 1, 10, 8, 'autre', label=r'$f_1$', size='m', r=0.5)
    text(ax, 52.5, y + 5, '+', 'encre', 'm')
    box(ax, 56.5, y + 1, 9, 8, 'varie', label=c2, size='m', r=0.5, weight='bold')
    box(ax, 66, y + 1, 10, 8, 'autre', label=r'$f_2$', size='m', r=0.5)
    y -= 15
text(ax, 44, 7, 'les nombres changent, la forme reste', 'varie', 's')
save(fig, '58-196')
