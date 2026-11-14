import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(78)
def digits(y, items, role):
    x = 6
    for s in items:
        wd = 3.5 if s == ',' else 7
        if s == ',': text(ax, x + 1.2, y - 2.5, ',', role, 'l')
        else: box(ax, x, y - 4, wd, 8, role, label=s, size='m')
        x += wd + 0.8
    return x
text(ax, 4, 70, 'décimal : il s’arrête', 'fixe', 's', ha='left')
digits(62, ['2', ',', '3', '5'], 'fixe')
text(ax, 4, 48, 'un tiers : un bloc se répète', 'autre', 's', ha='left')
digits(40, ['0', ',', '3', '3', '3', '3', '3'], 'autre')
text(ax, 62, 40, '…', 'autre', 'l')
text(ax, 4, 26, r'$\pi$ : ni fin, ni bloc répété', 'sujet', 's', ha='left', weight='bold')
digits(18, ['3', ',', '1', '4', '1', '5', '9'], 'sujet')
text(ax, 62, 18, '…', 'sujet', 'l')
text(ax, 44, 5, r'3,14159… : valeur approchée', 'sujet', 's')
save(fig, '11-089')
