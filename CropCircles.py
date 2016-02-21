from getMap import save_map
import subprocess

if __name__ == '__main__':
    #use 40, -88
    lat = float(input("Input latitude coordinate:"))
    lon = float(input("Input longitude coordinate:"))
    save_map(lat, lon)
    subprocess.run(['java', '-cp', '.', 'AddCropCircles', 'map.png'])
