import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cw, ch, x0, yt = 12, 9, 30, 58
ctr = lambda i, j: (x0 + (j + 0.5) * cw, yt - (i + 0.5) * ch)
for i in range(4):
    for j in range(3):
        ex = (i, j) == (2, 1)
        box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, 'sujet' if ex else 'fixe', label='(2, 1)' if ex else None, size='s', r=0.6)
for i in range(4): text(ax, x0 - 3, ctr(i, 0)[1], str(i), 'sujet', 's')
for j in range(3): text(ax, ctr(0, j)[0], yt + 3, str(j), 'autre', 's')
text(ax, 12, yt - 2 * ch, 'ℤ/4\nlignes', 'sujet', 'm')
text(ax, x0 + 1.5 * cw, yt + 9, 'ℤ/3 : colonnes', 'autre', 'm')
text(ax, 44, 8, 'ℤ/4 ⊕ ℤ/3 : 4 × 3 = 12 cases', 'encre', 'm')
save(fig, '60-005')
