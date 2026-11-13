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
fig, ax = canvas(72)
cw, g = 4.2, 1.5
def strip(y, groups, roles):
    x = 6.6; ctr = []
    for n, r in zip(groups, roles):
        for j in range(n): box(ax, x + j * cw, y, cw, 6, r, r=0.3, lw=0.6)
        x += n * cw + g
text(ax, 44, 64, 'division naïve : 16 ÷ 4 = 4', 'limite', 'm', weight='bold')
strip(52, [4] * 4, ['limite'] * 4)
text(ax, 44, 46, '4 orbites de taille 4', 'limite', 's')
text(ax, 44, 34, 'en réalité : 6 orbites', 'resultat', 'm', weight='bold')
strip(22, sizes, ['varie', 'sujet', 'sujet', 'varie', 'sujet', 'varie'])
text(ax, 44, 15, 'trois orbites plus petites', 'varie', 's')
text(ax, 44, 8, '4 colorations au lieu de 12', 'varie', 's')
save(fig, '49-235')
