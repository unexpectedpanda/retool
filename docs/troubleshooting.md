---
hide:
  - footer
---

# Troubleshooting

This document contains solutions for known problems when running Retool on supported
operating systems.

=== ":fontawesome-brands-windows: Windows"

    <h4>SSL: CERTIFICATE_VERIFY_FAILED error</h4>
    If you see the error
    `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate`
    when trying to download files in Retool, it's a
    [shortcoming in the way Python's SSL module is designed](https://github.com/python/cpython/issues/80192#issuecomment-1093815322)
    that prevents it from obtaining the certificates it needs to verify that it can trust
    the secure website it wants to download from.

    The easiest way to work around this is to install OpenSSL and import the Mozilla CA
    certificate store:

    1.  [Download OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) (the light
        version is fine), and then run the installer.

        !!! note
            You might be prompted to download and install a Visual C++ redistributable as
            part of the OpenSSL installation process. Do so. The redistributable downloads
            to your default download directory, and you should install it before
            continuing the OpenSSL installation.

    1.  Complete the OpenSSL install.

    1.  Open Windows PowerShell as an administrator.

    1.  Run the following script to download and import the Mozilla CA certificate store:

        ```ps {.copy}
        cd $env:USERPROFILE;
        Invoke-WebRequest https://curl.se/ca/cacert.pem -OutFile $env:USERPROFILE\cacert.pem;
        $plaintext_pw = 'PASSWORD';
        $secure_pw = ConvertTo-SecureString $plaintext_pw -AsPlainText -Force;
        & 'C:\Program Files\OpenSSL-Win64\bin\openssl.exe' pkcs12 -export -nokeys -out certs.pfx -in cacert.pem -passout pass:$plaintext_pw;
        Import-PfxCertificate -Password $secure_pw  -CertStoreLocation Cert:\LocalMachine\Root -FilePath certs.pfx;
        ```

    Retool should now be able to download the files it needs.

=== ":simple-apple: macOS"

    <h4>SSL: CERTIFICATE_VERIFY_FAILED error</h4>
    If you see the error
    `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate`
    when trying to download files in Retool, it's a
    [shortcoming in the way Python's SSL module is designed](https://github.com/python/cpython/issues/80192#issuecomment-1093815322)
    that prevents it from obtaining the certificates it needs to verify that it can trust
    the secure website it wants to download from.

    To work around this, run the following commands, which download the required
    certificates into your home folder and then add them to your system keychain. Replace
    <span class="variable">PYTHON_VERSION</span> with the major.minor version of your
    Python install. For example, for Python 3.14.0, use `3.14`.

    <pre class="copy"><code>curl -o ~/cacert.pem https://curl.se/ca/cacert.pem
    awk '/-----BEGIN CERTIFICATE-----/{flag=1} flag{print} /-----END CERTIFICATE-----/{exit}' ~/cacert.pem > ~/first-cert.pem
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/first-cert.pem
    open "/Applications/Python\ <span class="variable">PYTHON_VERSION</span>/Install\ Certificates.command"</code></pre>


=== ":simple-ubuntu: Ubuntu"

    <h4>libxcb error</h4>

    If you get a libxcb error in Linux when launching `retoolgui` in Ubuntu, you might need to
    download the following libraries:

    ```sh {.copy}
    sudo apt-get install libxcb-randr0-dev \
            libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xkb-dev
    ```
