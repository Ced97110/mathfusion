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
fig, ax = canvas(66)
x = (1, 0, 1, 0)
for k in range(3):
    cx = 14 + k * 30
    pions(ax, cx, 44, 14, rot(x, k), 'resultat' if k != 1 else 'fixe')
    if k < 2:
        arrow(ax, (cx + 8, 44), (cx + 22, 44), 'varie'); text(ax, cx + 15, 49, r'$r$', 'varie', 's')
line(ax, [(14, 33), (14, 29), (74, 29), (74, 33)], 'resultat')
text(ax, 44, 24, r'$r^2$ : même coloration', 'resultat', 's')
text(ax, 44, 12, r'stabilisateur $\{1, r^2\}$', 'sujet', 's')
text(ax, 44, 5, 'orbite : 2 colorations', 'resultat', 's')
text(ax, 44, 60, 'deux pions orange opposés', 'sujet', 's')
save(fig, '49-231')
