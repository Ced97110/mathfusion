import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cw, ch, x0, yt = 11, 8, 50, 54
ctr = lambda i, j: (x0 + (j + 0.5) * cw, yt - (i + 0.5) * ch)
for i in range(4):
    for j in range(3):
        ex = (i, j) == (2, 1)
        box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, 'varie' if ex else 'fixe', label='10' if ex else None, size='s', r=0.6)
for i in range(4): text(ax, x0 - 3.5, ctr(i, 0)[1], str(i), 'varie' if i == 2 else 'fixe', 's')
for j in range(3): text(ax, ctr(0, j)[0], yt + 4, str(j), 'varie' if j == 1 else 'fixe', 's')
box(ax, 2, 45, 10, 10, 'sujet', label='10', size='l')
box(ax, 15, 30, 25, 8, 'sujet', label='÷ 4 : reste 2', size='s')
box(ax, 15, 62, 25, 8, 'sujet', label='÷ 3 : reste 1', size='s')
arrow(ax, (12, 47), (15, 37), 'sujet'); arrow(ax, (12, 53), (15, 63), 'sujet')
arrow(ax, (40, 34), (45.5, 34), 'varie')
arrow(ax, (40, 66), (ctr(0, 1)[0] - 2, yt + 6.5), 'varie')
save(fig, '60-016')
