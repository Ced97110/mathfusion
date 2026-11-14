import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, '2 mots envoyés', 'encre', 's')
for x, a, b, r in [(6, '0', '000', 'sujet'), (50, '1', '111', 'varie')]:
    box(ax, x, 48, 10, 9, r, label=a, size='l')
    arrow(ax, (x + 10.5, 52.5), (x + 16.5, 52.5), r)
    box(ax, x + 17, 48, 16, 9, r, label=b, size='l')
text(ax, 44, 40, '8 mots reçus possibles : $2\\times2\\times2$', 'encre', 'm')
words = ['000', '001', '010', '011', '100', '101', '110', '111']
for k, wd in enumerate(words):
    r = 'sujet' if wd == '000' else 'varie' if wd == '111' else 'fixe'
    box(ax, 3.5 + (k % 4) * 21, 26 - (k // 4) * 12, 18, 8, r, label=wd, size='m')
save(fig, '68-013')
