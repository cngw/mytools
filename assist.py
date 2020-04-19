from pathlib import Path

paths = list(Path('.').rglob('*'))

print(paths)