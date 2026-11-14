import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
rows = [('départ', r'$\eta^n(a)=a^{q^n}$', 'fixe'),
        ('étape décisive', r'$E$ a $q^n$ éléments : $a^{q^n}=a$', 'varie'),
        ('arrivée', r'$\eta^n$ est l\'identité'.replace("\\'", "'"), 'resultat')]
ys = [70, 50, 30]
for (t, s, r), y in zip(rows, ys):
    text(ax, 3, y, t, r, 's', ha='left')
    box(ax, 28, y - 6, 58, 12, r, label=s, size='s', lw=1.6 if r == 'varie' else 0.8)
for y in ys[:2]: arrow(ax, (57, y - 7), (57, y - 13), 'fixe')
box(ax, 4, 4, 80, 14, 'sujet', label=r'cas : $q=2$, $n=3$ ; $E$ a $2^3=8$ éléments', size='s')
save(fig, '67-100')
