import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [('sujet', r'$A^{t}MA=M$'), ('sujet', r'$(\det A)^2\,\det M=\det M$'),
        ('resultat', r'$(\det A)^2=1$'), ('resultat', r'$\det A=1$ ou $-1$')]
notes = ['on prend det des deux côtés', r'$\div\ \det M$ (car $\det M\neq 0$)', 'donc']
nrole = ['fixe', 'varie', 'fixe']
ys = [70, 50, 30, 10]
for (role, s), y in zip(rows, ys):
    box(ax, 14, y, 60, 11, role, label=s, size='m')
for i in range(3):
    arrow(ax, (44, ys[i]), (44, ys[i + 1] + 11), nrole[i] if i != 1 else 'varie', lw=1.4 if i == 1 else 1.0)
    text(ax, 48, ys[i] - 4.5, notes[i], nrole[i], 's', ha='left', weight='bold' if i == 1 else 'normal')
save(fig, '73-065')
