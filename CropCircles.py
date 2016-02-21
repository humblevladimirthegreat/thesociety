from getMap import save_map
import subprocess

if __name__ == '__main__':
    #use 40, -88
    the_input = input("Input latitude, longitude coordinates separated by comma\n")
    lat, lon = the_input.split(',')
    lat, lon = float(lat), float(lon)
    save_map(lat, lon)
    subprocess.run(['java', '-cp', '.', 'AddCropCircles', 'map.png'])
