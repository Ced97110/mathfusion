import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
w = 11; h = 9; pitch = 13.2
G, H, Gi, Hi = r'$g$', r'$h$', r'$g^{-1}$', r'$h^{-1}$'
def row(y, items, x0):
    for i, (lab, role) in enumerate(items):
        box(ax, x0 + i * pitch, y, w, h, role, label=lab, size='m')
x0a = (88 - (6 * pitch - (pitch - w))) / 2
row1 = [(H, 'sujet'), (G, 'sujet'), (Gi, 'varie'), (Hi, 'sujet'), (G, 'sujet'), (H, 'sujet')]
row1[1] = (G, 'sujet'); row1[2] = (Gi, 'sujet')
# step 1: pair g, g^-1 (positions 1,2) cancels
row1 = [(H, 'fixe'), (G, 'varie'), (Gi, 'varie'), (Hi, 'sujet'), (G, 'sujet'), (H, 'sujet')]
row(46, row1, x0a)
brace(ax, x0a, x0a + 2 * pitch - (pitch - w), 57, 'fixe', label=r'$hg$', down=False)
brace(ax, x0a + 2 * pitch, x0a + 6 * pitch - (pitch - w), 57, 'sujet', label=r'commutateur $(g,h)$', down=False)
x0b = (88 - (4 * pitch - (pitch - w))) / 2
row2 = [(H, 'varie'), (Hi, 'varie'), (G, 'sujet'), (H, 'sujet')]
row(26, row2, x0b)
x0c = (88 - (2 * pitch - (pitch - w))) / 2
row(6, [(G, 'resultat'), (H, 'resultat')], x0c)
arrow(ax, (44, 44.5), (44, 36.5), 'varie')
arrow(ax, (44, 24.5), (44, 16.5), 'varie')
save(fig, '64-061')
