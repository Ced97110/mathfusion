import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def sq(cx, cy, s=8):
    poly(ax, [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)], 'sujet')
def orient(cx, cy, cw, role):
    if cw: arrow(ax, (cx-4, cy-2), (cx+4, cy-2), role, curve=-0.9)
    else: arrow(ax, (cx+4, cy-2), (cx-4, cy-2), role, curve=0.9)
xs = [15, 44, 73]
for x in xs: sq(x, 32)
orient(15, 32, True, 'varie'); orient(44, 32, True, 'resultat'); orient(73, 32, False, 'limite')
arrow(ax, (25, 32), (34, 32), 'encre'); arrow(ax, (54, 32), (63, 32), 'encre')
text(ax, 15, 50, 'départ', 'sujet', 's'); text(ax, 44, 50, 'rotation', 'sujet', 's'); text(ax, 73, 50, 'retournement', 'sujet', 's')
text(ax, 44, 18, '0 : garde le sens', 'resultat', 's'); text(ax, 73, 18, '1 : inverse', 'limite', 's')
text(ax, 44, 6, r'$D_4/\langle r\rangle=\{0,\,1\}$', 'varie', 'm')
save(fig, '47-210')
