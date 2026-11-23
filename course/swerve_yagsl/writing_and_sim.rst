Writing & Simulating Swerve Code
================================

Once YAGSL is installed and your JSON configuration files are in place, wire up the swerve subsystem and verify it in simulation before touching physical hardware.

1. Write the Code
-----------------

Use the YAGSL example project as your starting point:

* Follow `Step 4 — Write the Code <https://yagsl.yassrobotics.com/get-started/04-write-the-code>`_.
* Official reference repository: `YAGSL-Example on GitHub <https://github.com/Yet-Another-Software-Suite/YAGSL-Example.git>`_.

.. tip::

   Build your code after adding the swerve subsystem and drive commands. If it does not compile, inspect the compiler output and fix missing imports or config path issues before moving on to simulation.

2. Test in the WPILib Simulator & AdvantageScope
------------------------------------------------

Simulating your swerve drive lets you catch inverted axes, bad configs, and command binding issues safely on your laptop:

1. Follow `Step 5 — Test the Code <https://yagsl.yassrobotics.com/get-started/05-test-the-code>`_ to start the WPILib Robot Simulator.
2. Open **AdvantageScope** and connect to your running simulator.
3. Switch to the **2D Field** tab in AdvantageScope.
4. Drag and drop the robot pose from the left-hand topic tree (``Mechanisms/swerve/field/Robot``) into the **Poses** section under the **2D Field** tab.
5. Enable Teleop in the Simulator GUI and drive with your controller (or keyboard) to confirm the robot translates and rotates smoothly in the expected directions.

.. admonition:: Software Lab 3 — Swerve Simulation Check

   **Goal**: Confirm your YAGSL configuration drives accurately in simulation.

   1. Launch the WPILib Simulator with your configured YAGSL project.
   2. Display ``Mechanisms/swerve/field/Robot`` on the AdvantageScope 2D Field.
   3. Verify forward, strafe left/right, and counter-clockwise/clockwise rotation all match field-oriented expectations.
   4. Commit and push your working configuration to your team branch on GitHub.
