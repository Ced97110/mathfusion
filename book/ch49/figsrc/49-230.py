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
fig, ax = canvas(52)
x = (0, 1, 1, 0)
for k in range(4):
    cx = 10 + k * 22.7
    pions(ax, cx, 26, 14, rot(x, k))
    if k < 3:
        arrow(ax, (cx + 8, 26), (cx + 14.7, 26), 'varie'); text(ax, cx + 11.4, 31, r'$r$', 'varie', 's')
text(ax, 44, 46, 'paires de sommets voisins', 'sujet', 's')
text(ax, 44, 8, r'orbite : 4, stabilisateur $\{1\}$', 'resultat', 'm')
save(fig, '49-230')
