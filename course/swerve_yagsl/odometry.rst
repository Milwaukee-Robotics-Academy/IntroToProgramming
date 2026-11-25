Odometry Basics
===============

Understanding odometry is essential for accurate field-oriented driving, autonomous path following, and vision fusion. Odometry estimates the robot's pose — **X position**, **Y position**, and **heading (theta)** — on the field using wheel encoders and the gyro (Pigeon 2).

For the underlying math and WPILib classes, review the official `WPILib Swerve Drive Odometry Guide <https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/swerve-drive-odometry.html>`_.

Publishing Robot Pose to Telemetry
----------------------------------

Publish X, Y, and heading values in your swerve subsystem's ``periodic()`` method so you can inspect them live in AdvantageScope:

.. tab-set::

   .. tab-item:: 2027 WPILib (Telemetry API)

      .. code-block:: java

         import org.wpilib.telemetry.Telemetry;

         // Inside your swerve subsystem's periodic() method:
         Telemetry.publish("Odometry/Swerve/HeadingDeg", getPose().getRotation().getDegrees());
         Telemetry.publish("Odometry/Swerve/X", getPose().getX());
         Telemetry.publish("Odometry/Swerve/Y", getPose().getY());

   .. tab-item:: 2026 WPILib (Legacy SmartDashboard)

      .. code-block:: java

         import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;

         // Legacy 2026 pattern (removed in WPILib 2027):
         SmartDashboard.putNumber("Odometry/Swerve/Heading", getPose().getRotation().getDegrees());
         SmartDashboard.putNumber("Odometry/Swerve/X", getPose().getX());
         SmartDashboard.putNumber("Odometry/Swerve/Y", getPose().getY());

.. tip::

   Build your code and run it in the WPILib Simulator to verify that ``Odometry/Swerve/X``, ``Odometry/Swerve/Y``, and ``Odometry/Swerve/HeadingDeg`` update smoothly in AdvantageScope as you drive.
