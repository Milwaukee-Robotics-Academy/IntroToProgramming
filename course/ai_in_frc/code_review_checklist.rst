Reviewing & Testing AI-Generated Code
=====================================

Any time you use AI to help draft, refactor, or debug robot code, treat the output as an **untrusted pull request from a stranger**. Never accept a diff until you have reviewed every single line and verified it in simulation and on blocks.

Line-by-Line Code Review Checklist
----------------------------------

Walk through every checklist item before committing AI-assisted code to Git:

1. **Line-by-Line Comprehension**

   * Read every import, variable, condition, and method call from top to bottom.
   * If you cannot explain what a line does and *why* it is needed to a teammate or mentor, **delete it or research it until you can**.
   * Remove unnecessary boilerplate, unused imports, and overly complex abstractions AI loves to invent.

2. **WPILib 2027 & YAGSL API Accuracy**

   * Verify packages use ``org.wpilib.*`` (not legacy ``edu.wpi.first.*``).
   * Confirm initialization happens in the ``Robot()`` constructor (no ``robotInit()``) and test routines use ``utilityInit()`` / ``utilityPeriodic()``.
   * Confirm outbound data uses ``Telemetry`` / ``TelemetryTable`` and editable values use ``TunableDouble`` / ``Selectable<T>`` (no ``SmartDashboard`` or ``SendableChooser``).
   * Verify motor methods use ``setThrottle(double)`` and ``disable()`` (not ``set()`` / ``stopMotor()`` / ``MotorControllerGroup``).
   * Check for hidden timestamp bugs: ensure no raw ``/ 1e6`` or ``1000000`` conversions assume microseconds instead of Systemcore nanoseconds—always use typed ``Time`` units.
   * Cross-check any unfamiliar method signature against the official `WPILib Documentation <https://docs.wpilib.org/>`_ or `YAGSL Documentation <https://yagsl.yassrobotics.com/>`_.

3. **Units, Signs & Coordinate Conventions**

   * Verify every constant's units: **meters** vs. inches/feet, **radians** vs. degrees/rotations, **seconds** vs. milliseconds/nanoseconds.
   * Check sign conventions: positive throttle moves in the expected direction, gyro rotation is counter-clockwise positive, and field poses use the WPILib blue-alliance origin.

4. **Physical Robot Safety**

   * Verify motor current limits and mechanical soft limits are enforced where required.
   * Confirm there are **no blocking loops** (``while`` loops waiting on sensors) or ``Thread.sleep(...)`` calls inside ``periodic()`` methods—these freeze the entire robot loop.
   * Confirm the subsystem fails safely when disabled or when a sensor disconnects (for example, stopping motors instead of commanding full power on a ``null`` or ``0.0`` reading).

5. **Test Before Merging or Driving**

   * **Compile cleanly**: Run ``WPILib: Build Robot Code`` with zero errors and inspect warnings.
   * **Simulate first**: Run the WPILib Simulator and verify behavior, poses, and telemetry in **AdvantageScope** (see :doc:`/course/telemetry_logging/advantagescope_field`).
   * **Bench test on blocks**: Follow the full :doc:`/course/testing/bench_testing` safety checklist before ever placing the robot on the floor.
   * **Peer review**: Have a teammate or mentor review your pull request on GitHub before merging into ``main``.

.. admonition:: Software Lab 5 — AI Code Audit Challenge

   **Goal**: Practice reviewing AI-generated code line by line to catch outdated WPILib APIs, silent unit/timestamp bugs, and robot safety hazards.

   Suppose an AI assistant generated the following ``ElevatorSubsystem`` when asked for "a simple FRC elevator subsystem with dashboard tuning." **Do not copy this into your robot!** Audit every single line:

   .. code-block:: java

      import edu.wpi.first.wpilibj.RobotController;
      import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
      import edu.wpi.first.wpilibj2.command.SubsystemBase;

      public class ElevatorSubsystem extends SubsystemBase {
          private final SparkMax motor = new SparkMax(12, MotorType.kBrushless);
          private double lastTimeSec = 0;

          public void moveToHeightInches(double targetInches) {
              while (Math.abs(getHeightMeters() - targetInches) > 0.05) {
                  double kP = SmartDashboard.getNumber("Elevator/kP", 0.5);
                  double nowSec = RobotController.getTime() / 1e6;
                  double dt = nowSec - lastTimeSec;
                  lastTimeSec = nowSec;
                  double error = targetInches - getHeightMeters();
                  motor.set(error * kP);
              }
              motor.stopMotor();
          }

          public double getHeightMeters() {
              return motor.getEncoder().getPosition();
          }
      }

   **Audit Tasks**:

   1. List **every bug and hazard** you find in the snippet above (hint: there are at least **7 distinct issues** across WPILib 2027 APIs, Systemcore timestamps, units, control-loop safety, and mechanical safety).
   2. Compare your findings with a teammate or mentor—make sure you caught:

      * Deprecated ``edu.wpi.first.*`` imports and ``SmartDashboard`` usage instead of ``org.wpilib.*`` and ``TunableDouble`` / ``Telemetry``.
      * Deprecated ``motor.set(...)`` and ``motor.stopMotor()`` instead of 2027 APIs (``setThrottle(...)`` / ``disable()``).
      * Silent Systemcore nanosecond timestamp bug: ``RobotController.getTime() / 1e6`` treats nanoseconds as microseconds (off by 1,000x!).
      * Unit mismatch: comparing ``targetInches`` directly against ``getHeightMeters()`` (and returning raw encoder rotations as meters without a conversion factor).
      * Blocking ``while`` loop that freezes the robot scheduler and prevents commands/E-stop logic from cycling normally.
      * Unclamped motor output with no upper/lower soft limits or current limits—risking smashing the elevator into mechanical hard stops.

   3. Rewrite the subsystem cleanly on a practice branch using WPILib 2027 ``Telemetry`` / ``TunableDouble``, proper typed units, non-blocking ``periodic()`` control, and output/height clamping, then verify it builds and runs in simulation.
