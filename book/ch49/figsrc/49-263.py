import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
labs = ['000', '001', '010', '011', '100', '101', '110', '111']
f_on = {6, 7}; g_on = {3, 7}
cw = 9.6; x0 = 5.6
for i, l in enumerate(labs):
    x = x0 + cw * i
    text(ax, x + cw / 2 - 0.5, 63, l, 'encre', 's')
    box(ax, x, 46, cw - 1, 9, 'sujet' if i in f_on else 'fixe', r=0.6)
    box(ax, x, 12, cw - 1, 9, 'sujet' if i in g_on else 'fixe', r=0.6)
text(ax, 2, 50.5, 'f', 'sujet', 'l', ha='left'); text(ax, 2, 16.5, 'g', 'sujet', 'l', ha='left')
for a, b in [(6, 3), (7, 7)]:
    arrow(ax, (x0 + cw * a + cw / 2 - 0.5, 45), (x0 + cw * b + cw / 2 - 0.5, 22.5), 'varie', curve=0.0)
text(ax, 24, 33, r'$S_{3}$ déplace les entrées', 'varie', 's')
box(ax, 58, 1.5, 4.5, 4.5, 'sujet', r=0.5); text(ax, 64, 3.8, '1', 'encre', 's', ha='left')
box(ax, 70, 1.5, 4.5, 4.5, 'fixe', r=0.5); text(ax, 76, 3.8, '0', 'encre', 's', ha='left')
save(fig, '49-263')
