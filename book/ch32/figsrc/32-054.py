import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
wd, gap = 12.5, 5
x0 = (W - 5 * wd - 4 * gap) / 2
text(ax, 44, 41, 'un pas : le signe change', 'varie', 'm')
for n in range(5):
    x = x0 + n * (wd + gap); cx = x + wd / 2
    role = 'sujet' if n % 2 == 0 else 'varie'
    box(ax, x, 22, wd, 9, role, label=r'$+\alpha$' if n % 2 == 0 else r'$-\alpha$')
    text(ax, cx, 17.5, f'n = {n}', 'encre', 's')
    if n < 4: arrow(ax, (x + wd + 0.4, 26.5), (x + wd + gap - 0.4, 26.5), 'varie')
text(ax, 44, 7, r'$(-1)^n\alpha$ : + − + − +', 'encre', 'm')
save(fig, '32-054')
