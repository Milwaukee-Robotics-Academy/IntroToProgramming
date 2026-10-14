
The Encoders
============

.. comment out for later
    In the last lesson we mentioned *encoders*. What are they and what do they do?

    Encoders are sensors which measure how far each motor (and thus each wheel) has
    rotated. We mentioned that our motors aren't perfect, so when we tell them to go
    a certain effort we don't know how fast it is actually rotating. Encoders 
    measure exactly what the motor is doing and report this information back to the 
    XRP.

    .. image:: media/blog017-image001-disks-resolution.jpg

    An encoder uses a disk like the one above with alternating clear and black 
    squares. The disk is attached to the output shaft of the motor. A small light 
    is shined through the edge of the disk, and a sensor on the other side sees the
    light. When a black part of the disk is in front of the light, the sensor sees
    nothing. When a clear part of the disk is in front of the light, the sensor can
    see the light. As the disk rotates, the sensor constantly switches from seeing 
    and not seeing the light. The XRP can automatically count how many times it has
    switched between seeing and not seeing the light, and can use this to calculate 
    how far the wheel has moved.

    The size of the black and clear squares determines how *precise* the encoder is.
    As the squares get smaller, the light switches more times for the same amount of
    rotations of the wheel, and thus we can more precisely measure the distance. The
    downside of having really tiny squares is that the XRP's processor needs to work
    harder to keep up with counting all the switches. In the image above you can see
    some disks with different levels of precision.

.. tip:: 

    The disk and sensor in the XRP is hidden inside the motor's plastic case, so
    you won't be able to see them.

The XRP handles doing all the math to convert these switches into a real 
distance measurement for you, so you don't have to worry about it. We can use 
some new :code:`drivetrain` functions to see what the encoders are measuring:

.. tab-set:: 

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *
            from time import sleep

            while True:
                print(drivetrain.get_left_encoder_position()); # prints the left encoder position in centimeters
                print(f'Roll: {imu.get_roll():.2f}      Pitch: {imu.get_pitch():.2f}     Yaw: {imu.get_yaw():.2f}') # prints the IMU values
                sleep(1);

    .. tab-item:: Blockly

        .. image:: media/encoder.png
            :width: 300

This code uses something new: a :code:`while` *loop*. A :code:`while` loop will
run the code underneath it until a *condition* is no longer equal to
:code:`True`. In this case, the *condition* is the keyword :code:`True`, which
means that this code will run until :code:`True` doesn't equal :code:`True`.
Since this will never happen, the code will run forever unless you stop it 
manually on your computer.

.. tip:: 

    You will learn more about loops and conditions later in the course.

The code should run forever, display the drivetrain's left encoder position, and
then wait for one second. Then, it repeats and does this forever. If we didn't 
wait for one second, the XRP would read and send the encoder position to your 
computer as fast as it could (very fast!) which would be too much data for your 
computer to display at once on the screen.

.. admonition:: Try it out

    Try running this code to see what happens. Spin the left wheel of the XRP
    by hand and notice how the number changes.



