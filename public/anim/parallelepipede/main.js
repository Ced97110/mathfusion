// Copyright: Your Name. Apache 2.0
// "Le parallélépipède dans le réel": calcite, a ream of paper, two boxes of liquid.
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
import {
  makeEnvironment, makeGround, makePaperTexture, makeWoodTexture,
  corners, parallelepipedGeometry, writeParallelepiped, meshVolume,
} from './world.js';
import { EdgeTubes } from './tubes.js';

const ROLE = { bleu: '#6fa3d6', orange: '#e98a45', gris: '#b4bac4', vert: '#5fc48c', violet: '#b593e0' };
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

// ---------- renderer, camera, light ----------
const canvas = document.getElementById('c');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.toneMapping = THREE.AgXToneMapping;
renderer.toneMappingExposure = 0.9;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;

const scene = new THREE.Scene();
scene.background = new THREE.Color('#0b0c0e');
scene.fog = new THREE.Fog('#0b0c0e', 7, 16);
scene.environment = makeEnvironment(renderer);
scene.environmentIntensity = 0.65;

const camera = new THREE.PerspectiveCamera(32, 1, 0.05, 60);
const key = new THREE.DirectionalLight('#fff1de', 1.9);
key.position.set(-4, 7, 5);
key.castShadow = true;
key.shadow.mapSize.set(2048, 2048);
Object.assign(key.shadow.camera, { left: -3.5, right: 3.5, top: 3.5, bottom: -3.5, near: 1, far: 20 });
key.shadow.bias = -0.0004;
key.shadow.normalBias = 0.015;
scene.add(key);
const rim = new THREE.DirectionalLight('#cfe0ff', 0.9);
rim.position.set(5, 3, -6);
scene.add(rim);
scene.add(makeGround());

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(new THREE.Vector2(1, 1), 0.32, 0.5, 1.6);
const Q = new URLSearchParams(location.search);
if (Q.get('bloom') !== '0') composer.addPass(bloom);
composer.addPass(new OutputPass());

// ---------- shot 1: calcite ----------
const PAPER_W = 1.48, PAPER_H = 1.05; // A5 sheet (1 unit = 10 cm)
const shot1 = new THREE.Group();
scene.add(shot1);
const paperTex = makePaperTexture(PAPER_W, PAPER_H);
const paper = new THREE.Mesh(
  new THREE.PlaneGeometry(PAPER_W, PAPER_H),
  new THREE.MeshStandardMaterial({ map: paperTex, color: '#d9d6cf', roughness: 0.92, envMapIntensity: 0.5 }),
);
paper.rotation.x = -Math.PI / 2;
paper.position.y = 0.002;
paper.receiveShadow = true;
shot1.add(paper);

// Cleavage rhombohedron: three equal edges, pairwise angle 101°55' (faces = rhombi 101°55' / 78°05').
const ALPHA = THREE.MathUtils.degToRad(101 + 55 / 60);
const EDGE = 0.42; // a 4 cm cleavage rhomb
const m1 = new THREE.Vector3(1, 0, 0);
const m2 = new THREE.Vector3(Math.cos(ALPHA), Math.sin(ALPHA), 0);
const cz = (Math.cos(ALPHA) - Math.cos(ALPHA) ** 2) / Math.sin(ALPHA);
const m3 = new THREE.Vector3(Math.cos(ALPHA), cz, Math.sqrt(1 - Math.cos(ALPHA) ** 2 - cz ** 2));
const toWorld = (m) => new THREE.Vector3(m.x, m.z, -m.y).multiplyScalar(EDGE); // math z-up -> three y-up
const ca = toWorld(m1), cb = toWorld(m2), cc = toWorld(m3);
const crystalPts = corners(ca, cb, cc);
const cCentre = crystalPts.reduce((s, p) => s.add(p), new THREE.Vector3()).multiplyScalar(1 / 8);
crystalPts.forEach((p) => p.sub(new THREE.Vector3(cCentre.x, 0, cCentre.z))); // bottom face on y = 0, centred
const crystalGeo = parallelepipedGeometry(crystalPts);

