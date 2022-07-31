# Painting_suggester

Painting a picture from an original art work - approach suggester



### The aim
From an input picture of a painting, be able to decompose that painting in n layers with as many diferent elements as the model is able to identify.
The extracted information is later disposed in an order given by the model so the final composition should match the initial picture.

#### Limitations
The project is limited to paintings produced from "wide brush strokes" or well defined elements as the next samples;

<img src="https://user-images.githubusercontent.com/103588816/182036596-73617949-76c0-47d2-bc99-c7006471135c.jpg" width="200" height="250" />
<img src="https://user-images.githubusercontent.com/103588816/182036324-4e4d7df0-059b-48cc-954d-5022c176267b.png" width="200" height="250" />

### Train the model
The model will be trained with a picture database which will be produced randomly. The pictures will be generated as matrices of 4 dimensions where:
- d1 Height
- d2 Width
- d3 RGB codification (r,g,b)
- d4 depth of the layer [0 to n_layers]

The model will be satisfactory if it is able to fulfill at least a **defined pct of match** to the original picture structure.
