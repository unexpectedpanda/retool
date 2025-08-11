---
hide:
  - footer
---

# Integrating with ROMVault

If you use [ROMVault](https://romvault.com/) or have a subscription to [DATVault](https://www.datvault.com/)
and want to integrate Retool into your flow, complete the following steps.

## Setup


1.  Add your Redump and No-Intro DAT files to a subfolder in your ROMVault `DATRoot`
    that is separate from your other DAT files. For example, `DATRoot\Retool\`.

    This is so Retool only processes these files and no others.

1.  Configure Retool as follows:

    === "Retool GUI"
        1.  Open Retool.

        1.  Click **File**, and then click **Settings**.

        1.  Set the **Quick folder import location** to where DATVault downloads your
            Redump and No-Intro DAT files.

        1.  Close the settings dialog box.

        1.  Optional: In the **Paths** tab, enable **Replace input DAT files**.

        1.  Optional: In the **Options** tab, enable
            **Don't modify the input DAT file's existing header fields**.

        1.  DATVault only: In the **Options** tab, disable
            **Add MIA attributes to files**.

        1.  Set your preferences for the ROMVault DAT files in Retool.

        !!! Note
            If you use system settings, you might also have to change these settings
            there.

    === "Retool CLI"
        Use the following flags, along with the path to the separate folder you've set up
        for Redump and No-Intro DAT files. Add any other settings you want.

        * `--replace`:  Replace input DAT files with Retool versions. Only use this if
          you can recover the original DAT files from elsewhere.

        * `--originalheader`: Optional. Use the original input DAT headers in output DAT
          files.

## Process the DAT files and update ROMVault

After you've got your DAT files where you want them in ROMVault's `DatRoot`:

1.  In Retool, click ![A screenshot of the "add DAT files recursively from your quick import folder" button](images/icons8-add-quick-folder-80.png){:.inline-icon}
    **Add DAT files recursively from your quick import folder** to add
    your ROMVault Redump and No-Intro DAT files.

1.  Click **Process DAT files** to replace the DAT files with those that have been
    processed by Retool.

1.  In ROMVault, click **Update DATs** to load the Retool-processed version of your DAT
    files.
