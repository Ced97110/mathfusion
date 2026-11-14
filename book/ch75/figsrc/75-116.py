import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, ch = 8.5, 5.5
x0, y0 = 6, 12
for c in range(8):
    for r in range(6):
        box(ax, x0 + c * cw, y0 + r * ch, cw, ch, 'resultat' if c < 4 else 'fixe', r=0.3, lw=0.4)
brace(ax, x0, x0 + 8 * cw, y0 + 6 * ch + 1, label='48 tableaux inversibles', down=False)
text(ax, x0 + 2 * cw, 6, '24 : det = 1', 'resultat', 's'); text(ax, x0 + 6 * cw, 6, '24 : det = 2', 'fixe', 's')
text(ax, 44, 59, r'$48 \div 2 = 24$', 'varie', 'l')
save(fig, '75-116')
