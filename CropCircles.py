from getMap import save_map
import subprocess

if __name__ == '__main__':
    save_map(40, -88)
    subprocess.run(['java', '-cp', '.', 'AddCropCircles', 'map.png'])
