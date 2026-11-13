import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, v = (1, 2, 3), (4, 5, 6)
fig, ax = canvas(50)
cw, ch, gap = 7, 5.5, 0.6
y0 = 14
centers = [22, 49, 76]
used = [(2, 3), (3, 1), (1, 2)]
calc = [r'$2\times6-3\times5$', r'$3\times4-1\times6$', r'$1\times5-2\times4$']
for pi, (c, (a, b)) in enumerate(zip(centers, used)):
    forgot = ({1, 2, 3} - {a, b}).pop()
    text(ax, c, y0 + 26, f'oublie {forgot}', 'varie', 's')
    for idx in (1, 2, 3):
        y = y0 + (3 - idx) * (ch + gap)
        for col, (x, role) in enumerate([(c - 9, 'sujet'), (c + 2, 'autre')]):
            if idx == forgot:
                box(ax, x, y, cw, ch, 'fixe', fill=False, dash=True, r=0.4, lw=0.6)
            else:
                box(ax, x, y, cw, ch, role, r=0.4)
    text(ax, c, y0 - 4, calc[pi], 'encre', 's')
for idx in (1, 2, 3):
    text(ax, 4.5, y0 + (3 - idx) * (ch + gap) + ch / 2, str(idx), 'fixe', 's')
text(ax, 22 - 5.5, y0 + 21.5, r'$u$', 'sujet', 's')
text(ax, 22 + 5.5, y0 + 21.5, r'$v$', 'autre', 's')
text(ax, 44, 3, 'les indices tournent : 2 3, puis 3 1, puis 1 2', 'encre', 's')
save(fig, '41-111')
