# AdGence 

## Google Cloud Video Intelligence API Sample

.. _Google Cloud Video Intelligence API: https://cloud.google.com/video-intelligence/docs 

Setup
-------------------------------------------------------------------------------


Authentication
++++++++++++++

Authentication is typically done through `Application Default Credentials`_,
which means you do not have to change the code to authenticate as long as
your environment has credentials. You have a few options for setting up
authentication:

#. When running locally, use the `Google Cloud SDK`_

    .. code-block:: bash

        gcloud auth application-default login


#. When running on App Engine or Compute Engine, credentials are already
   set-up. However, you may need to configure your Compute Engine instance
   with `additional scopes`_.

#. You can create a `Service Account key file`_. This file can be used to
   authenticate to Google Cloud Platform services from any environment. To use
   the file, set the ``GOOGLE_APPLICATION_CREDENTIALS`` environment variable to
   the path to the key file, for example:

    .. code-block:: bash

        export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account.json

.. _Application Default Credentials: https://cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow
.. _additional scopes: https://cloud.google.com/compute/docs/authentication#using
.. _Service Account key file: https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount


Samples
-------------------------------------------------------------------------------

labels
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



To run this sample:

.. code-block:: bash

    $ python labels.py

    usage: labels.py [-h] path
    
    This application demonstrates how to perform basic operations with the
    Google Cloud Video Intelligence API.
    
    For more information, check out the documentation at
    https://cloud.google.com/videointelligence/docs.
    
    Usage Example:
    
        python labels.py gs://cloud-ml-sandbox/video/chicago.mp4
    
    positional arguments:
      path        GCS file path for label detection.
    
    optional arguments:
      -h, --help  show this help message and exit