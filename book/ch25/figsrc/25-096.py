import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
y0 = 26; k = 50
for cx, head, rise, a, b in [(22, 'de 10° à 11°', 0.018, '0,1763', '0,1944'), (66, 'de 80° à 81°', 0.64, '5,6713', '6,3138')]:
    text(ax, cx, 70, head, 'sujet', 'm')
    box(ax, cx - 7, y0, 14, max(rise * k, 1.0), 'varie', r=0.3)
    text(ax, cx, y0 + max(rise * k, 1.0) + 3.5, f'+{rise}'.replace('.', ','), 'varie', 'm')
    text(ax, cx, y0 - 4.5, '1° de plus', 'sujet', 's')
    text(ax, cx, y0 - 11, f'{a} → {b}', 'fixe', 's')
line(ax, [(4, y0), (84, y0)], 'fixe', lw=0.8)
save(fig, '25-096')