const crystalMat = new THREE.ShaderMaterial({
  side: THREE.DoubleSide,
  uniforms: {
    uPaper: { value: paperTex }, uPaperY: { value: 0.002 }, uPaperSize: { value: new THREE.Vector2(PAPER_W, PAPER_H) },
    uLight: { value: key.position.clone().normalize() }, uLit: { value: 0.62 },
    uExplode: { value: 0 }, uFace: { value: new Array(6).fill(0) }, uBlue: { value: new THREE.Color(ROLE.bleu) },
  },
  vertexShader: /* glsl */`
    attribute float faceId;
    uniform float uExplode;
    varying vec3 vWorld; varying vec3 vN; varying float vFace;
    void main() {
      vec3 p = position + normal * uExplode;
      vec4 w = modelMatrix * vec4(p, 1.0);
      vWorld = w.xyz;
      vN = normalize(mat3(modelMatrix) * normal);
      vFace = faceId;
      gl_Position = projectionMatrix * viewMatrix * w;
    }`,
  fragmentShader: /* glsl */`
    uniform sampler2D uPaper; uniform float uPaperY; uniform vec2 uPaperSize;
    uniform vec3 uLight; uniform float uLit; uniform float uFace[6]; uniform vec3 uBlue;
    varying vec3 vWorld; varying vec3 vN; varying float vFace;
    vec3 sky(vec3 r) {
      float h = r.y;
      vec3 c = h > 0.0 ? mix(vec3(0.16, 0.14, 0.13), vec3(0.32, 0.36, 0.44), pow(h, 0.7)) : vec3(0.05);
      c += vec3(2.4, 2.2, 1.9) * pow(max(dot(r, normalize(vec3(-0.55, 0.65, 0.45))), 0.0), 60.0);
      c += vec3(1.2) * smoothstep(0.985, 1.0, 1.0 - abs(r.y - 0.12)) * step(r.z, 0.0);
      return c;
    }
    // Ray enters the crystal with index n. If it lands on the sheet, read the paper there;
    // otherwise it leaves through a side face and shows the studio (or the dark slate).
    float chan(vec3 d, vec3 N, float n, int c) {
      vec3 r = refract(d, N, 1.0 / n);
      if (r.y > -0.08) return sky(r)[c] * 0.8;
      float t = (uPaperY - vWorld.y) / r.y;
      vec3 h = vWorld + r * t;
      vec2 uv = vec2(h.x / uPaperSize.x + 0.5, -h.z / uPaperSize.y + 0.5);
      if (any(lessThan(uv, vec2(0.0))) || any(greaterThan(uv, vec2(1.0)))) return 0.11;
      return texture2D(uPaper, uv)[c] * uLit;
    }
    // dispersion: red bends less than blue (n +- 0.01 around each index)
    vec3 through(vec3 d, vec3 N, float n) {
      return vec3(chan(d, N, n - 0.008, 0), chan(d, N, n, 1), chan(d, N, n + 0.012, 2));
    }
    void main() {
      vec3 d = normalize(vWorld - cameraPosition);
      vec3 N = normalize(vN) * (gl_FrontFacing ? 1.0 : -1.0);
      if (dot(N, d) > 0.0) N = -N;
      // birefringence: ordinary ray (n = 1.658) and extraordinary ray (n = 1.486) give two images
      vec3 img = 0.5 * (through(d, N, 1.658) + through(d, N, 1.486));
      vec3 trans = img * vec3(1.0, 0.985, 0.955);
      float cosT = max(dot(-d, N), 0.0);
      float F = 0.06 + 0.94 * pow(1.0 - cosT, 5.0);
      vec3 R = reflect(d, N);
      vec3 col = mix(trans, sky(R), F);
      col += vec3(3.0, 2.8, 2.5) * pow(max(dot(R, uLight), 0.0), 320.0);
      int f = int(vFace + 0.5);
      float on = 0.0;
      for (int i = 0; i < 6; i++) if (i == f) on = uFace[i];
      col = mix(col, uBlue * 0.9, on * 0.55);
      gl_FragColor = vec4(col, 1.0);
      #include <tonemapping_fragment>
      #include <colorspace_fragment>
    }`,
});
const crystal = new THREE.Mesh(crystalGeo, crystalMat);
const crystalPivot = new THREE.Group();
crystalPivot.add(crystal);
shot1.add(crystalPivot);
const crystalEdges = new EdgeTubes(new THREE.MeshStandardMaterial({ color: '#ffffff', emissive: '#ffffff', emissiveIntensity: 0.25, roughness: 0.2, transparent: true, opacity: 0.55 }), 0.0035);
crystal.add(crystalEdges.group);
crystalEdges.meshes.forEach((m) => { m.castShadow = false; }); // a clear crystal casts no wire shadow
crystalEdges.update(crystalPts);

