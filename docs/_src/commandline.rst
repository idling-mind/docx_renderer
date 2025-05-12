.. _command-line:

Running from command line
=========================

You can run the command ``docx-renderer`` from the commandline to convert an
input template into an output presentation.

The following is the syntax of the command.

.. click:: docx_renderer.command_line:main
    :prog: docx-renderer
    :nested: full

Example
-------

.. code-block::

    docx-renderer input_template.docx output_file.docx