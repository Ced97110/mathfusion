import Branch from '../branche/[slug]/page';

export const metadata = { title: 'Mathématiques discrètes — cause, effets, finalité' };

// Old address of the book: same content as the branch page /branche/mathematiques-discretes/.
export default function Discretes() {
  return Branch({ params: Promise.resolve({ slug: 'mathematiques-discretes' }) });
}
