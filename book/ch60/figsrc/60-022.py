import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cw, ch, yt = 10, 7.5, 52
def grid(x0, spec):
    for i in range(4):
        for j in range(3):
            role, lab = spec.get((i, j), ('fixe', None))
            box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, role, label=lab, size='s', r=0.5)
grid(7, {(1, 1): ('sujet', '1'), (2, 2): ('sujet', '2'), (3, 0): ('resultat', '3')})
grid(51, {(0, 1): ('sujet', '1'), (0, 2): ('sujet', '2'), (1, 0): ('fixe', '3'), (0, 0): ('limite', '0')})
text(ax, 22, 62, 'placement par restes', 'resultat', 'm')
text(ax, 66, 62, 'ligne après ligne', 'limite', 'm')
text(ax, 22, 14, '(1, 1) + (2, 2) = (3, 0)\n= case du 3', 'resultat', 's')
text(ax, 66, 14, '(0, 1) + (0, 2) = (0, 0)\ncase du 0, pas du 3', 'limite', 's')
save(fig, '60-022')
