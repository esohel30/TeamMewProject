from pathlib import Path
directory = Path('keys')
file_path = directory/'key_superhero.txt'

def get_key():
    with open(file_path) as f:
        key = f.read()
    #print(key)
    return key

if __name__ == '__main__':
    get_key()