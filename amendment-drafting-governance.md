# Amendment Drafting Governance

## Purpose

This document sets drafting rules for defined terms and proposed amendment
text in this project so that those materials stay consistent. Use it as a
governance document for future edits to terms sections and proposed amendment
language, not as advocacy copy.

## Scope

This governance document applies to:

- defined terms sections
- proposed amendment text
- proposal sections that directly draft or revise amendment language

This governance document does not control:

- strategy documents
- campaign messaging
- operations planning
- political analysis
- historical summaries
- other repo materials that are not drafting terms or proposed amendment text

## Core Rule

Prefer simple and clear over flexible and complicated.

If a choice must be made between a bright-line rule and a nuanced standard,
default to the bright-line rule unless there is a strong reason not to.

## Hierarchy Of Drafting Levels

### Constitutional Level

Use the amendment text for high-level binding rules only:

- who is covered
- what conduct or ownership is prohibited
- what broad categories are permitted or excluded
- whether Congress has authority or a duty to implement and enforce

Do not load constitutional text with administrative machinery unless it is
essential to the rule itself.

### Implementing-Law Level

Use implementing-law concepts for operational details such as:

- approved index lists
- concentration thresholds
- trustee certification standards
- compliance forms and reporting workflows
- tax nonrecognition mechanics
- liquidation timing for illiquid assets
- auditing, penalties, and administration

### Proposal-Memo Level

Use proposal documents to test options, compare structures, and explain the
reasoning behind choices. When a proposal section is drafting defined terms or
proposed amendment language, it should respect the rules below. When a proposal
section is purely explanatory or strategic, this document is informative but
not controlling.

## Definitions Rules

Definitions should answer only: what does this term mean?

Definitions should not answer:

- who approves the term's application
- how the term is governed
- what office administers it
- what procedure applies to it
- what statute section or subchapter contains it

### Definition Drafting Defaults

- Keep definitions agnostic and portable.
- Avoid statutory scaffolding phrases such as "under this subchapter" unless
  the reference is unavoidable.
- Avoid embedding governance rules inside definitions.
- Avoid embedding enforcement rules inside definitions.
- Avoid embedding tax mechanics inside definitions beyond the minimum needed to
  identify the concept.
- If a term requires an approval mechanism, place that mechanism in the
  operative clause, not in the term definition.

### Examples

Better:

- "Safe-harbor fund" means a public fund, including an index fund or
  target-date retirement fund, that either tracks or is benchmarked to a
  specifically identified index, or follows a target-date asset-allocation
  strategy with broad diversification and automatic rebalancing, and in either
  case does not use a sector, issuer-specific, thematic, or policy-targeted
  strategy.

Worse:

- "Safe-harbor fund" means a public fund approved by statute or regulation
  under this subchapter.

Reason: qualification or approval criteria are operative rules, not part of the
core meaning of the term.

## Operative-Clause Rules

Put the following in operative provisions, not in definitions:

- which indexes qualify
- which vehicles are approved
- who certifies a trust or fund
- which thresholds apply
- what deadlines govern compliance
- how tax deferral works
- what penalties attach

Operative clauses should answer: what must happen, who must do it, by when,
and under what legal standard.

## Asset Classification Rules

### Asset-Centric, Not Account-Centric

Classify assets by instrument exposure, not by the type of account in which
they are held.

Use account-neutral legal rules. A stock held in a taxable brokerage account,
IRA, or other account remains the same type of asset.

Account-centric language is acceptable for explanation or compliance guidance,
but not as the legal basis of classification.

### Bright-Line Safe Harbors

Use a short whitelist of clearly permitted assets.

Current preferred safe-harbor categories are:

- safe-harbor funds, including target-date funds and index funds
- United States government obligations
- qualifying cash equivalents

Everything else should be presumed covered unless expressly excluded.

### Avoid Flexible Fund Standards

Avoid phrases like:

- "broadly diversified"
- "sufficiently passive"
- "not overly concentrated"
- "diversified enough"

Those standards invite argument, regulator drift, and loopholes.

Prefer:

- enumerated permitted categories
- approved index lists
- fixed numerical thresholds where necessary
- default coverage for anything outside the safe harbor

## Transfer And Tax Rules

The amendment should require a compliance mechanism for every covered asset.

The draft should assume:

- every covered asset must have a lawful exit path
- mandatory compliance transfers should not trigger immediate tax recognition
- basis carryover, deferred-gain tracking, and replacement-property rules are
  implementation details for legislation, not constitutional text

The tax rule is substantive, but the tax mechanics belong in legislation.

## Wording Defaults

When drafting, prefer these defaults:

- one term, one definition
- one rule, one place
- short enumerated categories over open-ended standards
- plain meaning over technical surplusage
- default coverage over exception-heavy drafting

Avoid:

- redundant cross-references in early draft text
- premature statutory architecture
- mixed definition and enforcement language
- mixed concept and procedure language

## Change-Control Rule

When a definition changes in the terms section, conform every downstream use of
that term.

Do not redefine a term inside a proposal section merely because the section has
a narrower use case.

If a proposal needs a narrower rule, add an operative condition instead of
changing the term's meaning.

## Review Checklist

Before accepting a drafting change, ask:

1. Is this sentence defining a term or imposing a rule?
2. If it is defining a term, did it accidentally smuggle in governance,
   enforcement, approval, or statutory structure?
3. Is the rule bright-line, or does it invite discretionary interpretation?
4. Does the asset rule depend on account type when it should depend on asset
   exposure?
5. Is this detail constitutional-level or implementing-law-level?
6. If the text creates a safe harbor, is it enumerated clearly enough that a
   non-lawyer can tell what is allowed?
7. If the text creates a compliance burden, is there a corresponding lawful
   transfer path?
8. If the text forces a transfer, does it preserve the nonrecognition principle?

## Current Project Defaults

Until affirmatively changed, use these defaults throughout the repo:

- terms remain agnostic
- operative clauses carry approval and governance rules
- asset classification remains asset-centric
- permitted funds are limited to bright-line safe harbors
- anything outside an enumerated permitted category is covered by default
- transfer and exit mechanisms must exist for every covered asset
- forced compliance should not create an immediate taxable event