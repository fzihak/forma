#!/usr/bin/env node

const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

const platform = os.platform();
const arch = os.arch();

let binName = 'forma';
if (platform === 'win32') {
  binName += '.exe';
}

const binPath = path.join(__dirname, '..', 'dist', binName);

if (!fs.existsSync(binPath)) {
  console.error(`❌ Error: Forma binary not found at ${binPath}.`);
  console.error('Please ensure the postinstall script completed successfully.');
  process.exit(1);
}

// Pass all arguments to the Go binary
const args = process.argv.slice(2);
const result = spawnSync(binPath, args, { stdio: 'inherit' });

process.exit(result.status);
