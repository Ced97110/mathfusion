import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 3.5
for x0, a, b in [(4, 3, 5), (42, 6, 10)]:
    part = b * u / 5
    box(ax, x0, 30, b * u, 7, 'varie', r=0.3)
    for p in range(1, 5): line(ax, [(x0 + p * part, 30), (x0 + p * part, 37)], 'encre', lw=0.8)
    box(ax, x0, 20, a * u, 7, 'sujet', r=0.3)
    for p in range(1, 3): line(ax, [(x0 + p * part, 20), (x0 + p * part, 27)], 'encre', lw=0.8)
    line(ax, [(x0 + 3 * part, 37), (x0 + 3 * part, 20)], 'resultat', lw=0.8, dash=True)
    text(ax, x0 + b * u / 2, 41, f'orange : {b}', 'varie', 's'); text(ax, x0 + a * u / 2, 16, f'bleu : {a}', 'sujet', 's')
    text(ax, x0 + b * u / 2, 9, '3 parts sur 5', 'resultat', 's')
arrow(ax, (24, 33.5), (40, 33.5), 'varie')
text(ax, 32, 38, 'agrandir', 'varie', 's')
text(ax, 44, 52, 'le bleu sous l’orange', 'encre', 'm')
save(fig, '09-012')
