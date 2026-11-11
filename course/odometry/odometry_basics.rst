Understanding the basics of odometry is essential for programming your robot to move accurately and navigate its environment. This guide will introduce you to the fundamental concepts of odometry and how to implement them in your robot's code.
============================

Follow this guide to get started with understanding odometry.
.. tip:: 

    Open a new tab and go to the `WPILib Odometry <https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/swerve-drive-odometry.html>`_.

.. admonition:: Try it out

    Output the X, the Y and the Theta (heading) values to the dashboard :code:
    `SmartDashboard.putNumber("Odometry/Swerve/Heading", getPose().getRotation().getDegrees());
    SmartDashboard.putNumber("Odometry/Swerve/X", getPose().getX());
    SmartDashboard.putNumber("Odometry/Swerve/Y", getPose().getY());` 


.. tip:: 
    
    Build your code to test if it compiles. If it does not compile, check the error messages and fix the issues. If you are having trouble, ask for help from your instructor or a mentor.
