Swerve Drive with YAGSL
=======================

**YAGSL** (*Yet Another Generic Swerve Library*) is a JSON-configured swerve drive library built on top of WPILib. Instead of hand-writing low-level swerve module kinematics, PID wiring, and encoder math from scratch, YAGSL lets you describe your physical robot in JSON configuration files and focus on driving, autonomous paths, and mechanisms.

For full API reference, see the official `YAGSL Documentation <https://yagsl.yassrobotics.com/>`_.

Module Objectives
-----------------

By the end of this module, you will be able to:

* Gather your robot's swerve hardware measurements and generate YAGSL JSON configuration files.
* Install YAGSL as a WPILib vendor dependency and integrate the YAGSL example code.
* Simulate your swerve drive in WPILib and visualize robot poses on the AdvantageScope 2D Field.
* Publish swerve odometry (X, Y, and heading) using the WPILib 2027 Telemetry API.

.. toctree::
   :maxdepth: 1

   setup_and_config
   writing_and_sim
   odometry
