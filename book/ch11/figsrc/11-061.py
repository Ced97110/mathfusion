import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(64)
text(ax, 44, 58, 'on veut des pieds', 'resultat', 'l', weight='bold')
for cx, top, bot, ok in ((22, '1 pied', '12 po', True), (66, '12 po', '1 pied', False)):
    rt, rb = ('resultat', 'sujet') if ok else ('sujet', 'resultat')
    frac(ax, cx, 36, top, bot, rt, rb, w=18, size='m', dy=4)
    c = 'resultat' if ok else 'limite'
    box(ax, cx - 11, 36.6 if ok else 28.4, 22, 7, c, fill=False, lw=1.2)
    text(ax, cx, 12 if ok else 12, 'pied en haut : oui' if ok else 'pied en bas : non', c, 's')
save(fig, '11-061')
