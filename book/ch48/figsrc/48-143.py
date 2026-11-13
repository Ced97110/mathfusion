import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cx = [29, 42, 55, 68, 80]
top = ['2', '+', '3', '=', '5']; bot = ['7,389', '×', '20,086', '=', '148,41']
for i, (a, b) in enumerate(zip(top, bot)):
    if i % 2 == 0:
        box(ax, cx[i] - 6.5, 34, 13, 9, 'sujet', label=a, size='m')
        box(ax, cx[i] - 6.5, 8, 13, 9, 'autre' if i < 4 else 'resultat', label=b, size='s')
        arrow(ax, (cx[i], 34), (cx[i], 17.8), 'varie')
        text(ax, cx[i] + 5, 26, 'exp', 'varie', 's')
    else:
        text(ax, cx[i], 38.5, a, 'encre', 'l'); text(ax, cx[i], 12.5, b, 'encre', 'l')
text(ax, 9, 38.5, '(ℝ, +)', 'sujet', 's'); text(ax, 9, 12.5, '(ℝ>0, ×)', 'autre', 's')
save(fig, '48-143')
