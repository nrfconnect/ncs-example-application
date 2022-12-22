# nRF Connect SDK example application
 
<a href="https://nrfconnect.github.io/ncs-example-application">
  <img alt="Documentation" src="https://img.shields.io/badge/documentation-3D578C?logo=sphinx&logoColor=white">
</a>
<a href="https://nrfconnect.github.io/ncs-example-application/doxygen">
  <img alt="API Documentation" src="https://img.shields.io/badge/API-documentation-3D578C?logo=c&logoColor=white">
</a>

This repository contains an nRF Connect SDK example application. The main
purpose of this repository is to serve as a reference on how to structure nRF Connect
SDK based applications. Some of the features demonstrated in this example are:

- Basic [Zephyr application][app_dev] skeleton
- [Zephyr workspace applications][workspace_app]
- [Zephyr modules][modules]
- [West T2 topology][west_t2]
- [Custom boards][board_porting]
- Custom [devicetree bindings][bindings]
- Out-of-tree [drivers][drivers]
- Out-of-tree libraries
- Example CI configuration (using Github Actions)
- Custom [west extension][west_ext]
- Doxygen and Sphinx documentation boilerplate

This repository is versioned together with the [nRF Connect SDK main tree][sdk-nrf]. This
means that every time that nRF Connect SDK is tagged, this repository is tagged as well
with the same version number, and the [manifest](west.yml) entry for `zephyr`
will point to the corresponding nRF Connect SDK tag. For example, the `ncs-example-application`
v2.5.0 will point to nRF Connect SDK v2.5.0. Note that the `main` branch always
points to the development branch of nRF Connect SDK, also `main`.

[app_dev]: https://docs.zephyrproject.org/latest/develop/application/index.html
[workspace_app]: https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-workspace-app
[modules]: https://docs.zephyrproject.org/latest/develop/modules.html
[west_t2]: https://docs.zephyrproject.org/latest/develop/west/workspaces.html#west-t2
[board_porting]: https://docs.zephyrproject.org/latest/guides/porting/board_porting.html
[bindings]: https://docs.zephyrproject.org/latest/guides/dts/bindings.html
[drivers]: https://docs.zephyrproject.org/latest/reference/drivers/index.html
[sdk-nrf]: https://github.com/nrfconnect/sdk-nrf
[west_ext]: https://docs.zephyrproject.org/latest/develop/west/extensions.html

## Getting started

Before getting started, make sure you have a proper nRF Connect SDK development environment.
Follow the official
[Installation guide](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/installation/install_ncs.html).

### Initialization

The first step is to initialize the workspace folder (``my-workspace``) where
the ``example-application`` and all nRF Connect SDK modules will be cloned. Run the following
command:

```shell
# initialize my-workspace for the ncs-example-application (main branch)
west init -m https://github.com/nrfconnect/ncs-example-application --mr main my-workspace
# update nRF Connect SDK modules
cd my-workspace
west update
```

### Building and running

To build the application, run the following command:

```shell
cd example-application
west build -b $BOARD app
```

where `$BOARD` is the target board.

You can use the `custom_plank` board found in this repository. Note that you can use
Zephyr and nRF Connect SDK sample boards if an appropriate overlay is provided (see `app/boards`).

A sample debug configuration is also provided. To apply it, run the following
command:

```shell
west build -b $BOARD app -- -DOVERLAY_CONFIG=debug.conf
```

Once you have built the application, run the following command to flash it:

```shell
west flash
```

### Testing

To execute Twister integration tests, run the following command:

```shell
west twister -T tests --integration
```

### Documentation

A minimal documentation setup is provided for Doxygen and Sphinx. To build the
documentation first change to the ``doc`` folder:

```shell
cd doc
```

Before continueing, check if you have Doxygen installed. It is recommended to
use the same Doxygen version used in [CI](.github/workflows/docs.yml). To
install Sphinx, make sure you have a Python installation in place and run:

```shell
pip install -r requirements.txt
```

API documentation (Doxygen) can be built using the following command:

```shell
doxygen
```

The output will be stored in the ``_build_doxygen`` folder. Similarly, the
Sphinx documentation (HTML) can be built using the following command:

```shell
make html
```

The output will be stored in the ``_build_sphinx`` folder. You may check for
other output formats other than HTML by running ``make help``.
