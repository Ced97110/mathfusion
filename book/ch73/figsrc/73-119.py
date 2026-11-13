import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for i in range(5):
    disc(ax, 12 + 16 * i, 30, 5, 'limite' if i == 0 else 'sujet', fill=(i != 0), label=str(i))
text(ax, 12, 40, 'retiré', 'limite', 's')
arrow(ax, (44, 36), (60, 36), 'varie', curve=-0.5, both=True); text(ax, 52, 47, 'inverses', 'varie', 's')
brace(ax, 28, 76, 24, 'sujet', label=r'$F^*$ = $F$ sans 0')
text(ax, 44, 6, r'$F$ : restes de ÷ 5', 'fixe', 's')
save(fig, '73-119')
