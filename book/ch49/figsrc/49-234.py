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
sizes = [1, 4, 4, 2, 4, 1]
fig, ax = canvas(46)
cw, gap = 4.2, 1.6
x = 5.0; y = 24
segs = []
for n in sizes:
    for j in range(n): box(ax, x + j * cw, y, cw, cw * 1.4, 'sujet', r=0.3, lw=0.6)
    segs.append((x, x + n * cw)); x += n * cw + gap
for i, (a, b) in enumerate(segs):
    brace(ax, a + 0.3, b - 0.3, y - 1, 'fixe', label=str(sizes[i]), depth=1.6)
    if i < 5: text(ax, b + gap / 2, y - 5.1, '+', 'fixe', 's')
brace(ax, segs[0][0], segs[-1][1], y + cw * 1.4 + 1, 'resultat', label='16 colorations', down=False, depth=2)
text(ax, 44, 7, 'six orbites, 16 = 16', 'resultat', 'm', weight='bold')
save(fig, '49-234')
