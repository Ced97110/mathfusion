import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cw, ch = 11.0, 9.0
for r in range(3):
    y = 38 - r * 14
    text(ax, 14, y + ch / 2, r'$e_%d$' % (r + 1), 'sujet', 'l')
    for c in range(3):
        one = (c == r)
        box(ax, 28 + c * cw, y, cw, ch, 'sujet' if one else 'fixe', label='1' if one else '0', r=0.6, weight='bold' if one else 'normal')
text(ax, 63, 38 + ch / 2, 'riz', 'fixe', 's', ha='left')
text(ax, 63, 24 + ch / 2, 'lentilles', 'fixe', 's', ha='left')
text(ax, 63, 10 + ch / 2, 'sel', 'fixe', 's', ha='left')
text(ax, 44, 4, r'le 1 est en position $i$', 'sujet', 's')
text(ax, 44, 52, 'trois cases', 'fixe', 's')
save(fig, '58-040')
