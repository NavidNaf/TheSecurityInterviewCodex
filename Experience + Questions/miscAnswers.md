# Miscellaneous Security Interview Answers

This file contains short answers for the standalone questions in [miscQuestions.md](miscQuestions.md).

## Network and System Identification

### `[23BK-FIN]` Suppose you are given a fresh PC or laptop connected only to an internal network, with no external internet access. How would you identify the operating system of another device on the same internal network?

I would use `ping` and look at the TTL value in the response to make an initial OS guess. A TTL near `128` usually suggests Windows, while a TTL near `64` usually suggests Linux or Unix-like systems, though this is only an estimate because network hops can reduce the value.

## Source Code Analysis

### `[22IDLC-R2]` What tools have you used previously for source code analysis?

For source code analysis, common tools include Semgrep, SonarQube, Bandit, CodeQL, SpotBugs, ESLint security plugins, and dependency scanners like Snyk or OWASP Dependency-Check. The exact tool depends on the language, but I would combine static analysis, dependency review, secret scanning, and manual code review.

### `[22IDLC-R2]` How would you securely design a system for source code analysis?

I would isolate the analysis environment because source code and build processes can be sensitive or potentially unsafe. The system should use sandboxing, least privilege, access control, audit logging, encrypted storage, and separate workers for scanning untrusted repositories.

## Offensive Security and Compliance

### `[22IDLC-FIN]` If an organization is ISO compliant, how would you use your offensive security expertise during audits?

I would use offensive security to validate whether the controls described in policies are actually effective in practice. This could include penetration testing, control validation, attack simulation, vulnerability assessment, and mapping findings back to ISO control requirements and risk treatment plans.
