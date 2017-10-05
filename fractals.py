#!/usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt
import math

DPI = 150

def quadratic(z, c):
    return z*z + c

def burningShip(z, c):    
    return quadratic(math.fabs(z.real) + 1j*math.fabs(z.imag), c)
    
def iterateFractal(algorithm, c, z0, iterationsNumber):
    z = 0
    if algorithm == "julia":
        z = z0
    for n in range(iterationsNumber):
        if z.real*z.real + z.imag*z.imag > 4:
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

def buildFractal(algorithm, c, xmin,xmax,ymin,ymax,width,height,iterationsNumber):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for k in range(height):
            n3[i,k] = iterateFractal(algorithm, c, r1[i] + 1j*r2[k], iterationsNumber)            
    return (r1,r2,n3)

def drawPlot(algorithm, colormap, c, xmin,xmax,ymin,ymax,width=10,height=10,iterationsNumber=256):    
    img_width = DPI * width
    img_height = DPI * height
    x,y,z = buildFractal(algorithm, c, xmin,xmax,ymin,ymax,img_width,img_height,iterationsNumber)
    
    fig, ax = plt.subplots(figsize=(width, height), dpi=DPI)
    ticks = np.arange(0,img_width,3*DPI)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    plt.yticks(ticks, y_ticks)
    
    ax.imshow(z.T, cmap = colormap, origin='lower')

    fig.show()
    
    fig.savefig("fractal.png")

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

    return parser.parse_args()

def main():
    args = parseArgs()
    drawPlot(args.algorithm, args.colormap, args.c, args.xmin, args.xmax, args.ymin, args.ymax)    

main()
