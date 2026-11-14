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
fig, ax = canvas(88)
text(ax, 44, 84, r'$|G| = 4$', 'sujet', 'l', weight='bold')
for cx, b, stab, res in [(23, (0, 1, 0, 0), 'stabilisateur : 1', r'$4 \div 1 = 4$'), (66, (0, 0, 0, 0), 'stabilisateur : 4', r'$4 \div 4 = 1$')]:
    pions(ax, cx, 66, 16, b)
    text(ax, cx, 52, stab, 'fixe', 's')
    arrow(ax, (cx, 48), (cx, 41), 'varie')
    text(ax, cx, 36, res, 'varie', 'm', weight='bold')
    o = orbit(b)
    n = len(o); pitch = 9.5
    for j, c in enumerate(o): pions(ax, cx - (n - 1) * pitch / 2 + j * pitch, 20, 8, c)
    text(ax, cx, 9, f'orbite : {n}', 'resultat', 's')
save(fig, '49-227')
