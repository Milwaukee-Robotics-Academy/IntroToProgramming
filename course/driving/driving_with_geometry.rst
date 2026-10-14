Driving With Geometry
=====================

The XRP's driving and turning functions can also be used to draw geometric patterns!
By driving a set distance and turning by a certain angle several times, you can draw a 
shape with as many sides as you want.

.. tip:: 

    To see the path your XRP has driven, you can place a dry-erase marker between the
    robot's wheels and trace your pattern on a whiteboard.


To draw any polygon, you just need to know the size of the shape's exterior angles,
and you need to decide how long the sides should be. Then, you just have to drive straight with the distance
of a side length and turn the number of degrees of the corresponding exterior angle.
Repeat this until the shape is finished.

.. image:: media/exterior-angle.png

Triangle
--------

For a triangle, the interior angles measure 60 degrees and the exterior angles measure 120 degrees.
We can trace a triangle with side lengths of 10 cm by having our robot drive straight for 10 cm
three times and turn 120 degrees in between each drive straight.  


.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *
            
            board.wait_for_button();
            drivetrain.straight(10);
            drivetrain.turn(120);
            drivetrain.straight(10);
            drivetrain.turn(120);
            drivetrain.straight(10);

    .. tab-item:: Blockly

        .. image:: media/triangle-blockly.png
            :width: 300


Square
------

The process for tracing a square is similar to tracing a triangle. The interior angles are 90 degrees so
the exterior angles are also 90 degrees. Keeping a side length of 10 cm, we can trace a square by 
programming our robot to drive straight for 10 cm four times and turn 90 degrees between each drive straight.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import * 
            board.wait_for_button();
            drivetrain.straight(10);
            drivetrain.turn(90);
            drivetrain.straight(10);
            drivetrain.turn(90);
            drivetrain.straight(10);
            drivetrain.turn(90);
            drivetrain.straight(10);

    .. tab-item:: Blockly

        .. image:: media/square-blockly.png
            :width: 300



Polygons
--------

We can generalize the procedure used to make a triangle and square to make any regular polygon; you just have to
determine the exterior angle and choose a side length. However, for polygons with many sides, this process can get very tedious. 
Instead of repeating the same code multiple times, we can use a function to simplify the process. 

First, lets determine what information the function needs. To trace a polygon, you need to determine the number of sides 
and the length of each side. We can create a function that takes these two values as an input. 
The function will drive the distance we give it, turn by the exterior angle, and then repeat that process
as many times as there are sides in the shape. We can use a loop for this. The one problem is:
how do we know the measure of the exterior angles? Fortunately, this can be easily calculated with this equation:

.. math:: 
    360/n

With the variable *n* representing the number of sides of your polygon, this equation 
determines the number of degrees of your polgyon's exterior angles. With this information, you 
can now write a function to trace any regular polygon!

.. code-block:: python

    from XRPLib.defaults import *

    def polygon(sideLength, numSides):
        for i in range(int(numSides)):
            drivetrain.straight(sideLength);
            drivetrain.turn((360 / numSides));
            
    board.wait_for_button();
    polygon(10,4);