// per-face centre and normal (local), for the count labels and the exploded view
const faceInfo = [];
{
  const p = crystalGeo.attributes.position, n = crystalGeo.attributes.normal;
  for (let f = 0; f < 6; f++) {
    const c = new THREE.Vector3();
    for (const k of [0, 1, 2, 5]) c.add(new THREE.Vector3().fromBufferAttribute(p, f * 6 + k));
    faceInfo.push({ c: c.multiplyScalar(0.25), n: new THREE.Vector3().fromBufferAttribute(n, f * 6) });
  }
}
const topFace = faceInfo.reduce((best, fi, i) => (fi.n.y > faceInfo[best].n.y ? i : best), 0);
const topCorners = [0, 1, 2, 5].map((k) => new THREE.Vector3().fromBufferAttribute(crystalGeo.attributes.position, topFace * 6 + k));
const angleAt = (i) => {
  const p = topCorners[i], a = topCorners[(i + 1) % 4], b = topCorners[(i + 3) % 4];
  return THREE.MathUtils.radToDeg(a.clone().sub(p).angleTo(b.clone().sub(p)));
};

// ---------- shot 2: a ream of 500 sheets ----------
const shot2 = new THREE.Group();
scene.add(shot2);
const N_SHEETS = 500, SHEET_T = 0.001, REAM_W = 2.97, REAM_D = 2.1;
const sheets = new THREE.InstancedMesh(
  new THREE.BoxGeometry(REAM_W, SHEET_T, REAM_D),
  new THREE.MeshStandardMaterial({ color: '#dcd8cf', roughness: 0.9, envMapIntensity: 0.55 }),
  N_SHEETS,
);
sheets.castShadow = sheets.receiveShadow = true;
const jitter = [];
{
  const c = new THREE.Color();
  for (let i = 0; i < N_SHEETS; i++) {
    jitter.push([(Math.random() - 0.5) * 2, (Math.random() - 0.5) * 2]);
    const g = 0.94 + Math.random() * 0.06;
    sheets.setColorAt(i, c.setRGB(g, g * 0.995, g * 0.98));
  }
}
shot2.add(sheets);
const boardPivot = new THREE.Group();
boardPivot.position.set(-REAM_W / 2 - 0.004, 0, 0);
const wood = makeWoodTexture();
const board = new THREE.Mesh(
  new THREE.BoxGeometry(0.05, 0.86, 2.35),
  new THREE.MeshStandardMaterial({ map: wood, color: '#e7a27a', roughness: 0.6, envMapIntensity: 0.8 }),
);
board.position.set(-0.025, 0.43, 0);
board.castShadow = board.receiveShadow = true;
boardPivot.add(board);
shot2.add(boardPivot);
const THETA_MAX = THREE.MathUtils.degToRad(24);
const heightTube = new EdgeTubes(new THREE.MeshBasicMaterial({ color: ROLE.gris }), 0.006, 1);
shot2.add(heightTube.group);
const dummy = new THREE.Object3D();
function setShear(theta) {
  const s = Math.tan(theta), mess = theta / THETA_MAX;
  for (let i = 0; i < N_SHEETS; i++) {
    const h = (i + 0.5) * SHEET_T;
    dummy.position.set(h * s + jitter[i][0] * 0.0045 * mess, h, jitter[i][1] * 0.0025 * mess);
    dummy.updateMatrix();
    sheets.setMatrixAt(i, dummy.matrix);
  }
  sheets.instanceMatrix.needsUpdate = true;
  boardPivot.rotation.z = -theta;
  const top = REAM_W / 2 + N_SHEETS * SHEET_T * s;
  heightTube.update([new THREE.Vector3(top, 0, REAM_D / 2 + 0.03), new THREE.Vector3(top, N_SHEETS * SHEET_T, REAM_D / 2 + 0.03)], [[0, 1]]);
}

