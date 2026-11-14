import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
x0, y0, cw, ch = 4, 6, 14, 12
box(ax, x0, y0 + 2 * ch, cw, ch, 'fixe', label=r'$\times$')
heads = [r'$+$', r'$-$']
for j in range(2):
    box(ax, x0 + (j + 1) * cw, y0 + 2 * ch, cw, ch, 'fixe', label=heads[j], weight='bold')
    box(ax, x0, y0 + (1 - j) * ch, cw, ch, 'fixe', label=heads[j], weight='bold')
for i in range(2):
    for j in range(2):
        same = i == j
        box(ax, x0 + (j + 1) * cw, y0 + (1 - i) * ch, cw, ch, 'sujet' if same else 'varie',
            label=r'$+$' if same else r'$-$', size='l', weight='bold')
box(ax, 54, 30, 4, 4, 'sujet')
text(ax, 61, 32, 'même signe : $+$', 'sujet', 's', ha='left')
box(ax, 54, 18, 4, 4, 'varie')
text(ax, 61, 20, 'signes contraires : $-$', 'varie', 's', ha='left')
save(fig, '13-080')
