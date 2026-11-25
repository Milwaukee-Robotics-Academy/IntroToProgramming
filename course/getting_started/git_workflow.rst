Git Workflow in VS Code
=======================

This page covers the core Git tasks you will use throughout the 2027 workshop: creating a new repository, cloning an existing repository, and working on your team's branch.

Creating a New Repository
-------------------------

When starting a brand-new 2027 project:

1. Go to `Create a New Repository on GitHub <https://github.com/new>`_.
2. Enter a repository name (for example, ``2027-alpha``) and an optional description.
3. Select **Public** so instructors, mentors, and teammates can review and share code.
4. Click **Create repository**. Leave the setup instructions page open if you plan to connect a local project next.

Cloning an Existing Repository
------------------------------

To work with an existing codebase (such as last season's 2026 repository):

1. Open WPILib VS Code.
2. Open the Command Palette with ``Ctrl + Shift + P`` (macOS: ``Cmd + Shift + P``) or **View** -> **Command Palette**.
3. Type and select ``Git: Clone``.
4. Paste the repository URL (for example, ``https://github.com/Milwaukee-Robotics-Academy/2026.git``) and choose a local folder.

Alternatively, you can clone from the integrated terminal:

.. code-block:: bash

   git clone https://github.com/Milwaukee-Robotics-Academy/2026.git

Selecting Your Branch
---------------------

Always work on your assigned team or personal branch rather than committing directly to ``main``:

1. Click the current branch name in the **bottom-left corner** of VS Code.
2. Choose your team or personal branch from the list.

You can also switch branches from the terminal:

.. code-block:: bash

   git checkout <your-team-number>

To create a new branch for a lab or feature (such as the 2027 migration lab):

.. code-block:: bash

   git checkout -b 2027-migration
