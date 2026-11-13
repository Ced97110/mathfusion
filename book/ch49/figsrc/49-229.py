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
fig, ax = canvas(58)
x = (0, 1, 0, 0)
labs = ['1', r'$r$', r'$r^2$', r'$r^3$']
for k in range(4):
    cx = 11 + k * 22
    pions(ax, cx, 36, 15, rot(x, k))
    text(ax, cx, 22, labs[k], 'varie', 'm')
brace(ax, 3, 85, 17, 'resultat', label='4 colorations différentes', depth=2)
text(ax, 44, 53, 'seul le neutre la laisse en place', 'sujet', 's')
save(fig, '49-229')
