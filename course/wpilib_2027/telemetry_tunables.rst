Observability: Telemetry, Tunables & Logging
============================================

Starting in WPILib 2027 (introduced in Alpha 7), ``SmartDashboard``, ``Sendable``, ``SendableChooser``, and NetworkTables v3 are removed, along with the legacy SmartDashboard and Shuffleboard desktop applications.

The New Architecture
--------------------

Observability in WPILib 2027 is split into explicit, uni-directional design patterns to prevent accidental dashboard edits from corrupting read-only sensor telemetry:

* **Telemetry (Write-Only Outbound Data)**: Used for logging robot state, poses, velocities, and subsystem health to dashboards or log files. Enforces structured typing without the reflection overhead of ``Sendable``.

  * ``Telemetry`` — Static convenience facade for simple logging.
  * ``TelemetryTable`` — Hierarchical namespace for grouping related telemetry values.
  * ``TelemetryLoggable`` — Interface for complex objects that publish themselves into a table.
  * ``TelemetryEntry`` — Backend-facing sink for individual values.

* **Tunables & Selectable (Bidirectional Dashboard Controls)**: Any value meant to be edited from a dashboard (PID gains, auto routines, setpoints) must be explicitly declared as a ``Tunable`` (such as ``TunableDouble``) or ``Selectable<T>`` (replacing ``SendableChooser``).
* **DriverStationDisplay (ANSI Console)**: Built-in terminal output stream on the 2027 Driver Station supporting ANSI color codes for immediate state and error reporting during match startup.
* **Modern Dashboards**: Use **AdvantageScope**, **Glass**, or **Elastic** instead of SmartDashboard or Shuffleboard.

Code Pattern: Publishing & Tuning
---------------------------------

.. code-block:: java

   import org.wpilib.telemetry.Telemetry;
   import org.wpilib.tunables.Selectable;
   import org.wpilib.tunables.TunableDouble;

   public class FlywheelController {
       // Explicitly tunable from dashboard (read/write)
       private final TunableDouble kP = new TunableDouble("Shooter/kP", 0.05);
       private final Selectable<String> modeSelector = new Selectable<>("Shooter/Mode");

       public FlywheelController() {
           modeSelector.addOption("Speaker", "SPEAKER");
           modeSelector.addOption("Pass", "PASS");
           modeSelector.setDefault("SPEAKER");
           Telemetry.publish("Shooter/ModeSelector", modeSelector);
       }

       public void periodic(double currentRpm) {
           // Read-only outbound telemetry
           Telemetry.publish("Shooter/CurrentRPM", currentRpm);

           if (kP.hasChanged()) {
               updatePidGains(kP.get());
           }
       }
   }

.. admonition:: Software Lab 2 — Telemetry Refactor

   **Goal**: Remove all legacy SmartDashboard dependencies from a subsystem and ``RobotContainer``.

   1. Strip all ``SmartDashboard``, ``Sendable``, and ``SendableChooser`` imports from one subsystem and ``RobotContainer``.
   2. Migrate all outbound sensor and state reads to ``Telemetry.publish(...)``.
   3. Convert dashboard-editable PID constants to ``TunableDouble`` and autonomous choosers to ``Selectable<T>``.
   4. Run the robot in simulation and verify your topics appear cleanly in AdvantageScope.

References
----------

* `WPILib 2027 Yearly Changelog <https://docs.wpilib.org/en/2027/docs/yearly-overview/yearly-changelog.html>`_
* `Chief Delphi — Telemetry & Tunable API Discussion <https://www.chiefdelphi.com/t/telemetry-tunable-api/523577>`_
* `WPILib Dashboard Overview <https://docs.wpilib.org/en/stable/docs/software/dashboards/dashboard-intro.html>`_
* `Legacy SmartDashboard Documentation (for migration reference) <https://docs.wpilib.org/en/stable/docs/software/dashboards/smartdashboard/index.html>`_
