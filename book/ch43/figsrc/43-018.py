import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, cw = 8, 6.0
ys = [10 + i*9 for i in range(4)]
for c in range(12):
    hl = c == 3
    box(ax, x0 + c*cw, 8, cw - 0.8, 38, 'sujet' if hl else 'fixe', r=0.4)
    for y in ys:
        if not hl: disc(ax, x0 + c*cw + (cw-0.8)/2, y + 4, 0.9, 'fixe')
for n, y in zip((-9, 3, 15, 27), ys):
    text(ax, x0 + 3*cw + (cw-0.8)/2, y + 4, str(n).replace('-', '−'), 'sujet', 's')
text(ax, x0 + 3*cw + (cw-0.8)/2, 49.5, '⋮', 'sujet', 'm')
text(ax, x0 + 3*cw + (cw-0.8)/2, 5.0, '⋮', 'sujet', 'm')
for c, lab in ((0, '0'), (3, '3'), (11, '11')):
    pass
brace(ax, x0, x0 + 12*cw - 0.8, 56, 'fixe', '12 blocs', down=False)
text(ax, 44, 66, 'chaque bloc est infini', 'sujet', 's')
save(fig, '43-018')
