# Run

`python app.py`

This will start a flask webserver at port 5000

Live streaming from the webcam on the pi.

Using keys w, a, s, d, p you can control the motion of the car.

p is for stopping the car.

This accomplished by ajax calls at routes

```
 w -> /forward
 s -> /reverse
 a -> /left
 d -> /right
 p -> /stop
```

![Untitled drawing (5)](https://user-images.githubusercontent.com/30196830/108810912-2dfbf100-75d2-11eb-8e4c-8bbd49c53435.png)
