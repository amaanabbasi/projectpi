# Run

`python app.py`

This will start a flask webserver at port 5000

Live streaming from the webcam on the pi.

Using keyboard keys w, a, s, d, p you can control the motion of the car.

p is for stopping the car.

This accomplished by ajax calls at routes

```
 w -> /forward
 s -> /reverse
 a -> /left
 d -> /right
 p -> /stop
```
