import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
k, x0, h = 2.0, 8, 8          # 1 unité = 2 mm
def bar(x, y, w, role, label=None, dash=False, fill=True):
    box(ax, x, y, w, h, role, label=label, size='s', dash=dash, fill=fill, r=0.6)
text(ax, 8, 49, 'angle droit : Pythagore', 'fixe', 's', ha='left')
bar(x0, 37, 30 * k, 'fixe', r'$10+20=30$')
text(ax, 8, 27, 'angle de $45^\\circ$ : le vrai carré', 'varie', 's', ha='left')
bar(x0, 15, 10 * k, 'varie', '10')
bar(x0 + 10 * k, 15, 20 * k, 'sujet', r'$-2\,u\cdot v=-20$', dash=True)
brace(ax, x0 + 10 * k, x0 + 30 * k, 14, 'sujet', label='correction', down=True, depth=1.6)
arrow(ax, (x0 + 24 * k, 36), (x0 + 24 * k, 24), 'fixe', lw=0.7)
text(ax, 44, 3, 'angle aigu : correction $<0$', 'sujet', 's')
save(fig, '41-086')
