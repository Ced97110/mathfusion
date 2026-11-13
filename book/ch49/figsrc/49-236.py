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
fig, ax = canvas(74)
x = (0, 1, 0, 0)
text(ax, 22, 68, '4 rotations', 'sujet', 'm', weight='bold'); text(ax, 66, 68, '8 symétries', 'autre', 'm', weight='bold')
pions(ax, 22, 46, 20, x); pions(ax, 66, 46, 20, x)
d = 20 * 0.27
line(ax, [(66 + 15, 46 + 15), (66 - 15, 46 - 15)], 'resultat', dash=True)
text(ax, 80, 62, 'axe', 'resultat', 's')
text(ax, 22, 28, 'stabilisateur : 1', 'fixe', 's'); text(ax, 66, 28, 'stabilisateur : 2', 'fixe', 's')
text(ax, 22, 21, 'orbite : 4', 'resultat', 's'); text(ax, 66, 21, 'orbite : 4', 'resultat', 's')
text(ax, 22, 12, r'$4 \times 1 = 4$', 'varie', 'm'); text(ax, 66, 12, r'$4 \times 2 = 8$', 'varie', 'm')
text(ax, 44, 4, 'toujours 6 orbites', 'resultat', 's', weight='bold')
save(fig, '49-236')
