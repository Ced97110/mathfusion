import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(62)
text(ax, 44, 57, 'Tous les chats sont noirs', 'sujet', 'm')
for i in range(7):
    ax.add_patch(Circle((8 + 9 * i, 40), 3.8, ec=COL['encre'], fc=COL['encre'], lw=0.8, zorder=2))
ax.add_patch(Circle((76, 40), 3.8, ec=COL['limite'], fc=FILL['encre'], lw=1.6, zorder=2))
brace(ax, 3.5, 66.5, 33, 'fixe', 'chats noirs', down=True)
text(ax, 76, 47, 'un chat blanc', 'limite', 's')
arrow(ax, (76, 35.5), (76, 19), 'limite')
box(ax, 20, 6, 64, 12, 'limite', 'énoncé faux', 'm')
save(fig, '42-067')
