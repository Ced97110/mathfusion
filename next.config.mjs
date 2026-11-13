/** Site statique : `npm run build` écrit le dossier `out/`, à déposer sur n'importe quel hébergeur. */
const nextConfig = { output: 'export', trailingSlash: true, images: { unoptimized: true } };
export default nextConfig;
