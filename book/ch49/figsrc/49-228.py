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
fig, ax = canvas(80)
z = (0, 0, 0, 0)
pions(ax, 16, 40, 18, z)
text(ax, 16, 24, 'départ', 'fixe', 's')
for y, lab in [(66, '¼ tour'), (40, '½ tour'), (14, '¾ tour')]:
    arrow(ax, (27, 40), (53, y), 'varie')
    pions(ax, 70, y, 16, z, 'resultat')
    text(ax, 40, y + (6 if y > 40 else (3.5 if y == 40 else -5)) + (0 if y != 40 else 0), lab, 'varie', 's')
text(ax, 70, 78, 'inchangée', 'resultat', 's')
text(ax, 16, 62, 'stabilisateur : 4', 'sujet', 's'); text(ax, 16, 56, 'orbite : 1', 'resultat', 's')
save(fig, '49-228')
