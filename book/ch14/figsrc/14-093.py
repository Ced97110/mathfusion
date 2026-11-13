import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, r'marches de la base 0 : $0^n$', 'sujet', 'm')
w, p, x0 = 11, 13.5, 6
for i, n in enumerate(range(-2, 4)):
    x = x0 + i * p
    if n < 0: box(ax, x, 26, w, 14, 'limite', fill=False, dash=True)
    elif n == 0: box(ax, x, 26, w, 14, 'limite', label='?', size='l')
    else: box(ax, x, 26, w, 14, 'sujet', label='0', size='l')
    text(ax, x + w / 2, 21, f'$n = {n}$'.replace('-', '$-$') if False else f'$n = {n}$', 'fixe', 's')
brace(ax, x0, x0 + p + w, 44, 'limite', "n'existe pas", down=False, depth=1.4)
brace(ax, x0 + 2 * p, x0 + 2 * p + w, 44, 'limite', 'non défini', down=False, depth=1.4)
brace(ax, x0 + 3 * p, x0 + 5 * p + w, 44, 'sujet', 'vaut 0', down=False, depth=1.4)
text(ax, 44, 8, r'$0^{-2}$ : diviser 1 par 0', 'limite', 's')
save(fig, '14-093')
