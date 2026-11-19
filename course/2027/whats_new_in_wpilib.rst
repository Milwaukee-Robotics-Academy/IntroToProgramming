Whats New in WPILib
===================

What Broke and Why
------------------

WPILib 2027 isn't a minor point release—it is a clean-slate architectural refactor targeting Java 25 and Linux/RP2350 real-time execution on Systemcore.

Namespace & Kinematics Semantics:
---------------------------------
* All edu.wpi.first.* packages move to org.wpilib.*.
* Kinematics types are renamed for dimensional accuracy: ChassisSpeeds  ChassisVelocities and SwerveModuleState  SwerveModuleVelocity.
* WPILib constants and enums are standardized to ALL_CAPS (kReverse  REVERSE).

SmartDashboard is replaced
--------------------------
* Starting in WPILib for 2027 (introduced in Alpha 7), SmartDashboard, SendableChooser, and Sendable are replaced by the Telemetry and Tunables APIs. SendableChooser is replaced by Selectable, and both the SmartDashboard application and Shuffleboard are deprecated/removed for 2027
* Read the details `here <./whats_new_telemetry.html>`_.

Constructor-Driven Robot Lifecycle:
-----------------------------------
* robotInit() is deleted. All robot initialization now executes inside the Robot() constructor, aligning WPILib with standard Java object instantiation rules (final fields can now be initialized cleanly without nullable fields or lateinit workarounds).
* "Test" mode is renamed to "Utility" mode (utilityInit(), utilityPeriodic()).
* DriverStation static god-class methods are split into focused classes: MatchState and RobotState.

MotorController API & Removed Abstractions:
-------------------------------------------
* set(double)  setThrottle(double); stopMotor()  disable().
* MotorControllerGroup is removed—follower behavior must be configured at the motor controller firmware/API level (follow()).

Silent Bug Risk: Nanosecond Timestamps:
---------------------------------------
* Systemcore's OS clock exposes nanoseconds rather than microseconds. Raw calls like RobotController.getTime() and getMonotonicTime() now return nanoseconds (10^9 ticks/sec instead of 10^6). Any hardcoded / 1e6 math in custom PID loops or odometry filters will break silently by 3 orders of magnitude. Always use strongly-typed org.wpilib.units.measure.Time (Seconds, Milliseconds).

Code Diff Reference:
--------------------

Code examples of differences between 2026 and 2027 WPILib are shown below.

2026 WPILib

.. code-block:: java

    package frc.robot;
    import edu.wpi.first.wpilibj.TimedRobot;
    import edu.wpi.first.math.kinematics.ChassisSpeeds;

    public class Robot extends TimedRobot {
    private ChassisSpeeds targetSpeeds; // Forced non-final due to robotInit()

    @Override
    public void robotInit() {
        targetSpeeds = new ChassisSpeeds(1.0, 0.0, 0.0);
    }

    @Override
    public void testPeriodic() { /* ... */ }
    }

2027 WPILib

.. code-block:: java

    package frc.robot;
    import org.wpilib.framework.TimedRobot;
    import org.wpilib.math.kinematics.ChassisVelocities;

    public class Robot extends TimedRobot {
        private final ChassisVelocities targetVelocities; // Clean final initialization

        public Robot() {
            this.targetVelocities = new ChassisVelocities(1.0, 0.0, 0.0);
        }

        @Override
        public void utilityPeriodic() { /* Renamed from testPeriodic */ }
    }



Software Lab 1: 
---------------
* Create a 2027-migration branch on your 2026 robot repo and run the WPILib 2027 Project Importer.
* Refactor Robot.java to eliminate robotInit() and make subsystem references private final.
* Run a project-wide regex search for getFPGATimestamp, getTime, and 1e6 / 1000000 to replace raw timestamp arithmetic with Units (Time) objects.
