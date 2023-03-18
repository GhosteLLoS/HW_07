import sys
from pathlib import Path
from shutil import unpack_archive

CATEGORIES = {
    'audio': ['.mp3', '.aiff'],
    'image': ['.JPEG', '.PNG', '.JPG', '.SVG'],
    'video' : ['.AVI', '.MP4', '.MOV', '.MKV']
    
}


def unpack_zip():
    unpack = unpack_archive('path_to_archive', 'path_to_destination_folder', )
    
    return unpack




def move_file(file:Path, root_dir:Path, category:str):
    if category == 'unknown':
        return file.replace(root_dir.joinpath(file.name))


    target_dir = root_dir.joinpath(category)

    if not target_dir.exists():
        target_dir.mkdir()
    return file.replace(target_dir.joinpath(file.name))

def get_categories(file:Path):
    extension = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if extension in exts:
            return cat
    return 'unknown'

def sort_dir(root_dir:Path, current_dir:Path):

    for item in [f for f in current_dir.glob('*') if f.name and f.is_dir() not in CATEGORIES.keys()]:
        if not item.is_dir():
            category = get_categories(item)
            new_path = move_file(item, root_dir, category)
            print(new_path)
        else:
            sort_dir(root_dir, item)
            item.rmdir()

def main():
    try:
        path = Path(sys.argv[1])
        # return "All ok"
    except IndexError:
        return f"No path to folder. Take as parameter"
    
    if not path.exists():
        return "Sorry, folder not exists"
    
    sort_dir(path, path)


    return "All ok"
    


if __name__ == "__main__":
    print(main())


