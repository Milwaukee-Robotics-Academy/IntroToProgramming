Telemetry & Logging
===================

Once your robot passes basic bench testing, reliable **telemetry** and **on-robot logging** become your most important tools for tuning, diagnosing field issues, and reviewing matches. In WPILib 2027, legacy ``SmartDashboard`` workflows are replaced by the **Telemetry** and **Tunables** APIs paired with ``DataLogManager`` (``.wpilog``) recording and **AdvantageScope** visualization.

Module Objectives
-----------------

By the end of this module, you will be able to:

* Enable automatic on-robot ``.wpilog`` data logging in the WPILib 2027 ``Robot()`` constructor.
* Organize subsystem outputs cleanly using ``Telemetry``, ``TelemetryTable``, and ``TelemetryLoggable``.
* Publish structured robot pose (``Pose2d`` / ``Pose3d``) and field location data for visualization.
* Use **AdvantageScope**—following the `Hello, Telemetry! Tutorial <https://docs.advantagescope.org/tutorials/hello-telemetry/>`_—to inspect live telemetry, replay ``.wpilog`` files, and visualize robot poses and field targets on the 2D and 3D Field tabs.

.. toctree::
   :maxdepth: 1

   wpilib_logging
   advantagescope_field
