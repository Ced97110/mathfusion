import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
eye = (8, 42)
line(ax, [(4, 18), (84, 18)], 'sujet', lw=1.4); text(ax, 80, 22, 'rail', 'sujet', 's')
line(ax, [eye, (84, 42)], 'fixe', dash=True, lw=0.8)
text(ax, 62, 46.5, 'direction du rail', 'fixe', 's')
for x, lab in [(24, '10 m'), (52, '100 m'), (80, '1000 m')]:
    arrow(ax, (eye[0] + 2, eye[1] - 1), (x, 18), 'varie', lw=0.9)
    disc(ax, x, 18, 1.4, 'sujet'); text(ax, x, 11.5, lab, 'sujet', 's')
disc(ax, eye[0], eye[1], 2, 'fixe'); text(ax, eye[0], 49, 'œil', 'encre', 's')
save(fig, '80-282')
