import numpy as np

def main():
    for i in range(18):
        string = ""
        if i>9:
            string = f'000{i}'
        else:
            string = f'0000{i}'
        filename = f'data/Guineapig2022_{string}.asd.sco.txt'
        data = np.loadtxt(filename)
        spectralon = np.loadtxt("data/spectralon.txt")
        out = data[:,1]*spectralon
        
        np.savetxt(f'corrected_spectra/{string}.txt', out)

if __name__ == '__main__':
    main()