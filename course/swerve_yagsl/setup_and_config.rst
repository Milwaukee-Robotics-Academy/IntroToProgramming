YAGSL Setup & Configuration
===========================

We follow the official `YAGSL Getting Started Tutorial <https://yagsl.yassrobotics.com/get-started/tutorial>`_ tailored to Milwaukee Robotics Academy's 2027 swerve chassis.

1. Gather Your Robot Information
--------------------------------

Before generating configuration files, collect the mechanical and electrical details for your swerve drivetrain (module type, drive/angle motor types, gear ratios, CAN IDs, and encoders):

* For this workshop, we start from **last year's robot chassis, motors, and sensors**.
* **Gyro update**: Unlike last year, we are using a **Pigeon 2** gyro in this 2027 setup.
* Follow the checklist in `Step 1 — Gather Your Robot Information <https://yagsl.yassrobotics.com/get-started/01-gather-your-robot-information>`_.

2. Generate Your YAGSL Configuration
------------------------------------

YAGSL provides a web-based generator that produces the JSON files describing your robot's swerve modules, physical dimensions, and PID defaults:

1. Open the `YAGSL Configuration Tool <https://config.yagsl.com/>`_.
2. Follow `Step 2 — Generate Your YAGSL Configuration <https://yagsl.yassrobotics.com/get-started/02-generate-your-yagsl-configuration>`_ using the measurements you gathered in Step 1.
3. Place the generated ``swerve/`` JSON configuration folder into your robot project's deploy directory (``src/main/deploy/swerve`` — or ``src/main/resources`` if specified by your 2027 YAGSL template).

.. note::

   If you are upgrading an existing MRA robot, compare your generated JSON files against last year's ``src/main/deploy/swerve`` configs to double-check CAN IDs, encoder offsets, and motor inversions before deploying to hardware.

3. Install YAGSL Vendor Dependency
----------------------------------

Install YAGSL into your WPILib project using the WPILib Vendor Dependency Manager:

* Follow `Step 3 — Install YAGSL <https://yagsl.yassrobotics.com/get-started/03-install-yagsl>`_.
* Run a test build (``WPILib: Build Robot Code``) to confirm Gradle resolves the vendor dependency without errors.
