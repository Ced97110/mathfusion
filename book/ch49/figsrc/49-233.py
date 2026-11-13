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
for y, b, nm in [(66, (0, 0, 0, 0), 'toute bleue'), (18, (1, 1, 1, 1), 'toute orange')]:
    pions(ax, 14, y, 16, b); pions(ax, 44, y, 16, b, 'resultat')
    arrow(ax, (24, y), (34, y), 'varie'); text(ax, 29, y + 5, r'$r$', 'varie', 's')
    text(ax, 69, y + 3, nm, 'fixe', 's'); text(ax, 69, y - 3, 'orbite : 1', 'resultat', 's')
arrow(ax, (14, 56), (14, 28), 'limite', lw=1.2)
text(ax, 14, 42, r'$\times$', 'limite', 'xl')
text(ax, 44, 42, 'une rotation ne change', 'limite', 's'); text(ax, 44, 37, 'jamais la couleur', 'limite', 's')
save(fig, '49-233')
