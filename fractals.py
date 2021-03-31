#!/usr/bin/env python3

import argparse
import numpy as np
from numba import jit
import matplotlib.pyplot as plt
import time

DPI = 150


@jit(nopython=True, parallel=True, nogil=True)
def quadratic(z, c):
    return z**2 + c


@jit(nopython=True, parallel=True, nogil=True)
def burningShip(z, c):    
    return quadratic(np.abs(z.real) + 1j*np.abs(z.imag), c)
    
@jit(nopython=True, parallel=True, nogil=True)
def iterateFractal(algorithm, c, z0, iterationsNumber):
    z = 0
    if algorithm == "julia":
        z = z0
    for n in range(iterationsNumber):
        if z.real**2 + z.imag**2 > 4:
            return n        
        if algorithm == "mandelbrot":
            z = quadratic(z, z0)
        elif algorithm == "julia":
            z = quadratic(z, c)
        elif algorithm == "burningShip":
            z = burningShip(z, z0)       
        else:
            raise ValueError("Bad algorithm value");
             
    return 0   

@jit(nopython=True, parallel=True, nogil=True)
def buildFractal(algorithm, c, xmin,xmax,ymin,ymax,width,height,iterationsNumber):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for k in range(height):
            n3[i,k] = iterateFractal(algorithm, c, r1[i] + 1j*r2[k], iterationsNumber)            
    return (r1,r2,n3)

def drawPlot(algorithm, colormap, c, xmin,xmax,ymin,ymax,width=10,height=10,iterationsNumber=256, filename = "fractal.png"):    
    img_width = DPI * width
    img_height = DPI * height
    x,y,z = buildFractal(algorithm, c, xmin,xmax,ymin,ymax,img_width,img_height,iterationsNumber)
    
    fig, ax = plt.subplots(figsize=(width, height), dpi=DPI)          
    plt.xticks([]) 
    plt.yticks([]) 
	
    ax.imshow(z.T, cmap = colormap, origin='lower')

    fig.show()
    
    fig.savefig(filename)

def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('--algorithm', nargs='?', choices=['mandelbrot', 'burningShip', 'julia'],
                        default='mandelbrot', help='Fractal algorithm')
    parser.add_argument("--colormap", nargs='?', default='hot', help='Plot colormap')
    parser.add_argument('--c', nargs='?', type=complex, default = -0.8j, help = 'Complex argument for Julia set')
    parser.add_argument('--xmin',nargs='?', type=float, default = -1.5, help = 'Minimal value on x axis')
    parser.add_argument('--xmax', nargs='?', type=float, default = 1.5, help = 'Maximum value on x axis')
    parser.add_argument('--ymin', nargs='?', type=float, default = -1.5, help = 'Minimal value on y axis')
    parser.add_argument('--ymax', nargs='?', type=float, default = 1.5, help = 'Maximum value on y axis')
    parser.add_argument('--output', nargs='?', default = "fractal.png", help = 'Output filename')

    return parser.parse_args()

def main():
    args = parseArgs()
    start_time = time.time()
    drawPlot(args.algorithm, args.colormap, args.c, args.xmin, args.xmax, args.ymin, args.ymax, filename = args.output)   
    print("--- %.2f seconds ---" % (time.time() - start_time))	

main()
