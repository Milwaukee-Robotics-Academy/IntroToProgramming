No More SmartDashboard
===================

Starting in WPILib for 2027 (introduced in Alpha 7), SmartDashboard, SendableChooser, and Sendable are replaced by the Telemetry and Tunables APIs. SendableChooser is replaced by Selectable, and both the SmartDashboard application and Shuffleboard are deprecated/removed for 2027. 
References:
* `https://docs.wpilib.org/en/2027/docs/yearly-overview/yearly-changelog.html <https://docs.wpilib.org/en/2027/docs/yearly-overview/yearly-changelog.html>`_
* `https://docs.wpilib.org/en/stable/docs/software/dashboards/smartdashboard/index.html <https://docs.wpilib.org/en/stable/docs/software/dashboards/smartdashboard/index.html>`_
* `https://docs.wpilib.org/en/stable/docs/software/dashboards/dashboard-intro.html <https://docs.wpilib.org/en/stable/docs/software/dashboards/dashboard-intro.html>`_

New Telemetry API
------------------

The Telemetry API is an output-only system for publishing robot data to dashboards, debug tools, or log files: 
* Telemetry: Static convenience facade for simple logging.
* TelemetryTable: Hierarchical namespace for grouping related telemetry values.
* TelemetryLoggable: Interface for complex objects that publish themselves into a table.
* TelemetryEntry: Backend-facing sink for individual values. `https://www.chiefdelphi.com/t/telemetry-tunable-api/523577 <https://www.chiefdelphi.com/t/telemetry-tunable-api/523577>`_


Related Changes & Resources

* Tunables API: Handles adjustable values/inputs separately from output-only telemetry.`https://www.chiefdelphi.com/t/telemetry-tunable-api/523577 <https://www.chiefdelphi.com/t/telemetry-tunable-api/523577>`_
* Dashboards: Modern dashboards such as Glass, AdvantageScope, and Elastic are used instead of SmartDashboard or Shuffleboard.
* Official & Community Details: Check the WPILib 2027 Changelog for release notes and the Chief Delphi Telemetry/Tunable API post for technical architecture details. 
    * `https://docs.wpilib.org/en/stable/docs/software/dashboards/dashboard-intro.html <https://docs.wpilib.org/en/stable/docs/software/dashboards/dashboard-intro.html>`_
    * `https://www.chiefdelphi.com/t/telemetry-tunable-api/523577 <https://www.chiefdelphi.com/t/telemetry-tunable-api/523577>`_
    * `https://docs.wpilib.org/en/2027/docs/yearly-overview/yearly-changelog.html <https://docs.wpilib.org/en/2027/docs/yearly-overview/yearly-changelog.html>`_

