.. _example_about:

About the Example Application
#############################

.. contents::
   :local:
   :depth: 2

The About page is where more detailed information about the application should be placed.
For this example, it contains information on the documentation structure.

Table of contents
*****************

When a page other than the landing page is long and contains headers, you should also add a table of contents to that page.
To generate the table of contents, add the following after the page title:

.. code-block:: RST

  .. contents::
     :local:
     :depth: 2

.. _example_about_naming:

Naming page files and page links
********************************

When naming the file for a page, use simple and descriptive names.
Keep in mind that the file name will also be visible in the URL.

You should attach a reference target to every every page title as well.
The reference target is used when linking from one page to another.
In most cases, it's good to match the reference target to the page name, as this makes it easier to know which page is linked when the target is used.
For example, the the reference target for this page is ``example_about``, and it is defined with the following line just before the page title:

.. code-block:: RST

   .. _example_about:

If you want to link to a subheading on a page, you should also add a reference target for that heading.
The best practice for naming subheading reference targets is to use the page reference target and add some or all of the heading.
For example, the reference target for this section is ``example_about_naming``, and it is defined in the same way as the page reference target.

When you want to link to a reference target, you can use either of the following:

.. code-block:: RST

   :ref:`example_about`
   :ref:`replaced link text <example_about>`

The first one uses the name of the heading or title that is linked (:ref:`example_about`), while the second one replaces that with a custom link text (:ref:`replaced link text <example_about>`).

External links
==============

For links outside of the documentation set, use the :file:`links.txt` file.
This file makes it easier to update and re-use links.
Define the links according to the existing examples, then use either of the following to place the link in the text:

.. code-block:: RST

   `nRF Connect SDK`_
   `replaced link text <nRF Connect SDK_>`_

The first one uses the name of the link (`nRF Connect SDK`_), while the second one replaces that with a custom link text (`replaced link text <nRF Connect SDK_>`_).

Recommended pages
*****************

In addition to the About page, the following pages are recommended for all applications.

Requirements and setup
   The :ref:`example_setup` details what the user needs to have so they can work with the application.

Release notes
   The release notes page documents changes for each release.
