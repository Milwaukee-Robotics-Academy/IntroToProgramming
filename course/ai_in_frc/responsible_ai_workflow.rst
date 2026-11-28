Responsible AI Workflow in FRC
==============================

The Golden Rule
---------------

.. warning::

   **Never fully trust AI-generated code.** Treat AI as an overconfident assistant, never as the lead programmer. Every single line of code that enters your repository—and every command that runs on a 120-pound competition robot—is **your responsibility**.

Why AI Struggles with FRC 2027 Code
-----------------------------------

Even strong coding models make predictable mistakes in FRC software development:

* **Outdated training data**: Most public FRC code online was written for 2020–2026 WPILib. AI tools routinely output deprecated ``edu.wpi.first.*`` imports, ``SmartDashboard.putNumber(...)``, ``SendableChooser``, ``robotInit()``, ``ChassisSpeeds``, ``set(double)``, or ``MotorControllerGroup``—all of which break in WPILib 2027.
* **Silent runtime bugs**: AI often writes raw timestamp math like ``/ 1e6`` (assuming microseconds instead of Systemcore's nanoseconds), mixes up degrees and radians, or uses wrong gear ratios and sign conventions. These bugs can compile cleanly and only fail when the robot moves.
* **Zero awareness of your physical hardware**: AI cannot see your wiring, CAN IDs, mechanical hard stops, bevel gear orientations, or weight distribution. Untested AI code can slam an arm into a hard stop or drive a swerve robot into a wall.
* **Competition pit reality**: At FRC events, pit Wi-Fi is restricted and field networks have no internet access. If you copy-pasted code you do not fully understand, you will not be able to debug it in 5 minutes between qualification matches.

Good Uses vs. Bad Uses of AI
----------------------------

Use AI to **accelerate your understanding**, not to replace it:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Good Uses (Recommended)
     - Bad Uses (Avoid)
   * - Asking AI to explain an unfamiliar Java compiler error or stack trace.
     - Blindly copy-pasting entire subsystems or commands without reading every line.
   * - Brainstorming state-machine transitions, edge cases, or command structures before coding.
     - Trusting AI to pick PID gains, current limits, or mechanical soft limits for your robot.
   * - Generating JUnit unit tests to verify your math or state logic.
     - Accepting deprecated 2026 WPILib APIs without checking the 2027 documentation.
   * - Asking AI to review code *you* wrote for null checks, edge cases, or readability.
     - Deploying AI-generated code directly to a robot on the floor without simulation and bench testing.
   * - Asking *"Why does this work?"* or *"Walk me through this line by line."*
     - Committing code you could not explain to a teammate, mentor, or FRC judge.

How to Prompt Effectively for WPILib 2027
-----------------------------------------

When you do use an AI assistant, narrow its scope and ground it in real 2027 context:

1. **Specify the exact platform and version**: State explicitly that you are targeting **Java 25**, **WPILib 2027 on Systemcore** (``org.wpilib.*``, ``Telemetry``/``Tunables``, constructor initialization, typed ``Time`` units), and **YAGSL**.
2. **Provide authoritative context**: Paste the relevant snippet from your codebase or the official WPILib 2027 / YAGSL documentation rather than asking AI to guess method signatures from memory.
3. **Ask for small, focused pieces**: Request a single helper method or explanation instead of asking AI to architect an entire robot in one prompt.
4. **Ask for trade-offs and failure modes**: Follow up with *"What edge cases, unit mismatches, or safety risks could break this on a real robot?"*

Ownership & Team Integrity
--------------------------

FIRST Robotics is about building students' engineering skills. Before opening a pull request or asking a mentor to test your branch on the robot, make sure you—and your teammates—genuinely understand how the code works and why each design choice was made.
