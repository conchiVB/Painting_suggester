# Painting_suggester

Painting a picture from an original art work - approach suggester



#### The aim
From an input picture of a painting, be able to decompose that painting in n layers with as many diferent elements as the model is able to identify.
The extracted information is later disposed in an order given by the model so the final composition should match the initial picture.

### Limitations
The project is limited to paintings produced from "wide brush strokes" or definded elements as the next samples
https://images.squarespace-cdn.com/content/v1/595de185b8a79be945fafe8e/1589195266565-HKRL8V2VPD9F4XK0UM41/Screen+Shot+2020-05-11+at+9.00.16+pm.png?format=1000w


#### Model
The model will be trained with a picture database produced randomly. The pictures will be generated as matrices of 4 dimensions:
- d1 Height
- d2 Width
- d3 RGB codification (r,g,b)
- d4 depth of the layer [0 to n_layers]
