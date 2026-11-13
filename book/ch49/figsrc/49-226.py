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
rows = [(0, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 1, 1, 0), (1, 1, 1, 1)]
sizes = [1, 4, 4, 2, 4, 1]
fig, ax = canvas(98)
y0 = 88
for i, (b, n) in enumerate(zip(rows, sizes)):
    y = y0 - i * 14
    o = orbit(b); assert len(o) == n
    text(ax, 9, y, str(n), 'resultat', 'l', weight='bold')
    for j, c in enumerate(o): pions(ax, 22 + j * 15, y, 11, c)
    line(ax, [(4, y - 7), (84, y - 7)], 'fixe', lw=0.4, dash=True) if i < 5 else None
text(ax, 44, 5.5, r'$1+4+4+2+4+1=16$', 'resultat', 'm', weight='bold')
save(fig, '49-226')
