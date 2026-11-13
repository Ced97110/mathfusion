import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, r'écart $=$ 90° $-$ angle', 'sujet', 's', weight='bold')
text(ax, 8, 36, 'écart\nà 90°', 'sujet', 's'); text(ax, 8, 16, 'tangente', 'sujet', 's')
def panel(x0, role, head, e, t, ratio):
    text(ax, x0 + 15, 46, head, role, 's', weight='bold')
    for i in range(2):
        bx = x0 + i * 20
        box(ax, bx, 32, 12, 8, role, label=e[i], size='s')
        box(ax, bx, 12, 12, 8, role, label=t[i], size='s')
    arrow(ax, (x0 + 13, 36), (x0 + 19, 36), 'varie'); text(ax, x0 + 16, 42, '÷ 10', 'varie', 's')
    arrow(ax, (x0 + 13, 16), (x0 + 19, 16), 'varie'); text(ax, x0 + 16, 7, ratio, role, 's', weight='bold')
panel(17, 'resultat', 'petit écart', ['10°', '1°'], ['5,6713', '57,29'], '× 10,1')
panel(54, 'limite', 'grand écart', ['60°', '6°'], ['0,5774', '9,5144'], '× 16,5')
save(fig, '25-123')
