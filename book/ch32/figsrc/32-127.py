import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'tan² x sin x = tan² x', 'encre', 'm')
arrow(ax, (44, 66), (44, 57), 'varie'); text(ax, 56, 61.5, 'factoriser', 'varie', 's', ha='left')
text(ax, 44, 53, 'tan² x (sin x − 1) = 0', 'encre', 'm')
f = numberline(ax, 8, 76, 30, 0, 360, step=90, arrow_right=False)
for v in (0, 180):
    disc(ax, f(v), 30, 2.2, 'resultat')
    text(ax, f(v), 38, 'tan² x = 0', 'sujet', 's')
disc(ax, f(90), 30, 2.2, 'limite', fill=False, lw=1.2)
text(ax, f(90), 38, 'sin x = 1', 'autre', 's')
text(ax, f(90), 17, "rejeté : tan 90° n'existe pas", 'limite', 's')
text(ax, 44, 7, 'solutions : 0° et 180°', 'resultat', 's')
save(fig, '32-127')
