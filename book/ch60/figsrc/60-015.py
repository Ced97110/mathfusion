import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cw, ch, x0, yt = 14, 10, 30, 56
for i in range(4):
    for j in range(3):
        v = next(x for x in range(12) if x % 4 == i and x % 3 == j)
        box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, 'varie' if v == 7 else 'sujet', label=str(v), size='m', r=0.6, weight='bold' if v == 7 else 'normal')
text(ax, x0 - 2, yt - 3.5 * ch, 'ligne 3\n(reste de 7 ÷ 4)', 'varie', 's', ha='right')
text(ax, x0 + 1.5 * cw, yt + 6, 'colonne 1 (reste de 7 ÷ 3)', 'varie', 's')
save(fig, '60-015')
