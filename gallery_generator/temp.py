import config









from pathlib import Path

path = Path(config.current_path+'\Canada')
dirs = [e for e in path.iterdir() if e.is_file()]
print(dirs)

