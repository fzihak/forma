import sys
import os
import hashlib
import json
import time
from datetime import datetime

HISTORY_FILE = os.path.join(os.getcwd(), 'design-system', '.history.json')

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def ensure_history_dir():
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump({"versions": []}, f)

def commit_version(message="System generated snapshot"):
    ensure_history_dir()
    
    ds_md = os.path.join(os.getcwd(), 'design-system', 'MASTER.md')
    ds_tokens = os.path.join(os.getcwd(), 'design-system', 'MASTER.tokens.json')
    
    if not os.path.exists(ds_md) or not os.path.exists(ds_tokens):
        print("❌ Cannot version: MASTER.md or MASTER.tokens.json not found.")
        sys.exit(1)
        
    version_id = get_file_hash(ds_tokens)[:8]
    
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        history = json.load(f)
        
    # Check if already exists
    for v in history.get('versions', []):
        if v['id'] == version_id:
            print(f"ℹ️ Snapshot unchanged. Current version: {version_id}")
            return
            
    snapshot = {
        "id": version_id,
        "timestamp": datetime.now().isoformat(),
        "message": message,
        "md_hash": get_file_hash(ds_md),
        "tokens_hash": get_file_hash(ds_tokens)
    }
    
    history['versions'].append(snapshot)
    
    # Save backups of the files
    backup_dir = os.path.join(os.getcwd(), 'design-system', '.backups', version_id)
    os.makedirs(backup_dir, exist_ok=True)
    
    with open(ds_md, 'r', encoding='utf-8') as src, open(os.path.join(backup_dir, 'MASTER.md'), 'w', encoding='utf-8') as dst:
        dst.write(src.read())
        
    with open(ds_tokens, 'r', encoding='utf-8') as src, open(os.path.join(backup_dir, 'MASTER.tokens.json'), 'w', encoding='utf-8') as dst:
        dst.write(src.read())
        
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)
        
    print(f"✅ Version saved: {version_id} ({message})")

def list_versions():
    if not os.path.exists(HISTORY_FILE):
        print("No version history found.")
        return
        
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        history = json.load(f)
        
    print("\n" + "="*50)
    print(" 🕒 FORMA VERSION HISTORY")
    print("="*50 + "\n")
    
    for v in reversed(history.get('versions', [])):
        dt = datetime.fromisoformat(v['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{v['id']}] {dt} - {v['message']}")
        
    print("\n" + "="*50 + "\n")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python version.py commit \"Commit message\"")
        print("  python version.py log")
        sys.exit(1)
        
    action = sys.argv[1]
    
    if action == "commit":
        message = sys.argv[2] if len(sys.argv) > 2 else "System generated snapshot"
        commit_version(message)
    elif action == "log":
        list_versions()
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
