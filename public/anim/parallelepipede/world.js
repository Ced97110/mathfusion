// Copyright: Your Name. Apache 2.0
// Studio, ground and geometry helpers. Everything procedural: no image, no model file.
import * as THREE from 'three';

// ---------- noise (value noise + fbm), used for slate, paper fibres and wood ----------
function hash(x, y, s) {
  let h = (x * 374761393 + y * 668265263 + s * 2147483647) | 0;
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  return ((h ^ (h >>> 16)) >>> 0) / 4294967295;
}
function vnoise(x, y, s, period) {
  const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
  const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
  const w = (a) => ((a % period) + period) % period;
  const a = hash(w(xi), w(yi), s), b = hash(w(xi + 1), w(yi), s);
  const c = hash(w(xi), w(yi + 1), s), d = hash(w(xi + 1), w(yi + 1), s);
  return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
}
export function fbm(x, y, seed, oct = 5, base = 8) {
  let f = 0, amp = 0.5, freq = base, norm = 0;
  for (let i = 0; i < oct; i++) {
    f += amp * vnoise(x * freq, y * freq, seed + i, freq);
    norm += amp; amp *= 0.5; freq *= 2;
  }
  return f / norm;
}

function canvasTexture(size, paint, srgb = true, repeat = 1) {
  const cv = document.createElement('canvas');
  cv.width = cv.height = size;
  const ctx = cv.getContext('2d');
  const img = ctx.createImageData(size, size);
  paint(img.data, size);
  ctx.putImageData(img, 0, 0);
  const tex = new THREE.CanvasTexture(cv);
  tex.colorSpace = srgb ? THREE.SRGBColorSpace : THREE.NoColorSpace;
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
  tex.repeat.set(repeat, repeat);
  tex.anisotropy = 8;
  return { tex, cv, ctx };
}

// ---------- environment: a studio rendered once into a PMREM ----------
export function makeEnvironment(renderer) {
  const env = new THREE.Scene();
  const sky = new THREE.Mesh(
    new THREE.SphereGeometry(50, 64, 32),
    new THREE.ShaderMaterial({
      side: THREE.BackSide,
      depthWrite: false,
      vertexShader: 'varying vec3 vDir; void main(){ vDir = normalize(position); gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
      fragmentShader: `varying vec3 vDir;
        void main(){
          float h = vDir.y;
          vec3 top = vec3(0.32, 0.36, 0.44), hor = vec3(0.16, 0.14, 0.13), bot = vec3(0.02);
          vec3 c = h > 0.0 ? mix(hor, top, pow(h, 0.7)) : mix(hor, bot, pow(-h, 0.35));
          gl_FragColor = vec4(c, 1.0);
        }`,
    }),
  );
  env.add(sky);
  const softbox = (w, h, pos, power, hex) => {
    const m = new THREE.Mesh(
      new THREE.PlaneGeometry(w, h),
      new THREE.MeshBasicMaterial({ color: new THREE.Color(hex).multiplyScalar(power), side: THREE.DoubleSide }),
    );
    m.position.copy(pos);
    m.lookAt(0, 0, 0);
    env.add(m);
  };
  softbox(16, 7, new THREE.Vector3(-12, 15, 9), 7, '#fff0dc'); // warm key
  softbox(7, 9, new THREE.Vector3(13, 7, -7), 3.5, '#d8e4ff'); // cool rim
  softbox(34, 1.6, new THREE.Vector3(0, 2.5, -20), 2.2, '#ffffff'); // horizon strip: long glints
  const pmrem = new THREE.PMREMGenerator(renderer);
  const rt = pmrem.fromScene(env, 0.015);
  pmrem.dispose();
  return rt.texture;
}

// ---------- slate ground ----------
export function makeGround() {
  const color = canvasTexture(1024, (d, n) => {
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const u = x / n, v = y / n;
      const layers = fbm(u * 0.6, v * 3.0, 11, 4, 4); // slate is layered: stretched noise
      const grain = fbm(u, v, 29, 3, 64);
      const g = 0.11 + 0.06 * layers + 0.03 * grain;
      const i = (y * n + x) * 4;
      d[i] = 255 * g * 0.96; d[i + 1] = 255 * g; d[i + 2] = 255 * g * 1.07; d[i + 3] = 255;
    }
  }, true, 6).tex;
  const rough = canvasTexture(512, (d, n) => {
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const r = 0.55 + 0.35 * fbm(x / n, y / n, 51, 4, 6);
      const i = (y * n + x) * 4;
      d[i] = d[i + 1] = d[i + 2] = 255 * r; d[i + 3] = 255;
    }
  }, false, 6).tex;
  const mesh = new THREE.Mesh(
    new THREE.PlaneGeometry(80, 80),
    new THREE.MeshStandardMaterial({ map: color, roughnessMap: rough, roughness: 1, metalness: 0, envMapIntensity: 0.6 }),
  );
  mesh.rotation.x = -Math.PI / 2;
  mesh.receiveShadow = true;
  return mesh;
}

