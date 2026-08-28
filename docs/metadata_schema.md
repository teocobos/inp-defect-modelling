# Metadata Schema

## Purpose

This document defines the minimum metadata required to reconstruct and interpret calculations within the InP defect-modelling project.

Metadata may be stored in YAML, JSON or another structured format provided that the schema remains consistent.

## General Metadata

Each calculation should record:

- calculation identifier
- material
- crystal phase
- structure identifier
- calculation type
- date created
- researcher
- Git commit hash
- calculation status

## Material Metadata

Recommended fields:

```yaml
material: InP
material_id: inp
phase: zincblende
space_group: null