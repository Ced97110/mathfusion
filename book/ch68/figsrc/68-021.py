import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(38)
for i, b in enumerate('0011001'):
    box(ax, 4.5 + i * 11.5, 16, 10, 10, 'varie' if i == 2 else 'sujet', label=b, size='l')
cx = lambda i: 4.5 + i * 11.5 + 5
text(ax, cx(0), 11, r'$x_1$', 'sujet', 'm')
text(ax, cx(1), 11, r'$x_2$', 'sujet', 'm')
text(ax, cx(2), 11, r'$x_3 = 1$', 'varie', 'm')
text(ax, cx(6), 11, r'$x_n$', 'sujet', 'm')
brace(ax, 4.5, 83.5, 28, 'fixe', label=r'$n = 7$ bits', down=False)
save(fig, '68-021')
