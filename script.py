from pathlib import Path
import shutil
from collections import defaultdict

downloads = Path("C:\\Users\\User123\\Pictures")
filetype_dict = defaultdict(list)

for file_path in downloads.iterdir():
    if file_path.is_file():
        file_type = file_path.suffix[1:].lower()
        filetype_dict[file_path].append(file_path)

for file_type, files in filetype_dict.items():
    folder_name = downloads / f"{file_type}_folder"
    folder_name.mkdir(exist_ok=True)

    for file_path in files:
        new_file_path = folder_name / file_path.name
        shutil.move(str(file_path), str(new_file_path))