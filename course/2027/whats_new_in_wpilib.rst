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