// ---------- shot 3: two boxes, same base and height, same liquid ----------
const S = 0.42;
const shot3 = new THREE.Group();
scene.add(shot3);
const fiche = (x, y, z) => new THREE.Vector3(x, z, -y).multiplyScalar(S); // fiche coordinates (z up) -> world
const U = fiche(2, 0, 0), V = fiche(1, 2, 0);
const box = [
  { o: new THREE.Vector3(-2.05, 0, 0.35), a: fiche(2, 0, 0), b: fiche(0, 2, 0), w: fiche(0, 0, 3), col: ROLE.violet },
  { o: new THREE.Vector3(0.05, 0, 0.35), a: U, b: V, w: fiche(1, 1, 3), col: ROLE.bleu },
];
const glassMat = new THREE.MeshPhysicalMaterial({
  color: '#ffffff', transparent: true, opacity: 0.16, roughness: 0.03, metalness: 0, envMapIntensity: 1.6,
  side: THREE.DoubleSide, depthWrite: false, clearcoat: 1, clearcoatRoughness: 0.02,
});
// Not transmissive: the transmission buffer gave NaN blocks with the transparent glass around it.
const liquidMat = new THREE.MeshPhysicalMaterial({
  color: '#2f9e64', emissive: '#0d3b24', emissiveIntensity: 0.6, transparent: true, opacity: 0.78,
  roughness: 0.08, metalness: 0, clearcoat: 1, clearcoatRoughness: 0.05, envMapIntensity: 1.3, depthWrite: true,
});
box.forEach((bx) => {
  const pts = corners(bx.a, bx.b, bx.w, bx.o);
  bx.glass = new THREE.Mesh(parallelepipedGeometry(expand(pts, 1.012)), glassMat);
  bx.glass.renderOrder = 2;
  bx.edges = new EdgeTubes(new THREE.MeshStandardMaterial({ color: bx.col, emissive: bx.col, emissiveIntensity: 0.35, roughness: 0.3 }), 0.009);
  bx.edges.update(pts);
  bx.liquid = new THREE.Mesh(parallelepipedGeometry(corners(bx.a, bx.b, bx.w.clone().multiplyScalar(0.001), bx.o)), liquidMat);
  bx.liquid.castShadow = true;
  bx.stream = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.014, 1, 24, 1, true), liquidMat);
  bx.base = bx.o.clone().addScaledVector(bx.a, 0.5).addScaledVector(bx.b, 0.5);
  shot3.add(bx.glass, bx.edges.group, bx.liquid, bx.stream);
});
const level = { L: 0 };
function setBox(bx, w) {
  bx.w.copy(w);
  const g = expand(corners(bx.a, bx.b, bx.w, bx.o), 1.012);
  writeParallelepiped(bx.glass.geometry, g);
  bx.edges.update(g);
  writeParallelepiped(bx.liquid.geometry, corners(bx.a, bx.b, bx.w.clone().multiplyScalar(Math.max(level.L, 0.001) / 3), bx.o));
}
function expand(pts, f) {
  const c = pts.reduce((a, p) => a.add(p), new THREE.Vector3()).multiplyScalar(1 / 8);
  return pts.map((p) => p.clone().sub(c).multiplyScalar(f).add(c));
}
const volume = (bx) => meshVolume(bx.liquid.geometry, bx.liquid.matrixWorld) / S ** 3;

