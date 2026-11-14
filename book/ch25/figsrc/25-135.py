import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$\tan A = \sin A \, / \, \cos A$', 'sujet', 'l')
def tri(x0, k, labs, call):
    a, o = 4 * k, 3 * k
    A = (x0, 22); B = (x0 + a, 22); C = (x0 + a, 22 + o)
    poly(ax, [A, B, C], 'sujet')
    s = 3
    line(ax, [(B[0], 22 + s), (B[0] - s, 22 + s), (B[0] - s, 22)], 'sujet', lw=0.7)
    text(ax, x0 + a / 2, 18.5, labs[1], 'sujet', 's')
    text(ax, B[0] + 3, 22 + o / 2, labs[0], 'sujet', 's')
    text(ax, x0 + a / 2 - 3.6, 22 + o / 2 + 5, labs[2], 'sujet', 's')
    box(ax, 3 if x0 < 30 else 46, 4, 40, 9, 'resultat', label=call)
tri(7, 5, ('3', '4', '5'), '0,6 ÷ 0,8 = 0,75')
tri(48, 3, ('6', '8', '10'), '6/10 ÷ 8/10 = 0,75')
save(fig, '25-135')
