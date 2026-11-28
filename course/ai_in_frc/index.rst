Using AI in FRC Software Development
====================================

AI coding assistants can be powerful learning and productivity tools in FRC—helping you understand compiler errors, brainstorm architectures, and write unit tests faster. However, **AI does not know your physical robot, does not reliably know breaking WPILib 2027 APIs, and will confidently generate plausible-looking code that crashes or behaves unsafely on real hardware.**

This module teaches how to use AI tools responsibly while keeping **you** in complete control of your robot's codebase.

Module Objectives
-----------------

By the end of this module, you will be able to:

* Distinguish between high-value uses of AI and high-risk shortcuts that hurt learning and robot reliability.
* Recognize why AI frequently produces outdated or subtly broken WPILib 2027 and YAGSL code.
* Apply a disciplined **line-by-line code review and testing workflow** before committing or deploying any AI-assisted code.
* Audit an AI-generated FRC subsystem snippet to identify API, unit, and safety bugs.

.. toctree::
   :maxdepth: 1

   responsible_ai_workflow
   code_review_checklist
