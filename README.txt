

files:

 - basic_raycasting.py
       simple raycasting with sphere intersection
       run with: 'python main.py basic'
 - illuminated_raycasting.py
       adds illumination
       run with: 'python main.py illum'
 - shadows_raycasting.py
       adds shadows
       run with: 'python main.py shadows'
 - basic_raytracer.py
       recursive raycasting - reflections
       run with: 'python main.py raytracer'


- main.py
      top level file responsible for that draws the rendered image
      using turtle graphics or using png intermediary image for speed
       
- world.py
      defines the spheres to be rendered, and various configuration parameters
              
- things.py
      defines sphere and vector abstractions, and a few utilities



NOTE:
  If you get the error "ImportError: No module named png" you are probably
  on a system that does not support symbolic links. To fix this copy
  raytracer_intro/pypng/code/png.py to raytracer_intro/png.py

