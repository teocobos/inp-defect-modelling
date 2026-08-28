# IP and Publication Policy

## Purpose

This document defines how intellectual property, unpublished research and public repository content should be managed within the InP defect-modelling project.

## General Principle

The repository may contain work intended for eventual publication, but not all research outputs should automatically be released publicly.

Scientific reproducibility and intellectual-property protection should be considered together.

## Public Repository Content

Generally appropriate public content includes:

- repository structure
- documentation
- generic methodology
- naming conventions
- metadata schemas
- reproducibility procedures
- non-sensitive analysis scripts
- literature notes
- public reference structures where licensing permits
- published results

## Potentially Sensitive Content

The following should be reviewed before public release:

- unpublished defect datasets
- novel defect mechanisms
- unpublished formation-energy trends
- new migration mechanisms
- unpublished high-throughput screening results
- novel computational workflows with commercial value
- unpublished device-relevant interpretations
- proprietary client or collaborator data

## Potential Intellectual Property

Potentially protectable intellectual property may include:

- novel computational workflows
- automated defect-generation systems
- new analysis pipelines
- novel defect or degradation mechanisms
- methods linking atomistic calculations with device behaviour
- machine-learning models or datasets developed later
- commercially valuable structure-property relationships

Novel scientific findings alone are not automatically patentable.

Any potential invention should be reviewed before public disclosure.

## Publication Strategy

Where publication is intended:

1. Complete critical validation.
2. Record provenance.
3. Freeze the relevant dataset.
4. Review IP implications.
5. Determine whether any patent filing is required before public disclosure.
6. Prepare the manuscript.
7. Release supporting data at an appropriate stage.

## Public Disclosure

Public disclosure may include:

- GitHub commits
- conference presentations
- posters
- preprints
- manuscripts
- public datasets
- talks
- websites

Potentially patentable information should not be publicly disclosed before appropriate IP review.

## Repository Commit Review

Before committing significant new results to the public repository, ask:

- Is this result already published?
- Is publication planned?
- Could the result have commercial value?
- Could it form part of a patentable method or invention?
- Is the data subject to collaborator restrictions?
- Does the file contain licensed material?
- Does the file contain confidential information?

If uncertain, keep the data outside the public repository until reviewed.

## Licensed Software

Do not commit licensed or restricted software data.

Examples include:

- VASP POTCAR files
- proprietary pseudopotentials
- commercial software binaries
- licence keys

## Collaborations

Collaborative work should respect:

- confidentiality agreements
- publication agreements
- funding conditions
- institutional IP policies
- collaborator ownership

## Publication Dataset

A publication dataset should contain only data cleared for public release.

It should be separated from any restricted production archive.

## Git History

Sensitive material should not be committed with the intention of deleting it later.

Git preserves file history, and removal from the latest commit does not necessarily remove earlier versions.

## Decision Rule

When uncertain whether a result is suitable for public release:

**do not commit it publicly until its IP and publication status has been reviewed.**