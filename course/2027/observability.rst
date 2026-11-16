Observability — Telemetry, Tunables & Logging
============================================

The Death of SmartDashboard
----------------------------
WPILib 2027 removes SmartDashboard, Sendable, SendableChooser, and NetworkTables v3. Observability is now split into two explicit, uni-directional design patterns:
Telemetry (Write-Only Outbound Data): Used for logging robot state, poses, velocities, and subsystem health to AdvantageScope/dashboards. It enforces structured typing without the reflection overhead of Sendable.
Tunables & Selectable (Bidirectional Dashboard Controls): Any value meant to be edited from a dashboard (PID gains, auto routines, setpoints) must be explicitly declared as a Tunable or Selectable<T>. This prevents accidental dashboard writes from corrupting read-only telemetry topics.
DriverStationDisplay (ANSI Console): Built-in terminal output stream on the 2027 Driver Station supporting ANSI color codes for immediate state/error reporting during match startup.
Code Pattern: Publishing & Tuning


.. code-block:: Java
    Java
    import org.wpilib.telemetry.Telemetry;
    import org.wpilib.tunables.TunableDouble;
    import org.wpilib.tunables.Selectable;

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


Software Lab 2: Telemetry Refactor
Strip all SmartDashboard and Sendable imports from one subsystem and RobotContainer.
Migrate all outbound sensor/state reads to Telemetry.publish(...) and convert dashboard-editable PID constants and auto choosers to TunableDouble and Selectable.


