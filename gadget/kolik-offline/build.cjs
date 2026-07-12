const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

let marked;
try {
  ({ marked } = require('marked'));
} catch {
  throw new Error('Chybí build-time balíček marked. Spusť npm install.');
}

const root = path.resolve(__dirname, '../..');
const sourceRoot = path.join(root, 'revize-v2', 'knihy');
const distRoot = path.join(__dirname, 'dist');
const templatePath = path.join(__dirname, 'template.html');

const books = [
  ['kniha-1-vesnice', '01', 'Vesnice'],
  ['kniha-2-trasy', '02', 'Trasy'],
  ['kniha-3-etalon', '03', 'Etalon'],
  ['kniha-4-archiv', '04', 'Archiv'],
  ['kniha-5-kopie-00', '05', 'Kopie 00'],
];

function clean() {
  fs.rmSync(distRoot, { recursive: true, force: true });
  fs.mkdirSync(distRoot, { recursive: true });
}

function publicFiles(bookDir) {
  return fs.readdirSync(bookDir)
    .filter((name) => /^(00|0[1-8])-[^.]+\.md$/.test(name))
    .sort();
}

function firstHeading(markdown, fallback) {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : fallback;
}

function renderBooks() {
  const nav = [];
  const sections = [];

  for (const [slug, number, title] of books) {
    const bookDir = path.join(sourceRoot, slug);
    const outputDir = path.join(distRoot, 'knihy', slug);
    fs.mkdirSync(outputDir, { recursive: true });

    const chapterLinks = [];
    for (const filename of publicFiles(bookDir)) {
      const markdown = fs.readFileSync(path.join(bookDir, filename), 'utf8');
      fs.writeFileSync(path.join(outputDir, filename), markdown);

      const chapterSlug = `${slug}-${filename.replace(/\.md$/, '')}`;
      const chapterTitle = firstHeading(markdown, filename);
      const body = marked.parse(markdown.replace(/^#\s+.+\r?\n/, ''), {
        gfm: true,
        mangle: false,
        headerIds: false,
      });

      chapterLinks.push(`<li><a href="#${chapterSlug}">${chapterTitle}</a></li>`);
      sections.push(`
        <article class="chapter" id="${chapterSlug}" data-book="${slug}">
          <p class="chapter-kicker">Kniha ${number} · ${title}</p>
          <h2>${chapterTitle}</h2>
          <div class="chapter-body">${body}</div>
          <a class="back-link" href="#cist">Zpět k obsahu ↑</a>
        </article>`);
    }

    nav.push(`
      <details ${number === '01' ? 'open' : ''}>
        <summary>${number} · ${title}</summary>
        <ol>${chapterLinks.join('')}</ol>
      </details>`);
  }

  return { nav: nav.join(''), sections: sections.join('') };
}

function sha256(filePath) {
  return crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
}

function allFiles(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(dir, entry.name);
    return entry.isDirectory() ? allFiles(full) : [full];
  });
}

function writeIntegrityFiles() {
  const files = allFiles(distRoot)
    .filter((file) => !file.endsWith('SHA256SUMS.txt') && !file.endsWith('release-manifest.json'))
    .sort();
  const entries = files.map((file) => ({
    path: path.relative(distRoot, file).split(path.sep).join('/'),
    sha256: sha256(file),
    bytes: fs.statSync(file).size,
  }));
  const manifest = {
    schema: 1,
    release_id: 'prototype-2026-07-11',
    title: 'Smazaná odpověď — Kolík',
    signed: false,
    files: entries,
  };
  const manifestPath = path.join(distRoot, 'release-manifest.json');
  fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);

  const sums = [...entries, {
    path: 'release-manifest.json',
    sha256: sha256(manifestPath),
  }].map((entry) => `${entry.sha256}  ${entry.path}`).join('\n');
  fs.writeFileSync(path.join(distRoot, 'SHA256SUMS.txt'), `${sums}\n`);
}

function build() {
  clean();
  const { nav, sections } = renderBooks();
  const template = fs.readFileSync(templatePath, 'utf8');
  const html = template
    .replace('<!-- BOOK_NAV -->', nav)
    .replace('<!-- BOOK_SECTIONS -->', sections);
  fs.writeFileSync(path.join(distRoot, 'index.html'), html);
  fs.writeFileSync(path.join(distRoot, 'START-HERE.txt'), [
    'SMAZANÁ ODPOVĚĎ — KOLÍK / PROTOTYP',
    '',
    '1. Pokud nevíš, odkud tento USB disk je, nepřipojuj ho k osobnímu počítači.',
    '2. Ověřenou kopii otevři ručně a spusť index.html v prohlížeči.',
    '3. Nic se neinstaluje a nic se nespouští automaticky.',
    '4. Markdownové zdroje knih jsou ve složce knihy/.',
    '5. Integritu souborů ověříš proti SHA256SUMS.txt.',
    '',
    'Prototypový manifest ještě není digitálně podepsán.',
    '',
  ].join('\n'));
  writeIntegrityFiles();
  console.log(`Kolík vytvořen: ${distRoot}`);
}

build();

