# README

## Setting up development environment

Once you nix installed, run the following commands sequentially inside this project directory

```shell
nix-build
nix-shell
```

## Information About Fedora Installer

This installer has the following features:

- **Automatic Reboot & Resume**: When run without flags (for a full installation), the script now automatically reboots the system after installing core packages and drivers—a step often necessary for kernel modules to load correctly.
- **State Management**: The script saves its progress to a state file (`/var/tmp/fedora_installer.state`) before rebooting. Upon restart, it reads this file to seamlessly continue from where it left off, skipping already completed tasks.
- **Systemd Resume Service**: A temporary `systemd` service is dynamically created to relaunch the installer automatically after the reboot. This service cleans itself up once the entire process is finished, leaving the system in a pristine state.
- **User-Initiated vs. Automatic Flow**: The new reboot logic is **only** active during a full, no-flag installation. If you run the script with any specific task flags (e.g., `--install-packages`), it will perform only that task and exit as before, preserving its modularity for testing and debugging.
- **Enhanced `--dry-run`**: The dry run mode now simulates the entire reboot-and-resume process, showing you when a reboot would be triggered and how the resume service would be configured, all without making any changes.

Here is the complete, final version of the Python application with the new automated resume functionality.

### How to Use the Flag-Based Application

The usage is now simpler for a full installation.

1.  **Prerequisites**: Ensure `python3.13` and `git` are available.

    ```bash
    sudo dnf install -y python3 git
    ```

2.  **Download**: Create a `fedora_installer` directory and save all the Python files listed below inside it.

3.  **Run the Script**: From the directory _containing_ the `fedora_installer` package, execute with `sudo`.
    - **Fully Automated Installation (Recommended):**
      This single command will start the process, automatically reboot, and continue until everything is finished.

      ```bash
      sudo python3.13 -m fedora_installer.install
      ```

    - **Verify with a Dry Run (Highly Recommended First Step):**
      Simulate the entire automated process, including the reboot and resume steps.

      ```bash
      sudo python3.13 -m fedora_installer.install --dry-run
      ```

    - **Running Specific Tasks (Manual Mode):**
      All flags still work independently for manual control without automatic reboots.
      ```bash
      # Example: Harden the system and then clean up packages
      sudo python3.13 -m fedora_installer.install --harden-system --cleanup
      ```

---

### Project Structure

A new `resume_manager.py` file has been added to handle the reboot and resume logic.

```
.
└── fedora_installer/
    ├── __init__.py
    ├── config.py
    ├── ui.py
    ├── utils.py
    ├── packages.py
    ├── system_setup.py
    ├── user_setup.py
    ├── source_installer.py
    ├── system_hardening.py
    ├── service_creator.py
    ├── resume_manager.py     # <-- NEW FILE
    ├── engine.py
    └── install.py
```
