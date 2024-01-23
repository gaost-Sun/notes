
# instant-ngp experiment notes

### Exp1: Decomposition Stage

-   Setting && Indexes
    - GPU: 4060ti 16G
    - Parameter: Nmin=16, b=1.31951, F=2, T=2^19, L=16
    - Dataset: nerf_synthetic(hotdog\materials\chair\drums\ficus: 100 train images, 200 test images)
    - Epoch number：10\40\40\40
    - Training + testing time: 6min 40s\37min 24s\30min 11s
    - PSNR(train): 38.00\34.80\29.60
    - PSNR(test): 36.00\29.20\25.70

-   Network
    <center>
    <img
    src="img/Network1(decomposition：ref and illu)_00.jpg" width = "80%" />
    </center>
-   GT && Results deconposition views

 <center>
    <img 
    src="img/r_0.png" width = "50%" />
    <div padding: 2px;">
      Ground Truth
  	</div>
<br>
<br>
    <img 
    src="img/000.png" width = "24%" />
    <img
    src="img/000_d.png" width = "24%" />
    <img
    src="img/000_illu.png" width = "24%" />
    <img
    src="img/000_ref.png" width = "24%" />

<br>
    <div padding: 2px;">
      composition、depth、illumination、reflectance
  	</div>
    <br>
    <img 
    src="img/r_145.png" width = "50%" />
    <div padding: 2px;">
      Ground Truth
  	</div>
<br>
<br>
    <img 
    src="img/145.png" width = "24%" />
    <img
    src="img/145_d.png" width = "24%" />
    <img
    src="img/145_illu.png" width = "24%" />
    <img
    src="img/145_ref.png" width = "24%" />
    <br>
    <div>
      composition、depth、illumination、reflectance
  	</div>
    <br>
    <img 
    src="img/r_166.png" width = "50%" />
    <div padding: 2px;">
      Ground Truth
  	</div>
<br>
<br>
    <img 
    src="img/166.png" width = "24%" />
    <img
    src="img/166_d.png" width = "24%" />
    <img
    src="img/166_illu.png" width = "24%" />
    <img
    src="img/166_ref.png" width = "24%" />
    <br>
    <div>
      composition、depth、illumination、reflectance
  	</div>
</center>
<br>

-   Indexes



| datasets  | PSNR(train) | PSNR(test) | train+test time(min:s) |
|:---------:|:-----------:|:----------:|:----------------------:|
|  hotdog   |    38.00    |   36.00    |          6:40          |
| materials |    34.80    |   29.20    |         37:24          |
|   drums   |    29.60    |   25.70    |         30:11          |




-   Issues and Analysis
    - The decomposition part of refectance is not complete(has illumination residual)<br> 
    - <center><img src="img/000_ref_edit.png" width = "50%" /></center>
    - The possible reasons for the above issue is that the **light source** is same in different views. 
    It is hard to completely decompose the illuminaiton and the reflectance.
<br>
    
### Exp2: Enhancement Stage

-   Dataset changes
    - linear adjustment of illumination(0.1、0.5、1)
    <center>
    <img 
    src="img/r_0_0.png" width = "32%" />
    <img
    src="img/r_0_1.png" width = "32%" />
    <img
    src="img/r_0_2.png" width = "32%" />
    <img 
    src="img/r_15_0.png" width = "32%" />
    <img
    src="img/r_15_1.png" width = "32%" />
    <img
    src="img/r_15_2.png" width = "32%" />
    <img 
    src="img/r_40_0.png" width = "32%" />
    <img
    src="img/r_40_1.png" width = "32%" />
    <img
    src="img/r_40_2.png" width = "32%" />
    <div>linear adjustment factor=0.1、0.5、1</div>
    </center>
    <br>
    
    - add illumination factor into network
-   network
-   training strategy
-   results
-   Issues and Analysis

