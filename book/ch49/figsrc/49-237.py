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
names = ['identité', '¼ tour', '½ tour', '¾ tour']; vals = [16, 2, 4, 2]
base = 22; u = 2.2
for k, (nm, v) in enumerate(zip(names, vals)):
    cx = 12 + k * 21.3
    box(ax, cx - 6, base, 12, v * u, 'sujet', r=0.4)
    text(ax, cx, base + v * u + 3, str(v), 'sujet', 'm', weight='bold')
    text(ax, cx, base - 4, nm, 'fixe', 's')
line(ax, [(4, base), (84, base)], 'fixe')
text(ax, 44, 70, 'colorations non changées', 'fixe', 's') if False else None
text(ax, 44, 11, r'$16+2+4+2=24$', 'varie', 'm')
text(ax, 44, 4, r'$24 \div 4 = 6$ orbites', 'resultat', 'm', weight='bold')
save(fig, '49-237')
