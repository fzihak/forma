const fs = require('fs');
const path = require('path');
const os = require('os');
const { execSync } = require('child_process');

console.log('Fetching Forma CLI binaries...');

const platform = os.platform();
const arch = os.arch();

let osName = '';
if (platform === 'win32') osName = 'windows';
else if (platform === 'darwin') osName = 'darwin';
else if (platform === 'linux') osName = 'linux';
else {
  console.error(`Unsupported platform: ${platform}`);
  process.exit(1);
}

let archName = '';
if (arch === 'x64') archName = 'amd64';
else if (arch === 'arm64') archName = 'arm64';
else {
  console.error(`Unsupported architecture: ${arch}`);
  process.exit(1);
}

const version = require('../package.json').version;
let binName = `forma-${osName}-${archName}`;
if (osName === 'windows') binName += '.exe';

const downloadUrl = `https://github.com/fzihak/forma/releases/download/v${version}/${binName}`;
const distDir = path.join(__dirname, '..', 'dist');

if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir);
}

const finalBinName = osName === 'windows' ? 'forma.exe' : 'forma';
const destPath = path.join(distDir, finalBinName);

console.log(`Downloading ${downloadUrl}...`);

// Use curl or wget to download the binary depending on the system
try {
  if (platform === 'win32') {
    execSync(`powershell -Command "Invoke-WebRequest -Uri '${downloadUrl}' -OutFile '${destPath}'"`);
  } else {
    execSync(`curl -L -o "${destPath}" "${downloadUrl}"`);
    execSync(`chmod +x "${destPath}"`);
  }
  console.log('✅ Forma CLI installed successfully!');
} catch (error) {
  console.log('⚠️ Failed to download binary. You may need to compile it manually from the repository.');
}