// ---------- labels (HTML, placed on 3D points) ----------
const labels = [];
function label(html, cls, where, show) {
  const el = document.createElement('div');
  el.className = 'lab ' + cls;
  el.innerHTML = html;
  document.body.appendChild(el);
  const l = { el, where, show, html };
  labels.push(l);
  return l;
}
const tmp = new THREE.Vector3();
faceInfo.forEach((fi, i) => label(String(i + 1), 'b big', () => crystal.localToWorld(tmp.copy(fi.c).addScaledVector(fi.n, crystalMat.uniforms.uExplode.value * 1.6 + 0.05)),
  (t) => t > 7.2 + i * 0.7 && t < 12.2));
[0, 1, 2, 3].forEach((i) => {
  const ang = angleAt(i);
  const c = topCorners.reduce((s, p) => s.add(p), new THREE.Vector3()).multiplyScalar(0.25);
  label(`${ang > 90 ? '102' : '78'}°`, ang > 90 ? 'o' : 'o', () => crystal.localToWorld(tmp.copy(topCorners[i]).lerp(c, 0.3)),
    (t) => t > 13.8 && t < 16.4 && (i === 0 || i === 1));
});
label('hauteur 5 cm', 'g', () => tmp.set(REAM_W / 2 + 0.5 * Math.tan(shearNow) - 0.25, 0.68, REAM_D / 2), (t) => t > 28 && t < 33);
label('arête penchée', 'o', () => tmp.set(-REAM_W / 2 + 0.25 * Math.tan(shearNow) + 0.42, 0.25, REAM_D / 2 + 0.05), (t) => t > 28.4 && t < 33);
label('carton', 'p', () => tmp.copy(box[0].base).add(new THREE.Vector3(0, 3 * S + 0.16, 0)), (t) => t > 33.6);
label('parallélépipède', 'b', () => tmp.copy(box[1].base).addScaledVector(box[1].w, 1.12), (t) => t > 33.6);
label('base 4', 'g', () => tmp.copy(box[0].base).add(new THREE.Vector3(0, 0, 0.62)), (t) => t > 34 && t < 37.4);
label('base 4', 'g', () => tmp.copy(box[1].base).add(new THREE.Vector3(0, 0, 0.62)), (t) => t > 34 && t < 37.4);
label('niveau 2', 'g', () => tmp.copy(box[0].base).add(new THREE.Vector3(-0.62, 2 * S, 0)), (t) => t > 42);
const volLab = [0, 1].map((k) => label('volume 8', 'v', () => tmp.copy(box[k].base).addScaledVector(box[k].w, (level.L / 3) * 0.5).add(new THREE.Vector3(0, 0, 0.5)), (t) => t > 42.4));

// ---------- captions ----------
const CAPS = [
  [0.6, 5.0, 'Un cristal de <span class="b">calcite</span>. Ce minéral se casse toujours en blocs de cette forme.'],
  [5.3, 12.2, 'Ouvrons-le : <span class="b">six faces</span>, et chacune est un parallélogramme.'],
  [13.6, 16.4, 'Chaque face a deux angles : <span class="o">102°</span> et <span class="o">78°</span>. Aucun angle n’est droit.'],
  [16.6, 19.0, 'À travers le cristal, le trait bleu est vu deux fois : la lumière s’y sépare en deux.'],
  [19.4, 23.4, 'Une rame de 500 feuilles a la forme d’un <span class="p">carton</span> : tous ses angles sont droits.'],
  [23.6, 27.6, 'On penche la <span class="o">planche</span> : chaque feuille glisse un peu sur celle du dessous.'],
  [27.8, 32.6, 'Les arêtes penchent : la rame est devenue un <span class="b">parallélépipède</span>. Sa <span class="g">hauteur</span> reste 5 cm.'],
  [33.4, 37.2, 'Deux boîtes de même base, d’aire 4, et de même hauteur, 3. L’une est droite, l’autre penchée.'],
  [37.4, 42.0, 'On verse la même quantité de liquide dans chacune.'],
  [42.2, 47.0, 'Le <span class="g">niveau</span> est le même : 2. <span class="v">Volume = aire de la base × hauteur = 4 × 2 = 8.</span>'],
  [47.2, 1e9, 'À toi : fais glisser sur l’image pour pencher la boîte <span class="b">bleue</span>. Le niveau et le <span class="v">volume</span> ne bougent pas.'],
];
const capEl = document.getElementById('cap');
let capNow = -1;

