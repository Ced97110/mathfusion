import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def table(x0, bottom, role, title):
    for i in range(3):
        x = x0 + i * 12
        disc(ax, x, 40, 3.4, 'sujet', label=str(i + 1), size='s')
        disc(ax, x, 16, 3.4, role, label=str(bottom[i]), size='s')
        arrow(ax, (x, 36.6), (x + 12 * (bottom[i] - 1 - i) * 0.0 + (bottom[i] - i - 1) * 12 * 1.0, 19.4), role, lw=0.8)
    text(ax, x0 + 12, 52, title, role, 's')
table(10, [2, 3, 1], 'resultat', 'chaque nombre une fois')
table(54, [1, 1, 3], 'limite', '1 deux fois, 2 jamais')
save(fig, '44-119')
