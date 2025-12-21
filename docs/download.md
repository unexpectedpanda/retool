---
hide:
  - footer
---

# Download and install

Retool is supported on :fontawesome-brands-windows:{:style="margin-left:0.5em; margin-right:0.2em"}
Windows 10+, :simple-ubuntu:{:style="margin-left:0.5em; margin-right:0.2em"} Ubuntu 20+,
and :simple-apple:{:style="margin-left:0.5em; margin-right:0.2em"} macOS 15+.

How you download and install Retool will depend on your level of comfort with code, and
the operating system you use.

=== ":fontawesome-brands-windows: Windows binary (GUI only)"
    If you're a Windows user and want the easiest path, you can get Retool going in a few
    easy steps:

    1.  Download the Windows binary ZIP file:

        {% include 'includes/file_windows.md' %}

        `SHA256: {% include 'includes/sha256_windows.md' %}`

    1.  Extract the ZIP file to a folder of your choosing.

    1.  In that folder, double click `retoolgui.exe`. A Command Prompt window opens, which
        shows the output when Retool is running. Don't close it, as this also closes the
        GUI.

    1.  Click **File > Update clone lists** to download the latest clone lists and
        metadata files.

        !!! warning "SSL: CERTIFICATE_VERIFY_FAILED error"

            If you see the error
            `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate`
            when trying to download files in Retool, see
            [Troubleshooting](troubleshooting.md#windows) for the fix.

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
            python3 -m pip install alive-progress darkdetect lxml psutil pyside6 strictyaml validators
            ```

        === "Hatch"

            1.  Install Hatch if you haven't already:

                ```
                python3 -m pip install hatch
                ```

            1.  Enter the Hatch virtual environment:

                ```
                hatch shell
                ```

                To exit the environment at any time, run the `exit` command.

    1.  Download the latest clone lists and metadata files:

        ```
        python3 retool.py --update
        ```

        !!! warning "SSL: CERTIFICATE_VERIFY_FAILED error"

            If you see the error
            `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate`
            on macOS when trying to download files in Retool, see
            [Troubleshooting](troubleshooting.md#macos) for the fix.

    1.  You can now run `retool.py` or `retoolgui.py`.
