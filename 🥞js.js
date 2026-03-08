const readline = require('readline');
const fs = require('fs');
const { exec } = require('child_process');
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const clearScreen = () => exec(process.platform === 'win32' ? 'cls' : 'clear', { stdio: 'inherit' });
const ask = (rl, query) => new Promise(resolve => rl.question(query, resolve));
(async () => {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: true });
  const history = [];
  while (true) {
    while (true) {
      const command = await ask(rl, '🥞 </> (  ');
      if (command === 'run') { console.log('</> (🥞) -1/2-'); break; }
      if (command.includes('name')) { history.push(command); break; }
      if (command === 'clear') {
        for (let i = 0; i < 4; i++) { console.log(['.  ', '.. ', '...'][i % 3]); await sleep(500); }
        history.push(command); break;
      }
      history.push(command);
    }
    console.log('</> (🥞) -  ');
    for (const cmd of history) {
      if (history.includes('txt')) console.log(`</>  ${cmd}`);
      if (history.includes('hw')) console.log('</>  Hello World!');
      if (history.includes('clear')) { history.length = 0; clearScreen(); console.log('</>  history cleared'); }
      if (history.includes('option')) {
        history.length = 0;
        console.log('</>  txt = what you type will type back'); await sleep(3000);
        console.log('</>  hw = print Hello World'); await sleep(3000);
        console.log('</>  clear = clear past commands'); await sleep(3000);
        console.log('</>  search = command vocab'); await sleep(3000);
        console.log('</>  name = file a new file'); await sleep(3000);
        console.log('</>  save = save a file must be under name'); await sleep(3000);
      }
      if (history.includes('name')) console.log('code or txt');
    }
    await sleep(200);
    const fullCode = [];
    while (true) {
      await sleep(500);
      const line = await ask(rl, ' -  ');
      if (line === 'save') break;
      fullCode.push(line);
    }
    await sleep(200);
    const fileName = await ask(rl, 'file name -  ');
    try {
      fs.appendFileSync(fileName, fullCode.map(l => `${l}\n`).join(''), 'utf8');
      console.log('file successfully saved!');
    } catch (err) { console.error('Error while saving the file:', err); }
  }
})();
