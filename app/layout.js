import './globals.css';
import Link from 'next/link';
import BranchMenu from './components/BranchMenu';

export const metadata = {
  title: 'Des nombres aux structures — fiches illustrées',
  description: 'Une fiche par concept, une figure par fiche.',
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
          <Link href="/" className="bb">Sommaire</Link>
          <div className="t">Des nombres aux structures</div>
          <Link href="/physique/" className="bb">Physique</Link>
          <Link href="/apprentissage/" className="bb">Apprentissage</Link>
        </header>
        <BranchMenu />
        <main>{children}</main>
      </body>
    </html>
  );
}
