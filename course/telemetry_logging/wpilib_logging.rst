2027 WPILib Telemetry & Data Logging
====================================

WPILib 2027 removes ``SmartDashboard``, ``Sendable``, and NetworkTables v3 in favor of explicit **outbound telemetry** (``Telemetry``, ``TelemetryTable``, ``TelemetryLoggable``) and **bidirectional dashboard inputs** (``TunableDouble``, ``Selectable<T>``). For the API migration overview, see :doc:`/course/wpilib_2027/telemetry_tunables`.

This page covers how to record full-robot ``.wpilog`` files and structure subsystem telemetry using the 2027 WPILib workflow.

1. Starting On-Robot Data Logging
---------------------------------

Start ``DataLogManager`` inside your ``Robot()`` constructor so every bench test, simulation run, and match is recorded automatically to a ``.wpilog`` file:

.. code-block:: java

   package frc.robot;

   import org.wpilib.framework.TimedRobot;
   import org.wpilib.system.DataLogManager;
   import org.wpilib.driverstation.DriverStation;

   public class Robot extends TimedRobot {
       public Robot() {
           // Starts automatic .wpilog recording (captures NetworkTables & console output)
           DataLogManager.start();

           // Also log Driver Station control state, match metadata, and joystick inputs
           DriverStation.startDataLog(DataLogManager.getLog());
       }
   }

.. tip::

   ``DataLogManager`` automatically manages log filenames (including match numbers when connected to FMS) and prunes the oldest log files if disk space runs low. Always attach a reliable USB drive (or verify Systemcore storage) before competition matches so logs are preserved across reboots.

2. Structuring Telemetry with ``TelemetryTable`` & ``TelemetryLoggable``
------------------------------------------------------------------------

Rather than scattering flat keys across your codebase, group related signals under a hierarchical ``TelemetryTable`` per subsystem, or implement ``TelemetryLoggable`` so each subsystem owns its own telemetry schema:

.. code-block:: java

   import org.wpilib.math.geometry.Pose2d;
   import org.wpilib.math.kinematics.ChassisVelocities;
   import org.wpilib.telemetry.Telemetry;
   import org.wpilib.telemetry.TelemetryLoggable;
   import org.wpilib.telemetry.TelemetryTable;

   public class SwerveTelemetry implements TelemetryLoggable {
       private Pose2d robotPose = new Pose2d();
       private ChassisVelocities measuredVelocities = new ChassisVelocities();
       private double gyroYawDeg = 0.0;

       public void update(Pose2d pose, ChassisVelocities velocities, double yawDeg) {
           this.robotPose = pose;
           this.measuredVelocities = velocities;
           this.gyroYawDeg = yawDeg;
       }

       @Override
       public void logTo(TelemetryTable table) {
           // Structured WPILib types serialize cleanly for AdvantageScope
           table.log("Pose", robotPose);
           table.log("MeasuredVelocities", measuredVelocities);
           table.log("GyroYawDeg", gyroYawDeg);
       }
   }

For quick, one-off outbound values in a subsystem's ``periodic()`` method, you can also use the static ``Telemetry`` facade:

.. code-block:: java

   Telemetry.publish("Battery/Voltage", RobotController.getBatteryVoltage());
   Telemetry.publish("Drive/GyroConnected", gyro.isConnected());

3. Keep Telemetry Separate from Tunables
----------------------------------------

Follow WPILib 2027's strict separation of concerns:

* **Outbound state & sensors (write-only)**: Publish with ``Telemetry.publish(...)`` or ``TelemetryTable``. Dashboards can read and graph these values, but cannot accidentally overwrite them.
* **Editable parameters (bidirectional)**: Declare PID gains, feedforwards, and mode selectors explicitly with ``TunableDouble`` and ``Selectable<T>``.
* **Startup & fault messages**: Use ``DriverStationDisplay`` (ANSI console output) for high-visibility startup health checks and hardware faults.

4. Prefer Structured Types Over Raw Numbers
-------------------------------------------

Whenever you log geometry or drivetrain state, publish WPILib's native structured types—such as ``Pose2d``, ``Pose3d``, ``ChassisVelocities``, and ``SwerveModuleVelocity[]``—rather than only splitting them into separate ``X``, ``Y``, and ``Heading`` doubles.

Structured types:

* Pack cleanly into binary struct entries in NetworkTables 4 and ``.wpilog`` files.
* Are automatically recognized by **AdvantageScope** for 2D/3D field rendering, swerve module visualization, and trajectory overlays.

What to Log on Every Robot
--------------------------

As a baseline checklist for 2027 robots, log at least:

* **Drivetrain**: Estimated ``Pose2d``, vision-estimated ``Pose2d`` (if used), desired vs. measured ``ChassisVelocities``, ``SwerveModuleVelocity[]``, and Pigeon 2 gyro heading.
* **Mechanisms**: Target setpoints vs. measured positions/RPMs, motor currents, limit switches/sensors, and active command names.
* **System Health**: Battery voltage, brownout/CAN fault flags, and Driver Station match/alliance state.
