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
fig, ax = canvas(84)
for row, (b, lab) in enumerate([((0, 1, 0, 0), 'un pion orange'), ((1, 0, 1, 1), 'trois pions orange')]):
    y = 66 - row * 40
    text(ax, 44, y + 12, lab, 'sujet', 's')
    for k in range(4): pions(ax, 11 + k * 22, y, 14, rot(b, k))
    text(ax, 44, y - 11, '4 colorations', 'resultat', 's')
arrow(ax, (14, 51), (14, 42), 'varie', both=True); text(ax, 20, 46.5, 'échange des couleurs', 'varie', 's', ha='left')
save(fig, '49-232')
