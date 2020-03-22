<!-- Author (Created): Roger "Equah" Hürzeler -->
<!-- Author (Modified): Roger "Equah" Hürzeler -->
<!-- Date (Created): 12020.03.16 HE -->
<!-- Date (Modified): 12020.03.16 HE -->
<!-- License: apache-2.0 -->

**Nuntius [Python 3]**
================================================================================

[Nuntius](https://github.com/TheEquah/Nuntius/) Python 3 implementation.

--------------------------------------------------------------------------------

# Architecture

Overview of the Nuntius architecture.

## Nuntius

Nuntius is a binary data serialization format. The data contains entries, which always start with an [SBLInt](https:github.com/TheEquah/SBLInt) indicating the element type, followed by binary data of the element.

## Interpreter

Nuntius data is interpreted. Elements interpret themselves by e.g. reading the next byte or given amount of bytes. This allows to implement element types containing data of fixed length, in data defined length, character terminated length or data streams.

## Element Type

All elements in Nuntius belong to a type. The element type defines an unique identity and functions how the Nuntius interpreter reads and writes the element. Note, that if an element type is not defined in a Nuntius document, it will become unreadable.

### Identity

The identity of an element can be freely defined, which could also cause conflicts between applications using nuntius. It is important, that identity `0` should not be used.

--------------------------------------------------------------------------------

# Install

Nuntius provedes a [`/src/setup.py`](https://github.com/TheEquah/Nuntius-python3/blob/master/src/setup.py) script to install the package. To use this script, `cd` into the [`/src/`](https://github.com/TheEquah/Nuntius-python3/tree/master/src/) directory, and execute the script with `python3 ./setup.py install`.

## Requirements

Nuntius requires the [SBLInt Python 3](https://github.com/TheEquah/SBLInt-python3/) package to be installed.

--------------------------------------------------------------------------------

# Examples

This repository provides the following examples for Nuntius.

## String

Example which creates, writes and reads a string element type.

Directory: [`/example/string/`](https://github.com/TheEquah/Nuntius-python3/tree/master/example/string/)

--------------------------------------------------------------------------------
