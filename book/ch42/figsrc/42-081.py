import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [('sujet', 'départ', 'p ⇒ q', 'multiple de 4 ⇒ pair', 'vrai'),
        ('resultat', 'contraposée', 'non q ⇒ non p', 'pas pair ⇒ pas multiple de 4', 'vraie'),
        ('limite', 'réciproque', 'q ⇒ p', 'pair ⇒ multiple de 4', 'fausse')]
for i, (role, nom, form, ex, v) in enumerate(rows):
    y = 58 - i * 26
    text(ax, 4, y + 20, nom + ' : ' + v, role, 's', ha='left', weight='bold')
    box(ax, 4, y, 30, 16, role, label=form, size='m')
    box(ax, 40, y, 44, 16, role, label=ex, size='s')
    arrow(ax, (34, y + 8), (40, y + 8), role)
save(fig, '42-081')
