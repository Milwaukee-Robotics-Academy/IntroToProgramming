AdvantageScope: Telemetry, Robot Pose & Field Data
==================================================

**AdvantageScope** is our primary tool for viewing live 2027 WPILib telemetry, inspecting recorded ``.wpilog`` files after a run, and visualizing robot poses and field locations in 2D and 3D.

Start by reading the official `AdvantageScope "Hello, Telemetry!" Tutorial <https://docs.advantagescope.org/tutorials/hello-telemetry/>`_, which walks through connecting to live data, opening logs, and building your first telemetry views.

1. Connecting to Live Telemetry or Opening a Log
------------------------------------------------

You can use AdvantageScope in two modes:

* **Live Mode (Bench Testing & Simulation)**:

  1. Start the WPILib Robot Simulator (or connect your laptop to the robot's network).
  2. In AdvantageScope, choose **File** -> **Connect to Simulator** (or **File** -> **Connect to Robot** using your team number / NetworkTables 4).
  3. Expand the topic tree in the left sidebar to browse your published ``Telemetry`` and ``TelemetryTable`` entries in real time.

* **Log Replay Mode (Post-Test & Post-Match Analysis)**:

  1. Download the ``.wpilog`` file recorded by ``DataLogManager`` (or open the log created during simulation).
  2. In AdvantageScope, choose **File** -> **Open Log(s)...** and select the ``.wpilog`` file.
  3. Scrub through the timeline to inspect exactly what happened at any millisecond of the run.

Following the `Hello, Telemetry! Tutorial <https://docs.advantagescope.org/tutorials/hello-telemetry/>`_, start with a **Line Graph** tab to plot numeric signals (for example, desired vs. measured wheel velocity or flywheel RPM) alongside a **Table** or **Statistics** tab for exact values.

2. Publishing Robot Pose & Field Location Data
----------------------------------------------

To display where your robot is on the field—along with target locations, AprilTag vision estimates, or autonomous paths—publish WPILib ``Pose2d`` (or ``Pose3d``) objects from your subsystem's ``periodic()`` method using WPILib 2027's ``Telemetry`` API:

.. code-block:: java

   import org.wpilib.math.geometry.Pose2d;
   import org.wpilib.math.geometry.Rotation2d;
   import org.wpilib.telemetry.Telemetry;

   public class DriveTelemetry {
       // Example static field target location (x = 4.5 m, y = 2.5 m, heading = 0 deg)
       private static final Pose2d SCORING_TARGET =
           new Pose2d(4.5, 2.5, Rotation2d.fromDegrees(0.0));

       public static void publishFieldData(Pose2d odometryPose, Pose2d visionPose) {
           // Current estimated robot pose on the field
           Telemetry.publish("Field/RobotPose", odometryPose);

           // Optional vision pose estimate for comparing against wheel odometry
           Telemetry.publish("Field/VisionPose", visionPose);

           // Field location / target waypoint to overlay on the 2D or 3D field
           Telemetry.publish("Field/ScoringTarget", SCORING_TARGET);
       }
   }

.. note::

   AdvantageScope expects field coordinates in **meters** using the standard WPILib **blue-alliance origin** convention (``+X`` toward the red alliance wall, ``+Y`` toward the left side of the field from the blue driver station, and counter-clockwise positive rotation).

3. Visualizing Poses & Field Locations in AdvantageScope
--------------------------------------------------------

Once your robot or simulator is publishing ``Pose2d`` / ``Pose3d`` topics (or you have opened a ``.wpilog`` file containing them):

1. Click the ``+`` button in AdvantageScope's tab bar to add a **2D Field** tab (for a top-down map) or a **3D Field** tab (for spatial 3D visualization with field elements and AprilTags).
2. In the left sidebar, expand your telemetry namespace (for example, ``Field/`` or ``Mechanisms/swerve/field/``).
3. Drag ``Field/RobotPose`` into the **Poses** section of the field tab to display the robot moving across the field.
4. Drag additional field locations—such as ``Field/VisionPose`` (styled as a ghost robot) or ``Field/ScoringTarget`` (styled as a target marker)—into the **Poses** list to compare your odometry against vision estimates and target field coordinates.
5. Use the field tab settings to select the current FRC game field layout and verify alliance orientation.

.. tip::

   You can also add a **Swerve** tab in AdvantageScope and drag in your desired and measured ``SwerveModuleVelocity[]`` arrays to compare commanded vs. actual wheel angles and speeds alongside the 2D Field view.

.. admonition:: Software Lab 4 — Telemetry Logging & Field Pose Visualization

   **Goal**: Record a full WPILib 2027 ``.wpilog`` session and visualize telemetry, robot pose, and a field target location in AdvantageScope.

   1. Enable ``DataLogManager.start()`` and ``DriverStation.startDataLog(DataLogManager.getLog())`` in ``Robot.java``.
   2. Publish your swerve robot's ``Pose2d`` (``Field/RobotPose``), at least one target field location (``Field/ScoringTarget``), and two numeric subsystem metrics using ``Telemetry.publish(...)`` or ``TelemetryTable``.
   3. Run the WPILib Simulator (or drive on blocks during bench testing) and connect AdvantageScope live, following the `Hello, Telemetry! Tutorial <https://docs.advantagescope.org/tutorials/hello-telemetry/>`_.
   4. Build a layout with:

      * A **Line Graph** tab showing your numeric telemetry signals.
      * A **2D Field** tab displaying both ``Field/RobotPose`` and ``Field/ScoringTarget``.

   5. Stop the simulator, open the generated ``.wpilog`` file in AdvantageScope, and verify that your graphs and 2D field pose replay cleanly.

References
----------

* `AdvantageScope — "Hello, Telemetry!" Tutorial <https://docs.advantagescope.org/tutorials/hello-telemetry/>`_
* `AdvantageScope Documentation Home <https://docs.advantagescope.org/>`_
* `WPILib 2027 Yearly Changelog <https://docs.wpilib.org/en/2027/docs/yearly-overview/yearly-changelog.html>`_
* :doc:`/course/wpilib_2027/telemetry_tunables`
* :doc:`/course/swerve_yagsl/odometry`
