import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(48, '135'), (36, '1305'), (24, '13005')]
for y, s in rows:
    n = len(s)
    for k, ch in enumerate(s):
        x = 46 - 8 * (n - 1 - k)
        if ch == '0':
            box(ax, x, y, 8, 8, 'fixe', fill=False, label=ch, size='m')
        else:
            box(ax, x, y, 8, 8, 'sujet', fill=True, label=ch, size='m')
    arrow(ax, (55, y + 4), (63, y + 4), 'varie')
box(ax, 64, 24, 20, 32, 'resultat', label='somme : 9', size='l')
text(ax, 44, 12, 'donc divisible par 9 (ch. 3)', 'resultat', 'm')
save(fig, '01-150')
