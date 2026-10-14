Measuring Distances
============================

Animal Echolocation
~~~~~~~~~~~~~~~~~~~~~~~

Information about our environment helps our robots perform complex tasks such as obstacle avoidance, navigation, and path planning. 

Similarly, animals like bats have evolved to use processes like echolocation which allow them to navigate through dark caves and find food where animals like bats emit high-frequency sound waves using their mouths. They listen to the echo of the sound waves bouncing back from the environment with their highly sensitive ears, allowing them to determine the size, shape, and texture of objects.

.. image:: media/batEcholocation.jpg
  
Using the Ultrasonic Sensor
---------------------------

.. image:: media/setpointtarget.png

While using the XRP, your distance sensor will be an ultrasonic range finder. Here is the method call to get the distance from the sensor:

.. tab-set:: 

    .. tab-item:: Python

        .. code-block:: python

          rangefinder.distance()

    .. tab-item:: Blockly

        .. image:: media/sonardistance.png
            :width: 300
    
This function returns the distance, in cm, from the sensor to the nearest object.


.. note:: Try it out!
  Try writing code that checks the distance every 50 ms (0.05 seconds) and prints the output.

.. collapse:: Here's the answer:

  .. tab-set:: 

      .. tab-item:: Python

          .. code-block:: python

            from XRPLib.defaults import *
            import time

            while True:
              print(rangefinder.distance())
              time.sleep(0.05)

      .. tab-item:: Blockly

          .. image:: media/printsonardistance.png
              :width: 300