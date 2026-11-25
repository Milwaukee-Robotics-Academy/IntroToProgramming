WPILib 2027 & Systemcore
========================

WPILib 2027 is a major architectural release built for Java 25 and the new Systemcore real-time platform. This module explains what changed from 2026, how to replace legacy SmartDashboard code with the new Telemetry and Tunables APIs, and how to migrate your team's 2026 robot code.

Module Objectives
-----------------

By the end of this module, you will be able to:

* Identify the breaking API changes between WPILib 2026 and WPILib 2027.
* Refactor ``Robot.java`` to use constructor-driven initialization and typed ``Time`` units.
* Replace ``SmartDashboard``, ``Sendable``, and ``SendableChooser`` with ``Telemetry``, ``TunableDouble``, and ``Selectable``.
* Clone and begin migrating a 2026 robot project to 2027.

.. toctree::
   :maxdepth: 1

   whats_new
   telemetry_tunables
   migrating_2026_code
