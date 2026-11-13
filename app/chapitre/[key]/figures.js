// Interactive figures for the converted books (physique, …).
// public/<dir>/fig/index.json lists the figure ids ("c036/p0416_1") that have a module
// public/<dir>/fig/<id>.js exporting mount(el). The static SVG (<img class="vf">) stays in the page:
// it is shown until the module has drawn, if the module fails, and when printing.

/** @param {HTMLElement} root  chapter container  @param {string} dir  folder of public/ */
export function enhanceFigures(root, dir) {
  if (dir === 'chapters' || !('IntersectionObserver' in window)) return;
  fetch(`/${dir}/fig/index.json`)
    .then((r) => (r.ok ? r.json() : []))
    .then((ids) => {
      const known = new Set(ids);
      const re = new RegExp(`^/${dir}/img/(c\\d+/[^/.]+)\\.svg$`);
      const targets = [...root.querySelectorAll('img.vf')].filter((img) => {
        const m = re.exec(new URL(img.src, window.location.href).pathname);
        return m && known.has(m[1]) && (img.dataset.fig = m[1]);
      });
      if (!targets.length) return;
      const io = new IntersectionObserver(
        (entries) => {
          for (const e of entries) {
            if (!e.isIntersecting) continue;
            io.unobserve(e.target);
            mount(e.target, `/${dir}/fig/${e.target.dataset.fig}.js`);
          }
        },
        { rootMargin: '400px 0px' },
      );
      targets.forEach((img) => io.observe(img));
    })
    .catch((err) => console.error('figures interactives :', err));
}

/** Load the module with a native import (outside the bundler) and let it draw next to the image. */
function mount(img, url) {
  const box = document.createElement('div');
  box.className = 'fi';
  img.after(box);
  const slots = (window.__figSlots = window.__figSlots || []);
  const i = slots.push({ box, img }) - 1;
  const s = document.createElement('script');
  s.type = 'module';
  s.textContent =
    `const f = window.__figSlots[${i}];` +
    `import(${JSON.stringify(url)})` +
    `.then((m) => { m.mount(f.box); f.img.classList.add('fi-done'); })` +
    `.catch((e) => { console.error(${JSON.stringify(url)}, e); f.box.remove(); });`;
  document.head.appendChild(s);
}
