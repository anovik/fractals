fractals.py --algorithm newton --colormap RdYlBu  --output newton.png
fractals.py --algorithm mandelbrot --colormap magma --xmin -2 --xmax 2 --ymin -2 --ymax 2 --output mandelbrot.png
fractals.py --algorithm julia  --c 0-0.8j --output julia1.png
fractals.py --algorithm julia  --c " -0.8+0.156j" --xmin -2 --xmax 2 --ymin -2 --ymax 2 --output julia2.png
fractals.py --algorithm burningShip --colormap hot --xmin -2 --xmax 2 --ymin -2 --ymax 2 --output burningShip.png