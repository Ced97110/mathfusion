import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def chain(ax, H, rows, labels, dec=None, w=54, lw=26):
    ys = [H - 12 - 11 * i for i in range(len(rows))]
    for i, (y, r) in enumerate(zip(ys, rows)):
        role = 'sujet' if i < len(rows) - 1 else 'resultat'
        box(ax, 2, y, w, 8, role, label=r, size='m')
    for i, l in enumerate(labels):
        yc = ys[i + 1] + 4
        role = 'varie' if (dec is None or i == dec) else 'fixe'
        box(ax, 2 + w + 6, yc - 3, lw, 6, role, label=l, size='s')
        arrow(ax, (2 + w + 6, yc), (2 + w, yc), role)

fig, ax = canvas(60)
chain(ax, 60, [r"$I\vee b$", r"$=(b\vee b')\vee b$", r"$=(b\vee b)\vee b'$", r"$=b\vee b'$", r"$=I$"],
      ['A5', 'A1, A2 : décisif', 'idempotence', 'A5'], dec=1)
save(fig, '80-424')
