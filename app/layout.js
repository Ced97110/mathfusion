import './globals.css';
import Link from 'next/link';
import BranchMenu from './components/BranchMenu';

export const metadata = {
  title: 'Des nombres aux structures',
  description: 'Arithmétique, algèbre, trigonométrie, algèbre abstraite : un livre de mathématiques, une figure avant chaque formule.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Noto+Sans+Math&display=swap"
        />
      </head>
      <body>
        <header id="bar">
          <Link href="/" className="brand">Des nombres aux structures</Link>
          <nav aria-label="Navigation principale">
            <Link href="/#chapitres">Chapitres</Link>
            <Link href="/physique/">Physique</Link>
            <Link href="/apprentissage/">Apprentissage</Link>
          </nav>
        </header>
        <BranchMenu />
        <main>{children}</main>
      </body>
    </html>
  );
}
