---
hide:
  - footer
---

# Download and install

Retool is supported on :simple-windows:{:style="margin-left:0.5em; margin-right:0.2em"}
Windows 10+, :simple-ubuntu:{:style="margin-left:0.5em; margin-right:0.2em"} Ubuntu 20+,
and :simple-apple:{:style="margin-left:0.5em; margin-right:0.2em"} macOS 10+.

How you download and install Retool will depend on your level of comfort with code, and
the operating system you use.

=== ":simple-windows: Windows binary (GUI only)"
    If you're a Windows user and want the easiest path, you can get Retool going in a few
    easy steps:

    1.  Download the Windows binary ZIP file:

        {% include 'includes/file.md' %}

        `SHA256: {% include 'includes/sha256.md' %}`

    1.  Extract the ZIP file to a folder of your choosing.

    1.  In that folder, double click `retoolgui.exe`. A Command Prompt window opens, which
        shows the output when Retool is running. Don't close it, as this also closes the
        GUI.
    1.  Click **File > Update clone lists** to download the latest clone lists and
        metadata files.

    !!! note
        Retool's binary is [UPX packed](https://upx.github.io/) to reduce its size on
        disk. This means that some over-zealous anti-virus software might pick it up as a
        false positive. If the SHA256 of the downloaded ZIP matches the checksum on this
        page, you're likely safe to mark an exception in your anti-virus software.

=== ":simple-python::simple-ubuntu::simple-apple: Git and Python (GUI and CLI)"
    If you're more comfortable with the command line, or are running on a non-Windows
    platform, then this option is for you.

    1.  Download and install [Python 3.10 or higher](https://www.python.org/), if you
        haven't already.

    1.  Clone Retool from its repository:

        ```
        git clone https://github.com/unexpectedpanda/retool.git
        ```

    1.  Install Retool's dependencies, either with Pip or [Hatch](https://hatch.pypa.io/):

        === "Pip"
            ```
            pip install .
            ```

        === "Hatch"

            1.  Install Hatch if you haven't already:

                ```
                pip install hatch
                ```

            1.  Enter the Hatch virtual environment:

                ```
                hatch shell
                ```

                To exit the environment at any time, run the `exit` command.

        !!! info
            On systems that have both Python 2 and 3 installed, you might need to run
            `pip3` instead of `pip`.

    1.  Download the latest clone lists and metadata files:

        ```
        retool --update
        ```

        !!! info
            On some operating systems you might need to prefix Python files with `python3`
            or `python` to run them.

    1.  You can now run `retool` or `retoolgui`.

    **Linux issues**

    If you get a libxcb error in Linux when launching `retoolgui`, this fixed
    the problem for me in Ubuntu 20.04:

    ```
    sudo apt-get install libxcb-randr0-dev \
            libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xkb-dev
    ```
