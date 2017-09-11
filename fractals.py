#!/usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt

DPI = 72

def mandelbrot(c,iterationsNumber):
    z = c
    for n in range(iterationsNumber):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0

def burningShip(c,iterationsNumber):
    z = c
    for n in range(iterationsNumber):
        if abs(z) > 2:
            return n
        z = pow(abs(z.real) + 1j*abs(z.imag), 2) + c
    return 0

def buildFractal(algorithm, xmin,xmax,ymin,ymax,width,height,iterationsNumber):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            if algorithm == "mandelbrot":
                n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],iterationsNumber)
            elif algorithm == "burningShip":
                n3[i,j] = burningShip(r1[i] + 1j*r2[j],iterationsNumber)
            else:
                raise ValueError("Bad algorithm value")
    return (r1,r2,n3)

def drawPlot(algorithm, xmin,xmax,ymin,ymax,width=10,height=10,iterationsNumber=256):    
    img_width = DPI * width
    img_height = DPI * height
    x,y,z = buildFractal(algorithm, xmin,xmax,ymin,ymax,img_width,img_height,iterationsNumber)
    
    fig, ax = plt.subplots(figsize=(width, height), dpi=DPI)
    ticks = np.arange(0,img_width,3*DPI)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    plt.yticks(ticks, y_ticks)
    
    ax.imshow(z.T,origin='lower')

    fig.show()
    
    fig.savefig("fractal.png")

def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('algorithm', nargs='?', choices=['mandelbrot', 'burningShip'],
                        default='mandelbrot', help='Fractal algorithm')
    parser.add_argument('xmin',nargs='?', type=float, default = -1.5, help = 'Minimal value on x axis')
    parser.add_argument('xmax', nargs='?', type=float, default = 1.5, help = 'Maximum value on x axis')
    parser.add_argument('ymin', nargs='?', type=float, default = -1.5, help = 'Minimal value on y axis')
    parser.add_argument('ymax', nargs='?', type=float, default = 1.5, help = 'Maximum value on y axis')

    return parser.parse_args()

def main():
    args = parseArgs()
    drawPlot(args.algorithm, args.xmin, args.xmax, args.ymin, args.ymax)    

main()
