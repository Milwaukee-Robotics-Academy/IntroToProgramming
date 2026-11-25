IntroToProgramming — 2027 FRC WPILib & YAGSL Curriculum
=======================================================

This is the active development repository for Milwaukee Robotics Academy's FRC 2027 programming documentation, published on Read the Docs:

https://introduction-to-programming.readthedocs.io/en/latest/

Building Locally
----------------

Install the Sphinx dependencies and build the HTML site:

.. code-block:: bash

   pip install -r requirements.txt
   sphinx-build -W -b html . _build/html

Passing ``-W`` treats warnings as errors (matching Read the Docs' ``fail_on_warning: true`` setting) so broken links, missing ``toctree`` entries, and reStructuredText syntax errors are caught before pushing.

Directory Structure
-------------------

* ``index.rst`` — Landing page and top-level navigation.
* ``course/getting_started/`` — Environment setup, GitHub onboarding, and Git/VS Code workflow.
* ``course/wpilib_2027/`` — WPILib 2027 / Systemcore breaking changes, Telemetry & Tunables API, and 2026 code migration.
* ``course/swerve_yagsl/`` — YAGSL swerve setup, configuration, simulation in AdvantageScope, and odometry.
* ``course/testing/`` — Safety checklist and robot bench-testing workflow.
* ``course/about/`` — About FIRST, Milwaukee Robotics Academy, and FRC help resources. 

Authoring Style Guide
---------------------

* **Headings**: Ensure the underline matches (or exceeds) the exact character length of the heading:

  * Page title: ``=``
  * Section heading: ``-``
  * Subsection heading: ``~``

  .. figure:: headings.jpg
     :width: 600

     Heading level conventions.

* **Inline code & paths**: Always wrap inline code and paths in **double backticks** (e.g., ``src/main/deploy``) rather than single backticks, because single backticks render as italics in reStructuredText.
* **Code blocks**: Leave a blank line after ``.. code-block:: <lang>`` and indent the code consistently:

  .. code-block:: java

     Telemetry.publish("Shooter/CurrentRPM", currentRpm);

* **Internal cross-references**: Use Sphinx's ``:doc:`` role instead of hardcoded ``.html`` links:

  .. code-block:: rst

     :doc:`/course/wpilib_2027/telemetry_tunables`
* **Lists**: Leave a blank line before and after every bulleted or numbered list.
* **Videos**: Use the ``sphinxcontrib.youtube`` directive instead of raw HTML ``<iframe>`` tags:

  .. code-block:: rst

     .. youtube:: Jd29kzjclV0

* **Tabs**: Use ``sphinx_design`` tab sets for side-by-side comparisons (e.g., 2026 vs. 2027 APIs):

  .. code-block:: rst

     .. tab-set::

        .. tab-item:: 2027 WPILib

           .. code-block:: java

              Telemetry.publish("Odometry/X", x);

        .. tab-item:: 2026 WPILib (Legacy)

           .. code-block:: java

              SmartDashboard.putNumber("Odometry/X", x);

* **Versioning**: Keep one canonical filename per topic on ``main`` instead of creating ``_2026`` / ``_2027`` file copies. Use Git branches or tags with Read the Docs versioning for prior seasons.
