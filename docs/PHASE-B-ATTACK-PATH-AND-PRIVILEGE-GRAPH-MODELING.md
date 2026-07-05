# Phase B — Attack-Path and Privilege Graph Modeling

## Objective

Model identity relationships as a graph so Lighthouse Technology can identify how accounts, groups, service identities, delegated permissions, and critical assets combine to create potential attack paths.

## Why Graph Modeling Matters

Traditional IAM reviews usually show account lists and group membership. They do not clearly show how a compromised identity could move through the environment.

A privilege graph makes those relationships visible:

```text
Identity → Group Membership → Delegated Permission → Administrative Capability → Critical Asset
