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
fig, ax = canvas(76)
cases = [(14, (0, 0, 0, 0), 'resultat', 'fixe'), (44, (1, 1, 1, 1), 'resultat', 'fixe'), (74, (0, 1, 0, 0), 'limite', 'change')]
for cx, b, fr, lab in cases:
    pions(ax, cx, 60, 15, b)
    arrow(ax, (cx, 49), (cx, 40), 'varie'); text(ax, cx + 4, 44.5, r'$r$', 'varie', 's', ha='left')
    pions(ax, cx, 29, 15, rot(b), fr)
    text(ax, cx, 17, lab, fr, 's', weight='bold')
text(ax, 44, 7, '2 colorations fixées par r', 'resultat', 'm', weight='bold')
save(fig, '49-238')
