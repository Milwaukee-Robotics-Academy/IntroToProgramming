What's New in WPILib 2027
=========================

WPILib 2027 is not a minor point release—it is a clean-slate architectural refactor targeting **Java 25** and **Linux/RP2350 real-time execution on Systemcore**. Understanding what broke and why will save hours during migration.

Namespace & Kinematics Semantics
--------------------------------

* All ``edu.wpi.first.*`` packages move to ``org.wpilib.*``.
* Kinematics types are renamed for dimensional accuracy:

  * ``ChassisSpeeds`` -> ``ChassisVelocities``
  * ``SwerveModuleState`` -> ``SwerveModuleVelocity``

* WPILib constants and enums are standardized to ``ALL_CAPS`` (for example, ``kReverse`` -> ``REVERSE``).

SmartDashboard Is Replaced
--------------------------

Starting in WPILib 2027 (introduced in Alpha 7), ``SmartDashboard``, ``Sendable``, and ``SendableChooser`` are replaced by the **Telemetry** and **Tunables** APIs (with ``Selectable`` replacing ``SendableChooser``). Both the SmartDashboard desktop app and Shuffleboard are removed for 2027.

See :doc:`telemetry_tunables` for full migration details and code patterns.

Constructor-Driven Robot Lifecycle
----------------------------------

* ``robotInit()`` is deleted. All robot initialization now runs inside the ``Robot()`` constructor, aligning WPILib with standard Java object instantiation rules so ``final`` fields can be initialized cleanly without nullable fields.
* **Test** mode is renamed to **Utility** mode (``utilityInit()``, ``utilityPeriodic()``).
* ``DriverStation`` static utility methods are split into focused classes: ``MatchState`` and ``RobotState``.

MotorController API & Removed Abstractions
------------------------------------------

* ``set(double)`` -> ``setThrottle(double)``
* ``stopMotor()`` -> ``disable()``
* ``MotorControllerGroup`` is removed—configure follower behavior directly at the motor controller firmware/API level using ``follow()``.

.. warning::

   **Silent Bug Risk — Nanosecond Timestamps**: Systemcore's OS clock exposes **nanoseconds** rather than microseconds. Raw calls like ``RobotController.getTime()`` and ``getMonotonicTime()`` now return nanoseconds (10^9 ticks/sec instead of 10^6). Any hardcoded ``/ 1e6`` math in custom PID loops or odometry filters will silently break by 3 orders of magnitude. Always use strongly typed ``org.wpilib.units.measure.Time`` (``Seconds``, ``Milliseconds``).

Code Diff Reference: 2026 vs. 2027
----------------------------------

Compare how a minimal ``Robot`` class changes between 2026 and 2027:

.. tab-set::

   .. tab-item:: 2027 WPILib

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
             public void utilityPeriodic() {
                 // Renamed from testPeriodic()
             }
         }

   .. tab-item:: 2026 WPILib (Legacy)

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
             public void testPeriodic() {
                 // Legacy Test mode
             }
         }

.. admonition:: Software Lab 1 — Core 2027 Migration

   **Goal**: Migrate your robot's entry point and eliminate raw timestamp bugs.

   1. Create a ``2027-migration`` branch on your 2026 robot repository (see :doc:`migrating_2026_code`) and run the WPILib 2027 Project Importer.
   2. Refactor ``Robot.java`` to eliminate ``robotInit()`` and make subsystem references ``private final``.
   3. Run a project-wide regex search for ``getFPGATimestamp``, ``getTime``, and ``1e6`` / ``1000000``, replacing raw timestamp arithmetic with ``Time`` unit objects.
   4. Build the project and verify there are no remaining ``edu.wpi.first.*`` imports in ``Robot.java``.
