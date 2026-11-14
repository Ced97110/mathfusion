import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
poly(ax, [(3, 10), (33, 10), (33, 48), (3, 48)], 'sujet', fill=False, lw=1.1)
poly(ax, [(42, 10), (86, 10), (86, 48), (42, 48)], 'fixe', fill=False, lw=1.1)
text(ax, 18, 55, r'$C=\{000,\,111\}$', 'sujet', 's')
text(ax, 64, 55, 'autres mots de 3 bits', 'fixe', 's')
for y, w in [(34, '000'), (18, '111')]:
    box(ax, 8, y, 20, 9, 'sujet', label=w)
rest = ['001', '010', '011', '100', '101', '110']
for k, w in enumerate(rest):
    r, c = divmod(k, 2)
    box(ax, 46 + c * 20, 36 - r * 11, 18, 8, 'fixe', label=w)
save(fig, '68-068')
