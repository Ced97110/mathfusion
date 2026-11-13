import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(56)
text(ax, 40, 50, 'bonne preuve', 'resultat', 's'); text(ax, 66, 50, 'preuve fautive', 'limite', 's')
for y, a, v1, v2, nt, role in ((28, '30°', '1,73', '3,73', 'différent : faute vue', 'resultat'), (6, '45°', '2,41', '2,41', 'égal : faute cachée', 'limite')):
    text(ax, 8, y + 7, a, 'encre', 'l', weight='bold')
    lbox(ax, 28, y + 1, 24, 12, 'resultat', v1.replace(',', '{,}').join(('$', '$'))); lbox(ax, 54, y + 1, 24, 12, 'limite', v2.replace(',', '{,}').join(('$', '$')))
    text(ax, 53, y - 2.5, nt, role, 's')
save(fig, '31-133')
