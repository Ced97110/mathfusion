import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# bits order: haut-gauche, haut-droite, bas-droite, bas-gauche ; 1 = orange, 0 = bleu
def pions(ax, cx, cy, s, bits, frame='fixe'):
    box(ax, cx - s / 2, cy - s / 2, s, s, frame, r=0.6, lw=0.8)
    d = s * 0.27
    for (dx, dy), b in zip([(-1, 1), (1, 1), (1, -1), (-1, -1)], bits):
        disc(ax, cx + dx * d, cy + dy * d, s * 0.16, 'varie' if b else 'sujet')
def rot(b, k=1):
    for _ in range(k % 4): b = (b[3], b[0], b[1], b[2])
    return b
def orbit(b):
    out = []
    for k in range(4):
        c = rot(b, k)
        if c not in out: out.append(c)
    return out
fig, ax = canvas(62)
x = (0, 1, 0, 0)
pions(ax, 20, 36, 22, x); pions(ax, 68, 36, 22, rot(x))
arrow(ax, (33, 36), (55, 36), 'varie', lw=1.2)
text(ax, 44, 41, r'$r$', 'varie', 'l'); text(ax, 44, 30, '¼ de tour', 'varie', 's')
text(ax, 20, 20, 'avant', 'fixe', 's'); text(ax, 68, 20, 'après', 'fixe', 's')
box(ax, 4, 3, 36, 9, 'sujet', label='4 rotations')
box(ax, 48, 3, 36, 9, 'autre', label='16 colorations')
arrow(ax, (40, 7.5), (48, 7.5), 'varie'); text(ax, 44, 14.5, 'agit sur', 'varie', 's')
save(fig, '49-224')
