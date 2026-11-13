import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def bar(ax, x0, y, cw, n, k, on, thick, h=8):
    for i in range(15):
        r = on if i < k else 'fixe'
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL['fixe'], fc=FILL[r], lw=0.4, zorder=2))
    for i in range(0, 16, 15 // n):
        line(ax, [(x0 + i * cw, y - 1), (x0 + i * cw, y + h + 1)], on, lw=1.3)
fig, ax = canvas(74)
x0, cw = 6.5, 5.0
text(ax, x0, 66, r'$2\times5=10$ sur 15', 'sujet', 'm', ha='left')
bar(ax, x0, 52, cw, 3, 10, 'sujet', True)
text(ax, x0, 43, r'$3\times3=9$ sur 15', 'autre', 'm', ha='left')
bar(ax, x0, 29, cw, 5, 9, 'autre', True)
text(ax, 84, 62, r'$\frac{2}{3}$', 'sujet', 'm', ha='right')
text(ax, 84, 39, r'$\frac{3}{5}$', 'autre', 'm', ha='right')
brace(ax, x0, x0 + 15 * cw, 26, 'resultat', 'même nombre de parts : 15', down=True)
save(fig, '07-059')