// ---------- camera path ----------
const V3 = (x, y, z) => new THREE.Vector3(x, y, z);
const KEYS = [
  [0, V3(1.55, 0.55, 1.65), V3(0, 0.15, 0)], [5, V3(1.25, 1.25, 1.35), V3(0, 0.36, 0)], [12, V3(-0.95, 1.35, 1.45), V3(0, 0.36, 0)],
  [14.2, V3(0.2, 1.55, 0.85), V3(0, 0.06, 0)], [19, V3(0.1, 1.3, 0.55), V3(0, 0.03, 0)],
  [19.001, V3(3.9, 1.8, 4.5), V3(0, 0.22, 0)], [23.5, V3(3.1, 1.3, 3.9), V3(0.1, 0.25, 0)], [28, V3(0.75, 0.9, 4.5), V3(0.15, 0.25, 0)], [33, V3(0.4, 0.85, 4.1), V3(0.15, 0.25, 0)],
  [33.001, V3(-0.55, 2.9, 5.9), V3(-0.55, 0.45, 0)], [37.4, V3(-0.5, 2.35, 5.2), V3(-0.55, 0.5, 0)], [42, V3(-0.4, 2.0, 4.9), V3(-0.55, 0.55, 0)], [47, V3(-0.4, 2.05, 5.0), V3(-0.55, 0.55, 0)],
];
const ease = (x) => x * x * x * (x * (6 * x - 15) + 10);
function cameraAt(t) {
  let i = 0;
  while (i < KEYS.length - 2 && t > KEYS[i + 1][0]) i++;
  const [t0, p0, q0] = KEYS[i], [t1, p1, q1] = KEYS[i + 1];
  const k = ease(THREE.MathUtils.clamp((t - t0) / (t1 - t0), 0, 1));
  camera.position.lerpVectors(p0, p1, k);
  const target = q0.clone().lerp(q1, k);
  if (t > 47) { // free phase: slow drift
    const s = t - 47;
    camera.position.x += Math.sin(s * 0.17) * 0.35;
    camera.position.y += Math.sin(s * 0.11) * 0.08;
  }
  camera.lookAt(target);
}

// ---------- timeline ----------
const seg = (t, a, b) => ease(THREE.MathUtils.clamp((t - a) / (b - a), 0, 1));
let shearNow = 0;
let userW = null; // set by dragging in the free phase
function update(t) {
  shot1.visible = t < 19; shot2.visible = t >= 19 && t < 33; shot3.visible = t >= 33;
  // shot 1
  const lift = seg(t, 5, 6.5) - seg(t, 12, 13.4);
  crystalPivot.position.y = 0.22 * lift;
  crystalMat.uniforms.uExplode.value = 0.2 * (seg(t, 5.6, 7) - seg(t, 11.6, 12.8));
  crystalPivot.rotation.y = 0.35 + 0.45 * lift * Math.sin((t - 5) * 0.35) + 0.06 * Math.sin(t * 0.3);
  crystalPivot.rotation.x = 0;
  crystalEdges.group.visible = crystalMat.uniforms.uExplode.value < 0.004;
  crystalMat.uniforms.uFace.value = faceInfo.map((_, i) => (t > 7.2 + i * 0.7 && t < 12.2 ? Math.min(1, (t - 7.2 - i * 0.7) * 3) * (1 - seg(t, 11.4, 12.2)) : 0));
  // shot 2
  shearNow = THETA_MAX * seg(t, 23.8, 27.4);
  if (shot2.visible) setShear(shearNow);
  heightTube.group.visible = t > 28;
  // shot 3
  level.L = 2 * seg(t, 38, 41.6);
  box.forEach((bx, k) => {
    const pouring = t > 37.6 && t < 41.9;
    bx.stream.visible = pouring;
    const top = 2.6 * S + 0.6, bottom = level.L * S + 0.01;
    bx.stream.scale.y = top - bottom;
    bx.stream.position.copy(bx.base).add(new THREE.Vector3(0, (top + bottom) / 2, 0));
    if (k === 1) bx.stream.position.addScaledVector(bx.w, (level.L / 3) * 1).setY((top + bottom) / 2);
    const w = k === 1 && t > 47 ? (userW ?? swayW(t)) : bx.w;
    setBox(bx, w);
  });
  const v = [volume(box[0]), volume(box[1])];
  volLab.forEach((l, k) => { l.el.textContent = `volume ${v[k].toFixed(2).replace('.', ',')}`; });
  cameraAt(t);
  // fades between shots
  const f = Math.max(1 - seg(t, 0, 1.2), seg(t, 18.4, 19) * (1 - seg(t, 19, 19.6)), seg(t, 32.4, 33) * (1 - seg(t, 33, 33.6)));
  document.getElementById('fade').style.opacity = f.toFixed(3);
  // captions
  const c = CAPS.findIndex(([a, b]) => t >= a && t < b);
  if (c !== capNow) {
    capNow = c;
    capEl.classList.remove('on');
    if (c >= 0) setTimeout(() => { capEl.innerHTML = CAPS[c][2]; capEl.classList.add('on'); }, 250);
  }
  // labels
  labels.forEach((l) => {
    const on = l.show(t) && (l.el.offsetParent !== undefined);
    const p = l.where().project(camera);
    const vis = on && p.z < 1;
    l.el.classList.toggle('on', vis);
    if (vis) l.el.style.transform = `translate(${((p.x + 1) / 2) * innerWidth}px, ${((1 - p.y) / 2) * innerHeight}px) translate(-50%, -50%)`;
  });
}
const W0 = fiche(1, 1, 3);
function swayW(t) {
  const s = t - 47;
  return fiche(1 + 1.1 * Math.sin(s * 0.6), 1 - 0.8 * Math.sin(s * 0.37), 3);
}

