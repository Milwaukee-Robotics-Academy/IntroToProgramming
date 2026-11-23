Bench Testing Checklist
=======================

Never run untested code on a robot sitting on the floor. Always perform initial bring-up on blocks with clear E-stop access and live telemetry running.

Safety First
------------

.. warning::

   * Place the robot securely **on blocks** so all wheels spin freely off the ground.
   * Wear **safety glasses** whenever the robot is powered.
   * Keep one person focused on the **Driver Station disable / E-stop** (Spacebar) at all times.
   * Announce **"Enabling!"** clearly before enabling the robot.

1. Pre-Enable Checks (Disabled)
-------------------------------

With the robot powered on and connected to the Driver Station, remain **Disabled** and verify:

* **CAN Bus Health**: Confirm all drive motors, angle motors, absolute encoders, and the Pigeon 2 gyro appear on the CAN bus with expected IDs and zero firmware/config faults.
* **Absolute Encoders**: Manually rotate each swerve wheel and verify the angle telemetry updates smoothly in AdvantageScope without wrapping glitches.
* **Gyro Heading**: Rotate the robot (or test board) counter-clockwise and confirm the Pigeon 2 heading increases positively (CCW-positive convention).

2. Utility Mode Bring-Up
------------------------

WPILib 2027 renames Test mode to **Utility mode** (``utilityInit()`` / ``utilityPeriodic()``). Use Utility mode or low-throttle Teleop commands to validate one axis at a time:

1. **Zero & Align Modules**: Verify every swerve module points straight forward (bevel gears oriented consistently) when commanded to 0 degrees.
2. **Drive Direction**: Gently push the forward stick and confirm all four wheels spin forward in unison.
3. **Steer Direction**: Gently command rotation and verify all four modules angle tangentially to rotate the chassis counter-clockwise.
4. **Telemetry & Tunables**: Confirm outbound ``Telemetry`` topics and ``TunableDouble`` PID adjustments respond in AdvantageScope.

3. Floor Test Readiness
-----------------------

Only move the robot off blocks onto the floor once:

* All four modules drive and steer in the correct directions with no oscillation.
* Field-oriented driving tracks properly when the robot is rotated by hand.
* Odometry X, Y, and heading values in AdvantageScope match physical movement.
* Your verified code is committed and pushed to your team's GitHub branch.