// ---------- paper sheet with a printed ink line (seen double through calcite) ----------
export function makePaperTexture(w, h) {
  const size = 2048;
  const { tex, ctx } = canvasTexture(size, (d, n) => {
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const f = fbm(x / n, y / n, 71, 4, 48);
      const g = 0.93 + 0.05 * f;
      const i = (y * n + x) * 4;
      d[i] = 255 * g; d[i + 1] = 255 * g * 0.99; d[i + 2] = 255 * g * 0.965; d[i + 3] = 255;
    }
  });
  tex.wrapS = tex.wrapT = THREE.ClampToEdgeWrapping;
  tex.repeat.set(1, 1);
  // printed marks: one straight line and one dot, in the book's blue
  const px = (wx) => (wx / w + 0.5) * size; // world x on the sheet -> canvas x
  const py = (wz) => (wz / h + 0.5) * size; // world z on the sheet -> canvas y
  ctx.strokeStyle = '#1f4e79';
  ctx.lineWidth = size * 0.008;
  ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(px(-0.6), py(0.03)); ctx.lineTo(px(0.6), py(0.03)); ctx.stroke();
  ctx.fillStyle = '#1f4e79';
  ctx.beginPath(); ctx.arc(px(0.08), py(-0.12), size * 0.011, 0, Math.PI * 2); ctx.fill();
  tex.needsUpdate = true;
  return tex;
}

export function makeWoodTexture() {
  return canvasTexture(512, (d, n) => {
    for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
      const u = x / n, v = y / n;
      // grain runs along the board (v); rings bent by low-frequency noise
      const ring = 0.5 + 0.5 * Math.sin((u * 9 + 2.2 * fbm(u * 0.4, v * 0.6, 5, 4, 2)) * Math.PI * 2);
      const g = 0.5 + 0.1 * ring + 0.08 * fbm(u * 4, v * 0.3, 9, 3, 16);
      const i = (y * n + x) * 4;
      d[i] = 255 * g * 0.95; d[i + 1] = 255 * g * 0.66; d[i + 2] = 255 * g * 0.42; d[i + 3] = 255;
    }
  }).tex;
}

// ---------- parallelepiped of edge vectors a, b, c (three.js world, y up) ----------
// vertex index = i + 2j + 4k  <->  i*a + j*b + k*c
const QUADS = [[0, 2, 3, 1], [4, 5, 7, 6], [0, 1, 5, 4], [2, 6, 7, 3], [0, 4, 6, 2], [1, 3, 7, 5]];
export const EDGES = [];
for (let p = 0; p < 8; p++) for (const bit of [1, 2, 4]) if (!(p & bit)) EDGES.push([p, p | bit]);

export function corners(a, b, c, origin = new THREE.Vector3()) {
  const out = [];
  for (let k = 0; k < 2; k++) for (let j = 0; j < 2; j++) for (let i = 0; i < 2; i++) {
    out.push(origin.clone().addScaledVector(a, i).addScaledVector(b, j).addScaledVector(c, k));
  }
  return out;
}

/** Fill a non-indexed geometry (6 faces x 2 triangles) with outward-facing flat triangles. */
export function writeParallelepiped(geo, pts) {
  const pos = geo.attributes.position.array;
  const centre = new THREE.Vector3();
  pts.forEach((p) => centre.add(p));
  centre.multiplyScalar(1 / 8);
  const e1 = new THREE.Vector3(), e2 = new THREE.Vector3(), n = new THREE.Vector3(), fc = new THREE.Vector3();
  let o = 0;
  QUADS.forEach((q) => {
    let quad = q.map((i) => pts[i]);
    e1.subVectors(quad[1], quad[0]); e2.subVectors(quad[2], quad[0]); n.crossVectors(e1, e2);
    fc.set(0, 0, 0); quad.forEach((p) => fc.add(p)); fc.multiplyScalar(0.25).sub(centre);
    if (n.dot(fc) < 0) quad = [quad[0], quad[3], quad[2], quad[1]];
    for (const idx of [0, 1, 2, 0, 2, 3]) { pos[o++] = quad[idx].x; pos[o++] = quad[idx].y; pos[o++] = quad[idx].z; }
  });
  geo.attributes.position.needsUpdate = true;
  geo.computeVertexNormals();
  geo.computeBoundingSphere();
}

export function parallelepipedGeometry(pts) {
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(36 * 3), 3));
  const face = new Float32Array(36);
  for (let f = 0; f < 6; f++) face.fill(f, f * 6, f * 6 + 6);
  geo.setAttribute('faceId', new THREE.BufferAttribute(face, 1));
  writeParallelepiped(geo, pts);
  return geo;
}

export function edgeLines(pts, material) {
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(EDGES.length * 6), 3));
  const lines = new THREE.LineSegments(geo, material);
  writeEdges(lines, pts);
  return lines;
}
export function writeEdges(lines, pts) {
  const a = lines.geometry.attributes.position.array;
  EDGES.forEach(([p, q], k) => {
    a.set([pts[p].x, pts[p].y, pts[p].z, pts[q].x, pts[q].y, pts[q].z], k * 6);
  });
  lines.geometry.attributes.position.needsUpdate = true;
  lines.geometry.computeBoundingSphere();
}

/** Volume enclosed by a closed triangle mesh (divergence theorem); used by the tests. */
export function meshVolume(geo, matrix) {
  const p = geo.attributes.position, a = new THREE.Vector3(), b = new THREE.Vector3(), c = new THREE.Vector3();
  let v = 0;
  for (let i = 0; i < p.count; i += 3) {
    a.fromBufferAttribute(p, i).applyMatrix4(matrix);
    b.fromBufferAttribute(p, i + 1).applyMatrix4(matrix);
    c.fromBufferAttribute(p, i + 2).applyMatrix4(matrix);
    v += a.dot(b.cross(c)) / 6;
  }
  return Math.abs(v);
}
