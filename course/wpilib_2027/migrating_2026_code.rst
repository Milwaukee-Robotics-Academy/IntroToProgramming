Migrating 2026 Robot Code
=========================

Use this guide to pull down last season's 2026 robot code and prepare a clean branch for migrating to WPILib 2027.

1. Clone the 2026 Repository
----------------------------

Clone the MRA 2026 repository into VS Code:

* Repository URL: `https://github.com/Milwaukee-Robotics-Academy/2026 <https://github.com/Milwaukee-Robotics-Academy/2026>`_

.. tip::

   In VS Code, open **View** -> **Command Palette** (``Ctrl + Shift + P``), select ``Git: Clone``, paste the URL above, and choose a destination folder. You can also run ``git clone https://github.com/Milwaukee-Robotics-Academy/2026.git`` in the terminal.

2. Select Your Team's Branch
----------------------------

Switch to your team's branch before creating your migration branch:

1. Click the branch name in the bottom-left corner of VS Code.
2. Select your team or personal branch from the list so you do not modify ``main``.

.. tip::

   From the terminal, run ``git checkout <your-team-number>`` to switch to your branch.

3. Create a Migration Branch & Build
------------------------------------

Create a dedicated branch for your 2027 changes so you always have a clean 2026 baseline to compare against:

.. code-block:: bash

   git checkout -b 2027-migration

Now work through the breaking changes in :doc:`whats_new` (Software Lab 1) and :doc:`telemetry_tunables` (Software Lab 2), running a build after each milestone to catch compiler errors early.

.. tip::

   If your project fails to compile after importing, read the first error in the Problems/Terminal panel—package renames (``edu.wpi.first.*`` -> ``org.wpilib.*``) and removed methods (``robotInit()``, ``SmartDashboard``) account for the majority of initial errors. Ask an instructor or mentor if you get stuck.
