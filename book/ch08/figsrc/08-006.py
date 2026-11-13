import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
w0, x0 = 15, 6.5
vals = ['100', '10', '1', r'$\frac{1}{10}$', r'$\frac{1}{100}$']
digs = ['', '', '2', '3', '5']
for i, (v, d) in enumerate(zip(vals, digs)):
    role = 'fixe' if i < 3 else 'varie'
    x = x0 + w0 * i
    box(ax, x, 34, w0, 12, role, label=d if d else None, size='l')
    text(ax, x + w0 / 2, 51, v, role, 's')
brace(ax, x0 + 0.5, x0 + 3 * w0 - 0.5, 33, 'fixe', label='positions connues')
brace(ax, x0 + 3 * w0 + 0.5, x0 + 5 * w0 - 0.5, 33, 'varie', label='prolongées')
arrow(ax, (x0 + 2.5 * w0, 58), (x0 + 5 * w0 + 4, 58), 'varie')
text(ax, 64, 64, 'on continue vers la droite', 'varie', 's')
save(fig, '08-006')
