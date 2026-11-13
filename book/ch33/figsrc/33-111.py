import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
A, B, C = (6, 56), (42, 56), (42, 56 + 27)
poly(ax, [A, B, C], 'fixe', fill=False, lw=1.0)
line(ax, [A, B], 'sujet', lw=2.2); line(ax, [B, C], 'varie', lw=2.2)
line(ax, [(B[0] - 3, B[1]), (B[0] - 3, B[1] + 3), (B[0], B[1] + 3)], 'fixe', lw=0.7)
th = math.atan2(3, 4)
line(ax, [(A[0] + 7 * math.cos(a * th / 30), A[1] + 7 * math.sin(a * th / 30)) for a in range(31)], 'resultat', lw=1.2)
text(ax, A[0] + 12, A[1] + 2.5, r'$\theta$', 'resultat', 's')
text(ax, 24, 51.5, '4', 'sujet', 'm'); text(ax, 46, 69.5, '3', 'varie', 'm'); text(ax, 20, 73, '5', 'fixe', 'm')
text(ax, 68, 74, r'$\tan\theta = 3/4$', 'varie', 's')
text(ax, 68, 62, r'$\cos\theta = 4/5$', 'resultat', 's')
w = 13
for i in range(5):
    box(ax, 10 + i * w, 22, w, 9, 'sujet' if i < 4 else 'fixe', fill=i < 4)
brace(ax, 10, 10 + 4 * w, 21, 'sujet', label='4', down=True)
brace(ax, 10, 10 + 5 * w, 33, 'fixe', label='5', down=False)
text(ax, 82, 26.5, r'$= 0{,}8$', 'resultat', 'm')
save(fig, '33-111')
