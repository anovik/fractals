# Fractals

[Fractals](https://en.wikipedia.org/wiki/Fractal) using Python 3

# Description

Aim of the project is drawing of escape-time fractals. They currently include:

* [Mandelbrot fractal](https://en.wikipedia.org/wiki/Mandelbrot_set)

* [Julia fractal](https://en.wikipedia.org/wiki/Julia_set)

* [Burning ship fractal](https://en.wikipedia.org/wiki/Burning_Ship_fractal)

# Prerequisites

To run script you need the following to be installed:

* Python 3

* Mathplotlib

* Numpy

* Numba 

Simply launch fractal.py file and watch fractals! Or you can run demo.bat for getting the main fractal images.

# Images

    fractals.py --algorithm mandelbrot --colormap magma --xmin -2 --xmax 2 --ymin -2 --ymax 2

![Alt Mandelbrot](/images/mandelbrot.png?raw=true "Mandelbrot")

    fractals.py --algorithm julia  --c 0-0.8j
    
 ![Alt Julia](/images/julia0_8_j.png?raw=true "Julia")
 
     fractals.py --algorithm julia  --c " -0.8+0.156j" --xmin -2 --xmax 2 --ymin -2 --ymax 2
    
 ![Alt Julia](/images/julia0_8_0_156_j.png?raw=true "Julia")

    fractals.py --algorithm burningShip --colormap hot --xmin -2 --xmax 2 --ymin -2 --ymax 2

![Alt Burning Ship](/images/burningShip.png?raw=true "Burning Ship")


# License

License is [MIT](../master/LICENSE)


