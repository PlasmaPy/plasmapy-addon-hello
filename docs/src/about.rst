.. _plasmapy: http://docs.plasmapy.org/en/latest/

About
=====

The :mod:`plasmapy-addon-hello` package is setup to demonstrate how an independent
python distributions can extend the capabilities of
:mod:`plasmapy.formulary`.

Why does plasmapy_ need addon packages?  Why are these extensions not included in
the main plasmapy_ distribution?  PlasmaPy sets out to provide a broad toolkit
to support as many corners of plasma research and eduction as possible.  A result
of this, PlasmaPy focuses on providing the most commonly needed features for the
community.  With that said, we do see the benefit and need for specialized
features like interface related to a certain research lab, analysis routines for
a specific diagnostic, an interface to a simulation code, etc.  These addon packages
allow for these featrues to be independently developed, but still be accessilbe
through plasmapy_.  PlasmaPy we develop some of these addon features, but we hope
the community will also develop addons to make PlasmaPy more powerfull.  This addon
framework also allows for the main plasmapy_ distribution to stay "light-weight" and
allow users to install the extra addon features they would like.