// ---------- drag to shear (free phase) ----------
let drag = null;
canvas.addEventListener('pointerdown', (e) => {
  if (T < 42) return;
  const cur = userW ?? swayW(T);
  drag = { x: e.clientX, y: e.clientY, a: cur.x / S, b: -cur.z / S };
  canvas.setPointerCapture(e.pointerId);
});
canvas.addEventListener('pointermove', (e) => {
  if (!drag) return;
  const a = THREE.MathUtils.clamp(drag.a + ((e.clientX - drag.x) / innerWidth) * 6, -1.6, 2.6);
  const b = THREE.MathUtils.clamp(drag.b - ((e.clientY - drag.y) / innerHeight) * 6, -1.6, 2.6);
  userW = fiche(a, b, 3);
  if (T < 47) T = 47;
});
canvas.addEventListener('pointerup', () => { drag = null; });

// ---------- loop ----------
let T = reduced ? 47 : 0;
let paused = false;
let last = performance.now();
const frameTimes = [];
function resize() {
  const w = innerWidth, h = innerHeight;
  renderer.setSize(w, h, false);
  composer.setSize(w, h);
  bloom.resolution.set(w, h);
  camera.aspect = w / h;
  camera.fov = w / h < 0.8 ? 50 : 32; // phones: wider view
  camera.updateProjectionMatrix();
}
addEventListener('resize', resize);
resize();
function frame(now) {
  const dt = Math.min((now - last) / 1000, 0.1);
  last = now;
  if (!paused) T += reduced && T >= 47 ? 0 : dt;
  const t0 = performance.now();
  update(T);
  composer.render();
  frameTimes.push(performance.now() - t0);
  if (frameTimes.length > 2000) frameTimes.shift();
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
document.getElementById('replay').addEventListener('click', () => { T = 0; userW = null; paused = false; });

// ---------- test hooks ----------
window.__mf = {
  seek(t) { T = t; paused = true; },
  play() { paused = false; },
  get t() { return T; },
  volumes() { return [volume(box[0]), volume(box[1])]; },
  level() { return level.L; },
  setShear(a, b) { userW = fiche(a, b, 3); },
  faceAngles() { return [0, 1, 2, 3].map(angleAt); },
  frameTimes,
  ready: true,
};
