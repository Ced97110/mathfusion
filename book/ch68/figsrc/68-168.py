import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(102)
text(ax, 44, 98, r'code $(5, 2)$ de Judson', 'encre', 'm')
box(ax, 3, 72, 82, 22, 'sujet', fill=False)
for k, eq in enumerate([r'$x_2 + x_3 = 0$', r'$x_1 + x_4 = 0$', r'$x_1 + x_2 + x_5 = 0$']):
    text(ax, 44, 88 - k * 6.5, eq, 'sujet', 'm')
words = ['00000', '01101', '10011', '11110']
for k, wd in enumerate(words):
    x = 3 + k * 21
    role = 'sujet' if wd in ('01101', '10011') else 'fixe'
    box(ax, x, 46, 19, 8, role, label=wd)
    text(ax, x + 9.5, 40, 'mot nul' if k == 0 else f'poids {wd.count("1")}', role, 's')
arrow(ax, (44, 71), (44, 55.5), 'fixe')
text(ax, 47, 63, 'les mots qui les vérifient', 'fixe', 's', ha='left')
arrow(ax, (44, 36), (44, 30), 'fixe')
text(ax, 47, 33, 'plus petit poids non nul', 'fixe', 's', ha='left')
text(ax, 44, 25, r'$d = 3$, donc $t = 1$', 'resultat', 'l')
text(ax, 44, 11, r'$2^5 \div 2^2 = 8$ classes', 'resultat', 'm')
arrow(ax, (44, 20), (44, 16), 'fixe')
save(fig, '68-168')
