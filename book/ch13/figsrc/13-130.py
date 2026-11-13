import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for x, a, b in [(22, '12 ÷ 0', r'$0 \neq 12$'), (66, '−12 ÷ 0', r'$0 \neq -12$')]:
    box(ax, x - 15, 46, 30, 9, 'sujet', label=a)
    arrow(ax, (x, 45), (x, 36), 'varie')
    box(ax, x - 15, 27, 30, 9, 'fixe', label=r'$0 \times c = 0$')
    arrow(ax, (x, 26), (x, 17), 'limite')
    box(ax, x - 15, 8, 30, 9, 'limite', label=b)
text(ax, 44, 59, 'le signe ne change rien', 'fixe', 's')
save(fig, '13-130')
