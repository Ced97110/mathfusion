import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
text(ax, 44, 100, 'gN = Ng pour chaque g ?', 'encre', 'm')
text(ax, 12, 92, 'g', 'encre', 'm')
text(ax, 42, 92, 'N : rotations', 'sujet', 's')
text(ax, 72, 92, 'H = {1, s}', 'autre', 's')
names = ['1', 'r', 'r²', 'r³', 's', 'rs', 'r²s', 'r³s']
okH = [True, False, True, False, True, False, True, False]
def mark(x, y, ok):
    role = 'resultat' if ok else 'limite'
    disc(ax, x, y, 2.8, role)
    if ok: line(ax, [(x - 1.3, y), (x - 0.3, y - 1.2), (x + 1.5, y + 1.4)], role, lw=1.1)
    else:
        line(ax, [(x - 1.2, y - 1.2), (x + 1.2, y + 1.2)], role, lw=1.1); line(ax, [(x - 1.2, y + 1.2), (x + 1.2, y - 1.2)], role, lw=1.1)
for i, n in enumerate(names):
    y = 82 - 8 * i
    text(ax, 12, y, n, 'encre', 'm')
    mark(42, y, True); mark(72, y, okH[i])
text(ax, 42, 14, 'normal', 'resultat', 'm')
text(ax, 72, 14, 'pas normal', 'limite', 'm')
save(fig, '47-122')
