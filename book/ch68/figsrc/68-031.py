import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)

def bits(ax, x, y, s, role, cw, ch=5.5):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, role, label=c, size='m', r=0.5)

cw = 4.6
x0, xw = 3, 46
text(ax, 44, 69, r'$(n,\ k)$', 'encre', 'xl', weight='bold')
text(ax, 27, 62, r'$n$ : mot envoyé', 'sujet', 's')
text(ax, 61, 62, r'$k$ : bloc de message', 'fixe', 's')
arrow(ax, (36, 66.5), (31, 64), 'sujet', lw=0.8)
arrow(ax, (50, 66.5), (56, 64), 'fixe', lw=0.8)
for y, blk, wrd, k, n in [(34, '0', '000', 1, 3), (10, '1000001', '01000001', 7, 8)]:
    text(ax, 3, y + 11.5, r'$(%d,\ %d)$' % (n, k), 'encre', 'm', ha='left', weight='bold')
    bits(ax, x0, y, blk, 'fixe', cw)
    bits(ax, xw, y, wrd, 'sujet', cw)
    arrow(ax, (x0 + k * cw + 1.5, y + 2.75), (xw - 1.5, y + 2.75), 'varie')
    brace(ax, x0, x0 + k * cw, y, 'fixe', label=r'$k = %d$' % k)
    brace(ax, xw, xw + n * cw, y, 'sujet', label=r'$n = %d$' % n)
save(fig, '68-031')
