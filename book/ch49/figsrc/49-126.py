import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cols = [(15, r'$GL$', 'sujet', 'inversibles'), (44, '2', 'varie', '2 lignes, 2 col.'), (73, r'$(\mathbb{R})$', 'autre', 'nombres réels')]
for x, s, role, cap in cols:
    box(ax, x - 13, 44, 26, 14, role, label=s, size='l')
    text(ax, x, 38, cap, role, 's')
text(ax, 15, 24, r'$\det\neq 0$', 'sujet', 'm')
for i in range(2):
    for j in range(2):
        box(ax, 36 + j * 9, 14 + (1 - i) * 9, 8, 8, 'varie', r=0.4)
f = numberline(ax, 62, 84, 20, -1, 1, step=1, arrow_right=False, role='autre')
save(fig, '49-126')
