# FRD Template

## Purpose
This file defines the **output structure** for Functional Requirements Documents (FRD). It is used by the `frd-generator` droid as the template for generating FRDs.

## How to Customize
This template is **fully user-customizable**. Modify sections, add columns, change formats to match your organization's standards. The droid will follow whatever structure is defined here.

**Common customizations:**
- Add/remove sections (e.g., add "Compliance", "Accessibility")
- Change FR ID format (e.g., `FR-MEM-001` → `REQ-001`, `BANK-FR-001`)
- Adjust priority scheme (MoSCoW → P0/P1/P2)
- Add traceability columns (JIRA ID, Confluence link, Sprint)
- Change acceptance criteria format (BDD, checklist, table)
- Add domain-specific fields (Regulatory tags, Risk level)

---

## FRD TEMPLATE STRUCTURE

```
==============================================================================
FUNCTIONAL REQUIREMENTS DOCUMENT (FRD)
==============================================================================

DOCUMENT INFORMATION
--------------------
Document Title:     [Project Name] - Functional Requirements Document
Version:            [X.X]
Date:               [YYYY-MM-DD]
Author:             [Name]
Status:             [Draft | In Review | Approved]
Source BRD:         [Reference to Business Requirements Document]

REVISION HISTORY
----------------
| Version | Date       | Author | Changes                    |
|---------|------------|--------|----------------------------|
| 1.0     | YYYY-MM-DD | Name   | Initial draft              |

==============================================================================
1. INTRODUCTION
==============================================================================

1.1 Purpose
1.2 Scope
1.3 Definitions & Acronyms
1.4 References

==============================================================================
2. SYSTEM OVERVIEW
==============================================================================

2.1 System Context
2.2 User Roles
| Role ID | Role Name | Description | Primary Functions |

2.3 Module Summary
| Module ID | Module Name | Description | User Roles |

==============================================================================
3. FUNCTIONAL REQUIREMENTS
==============================================================================

[For each Module, repeat this structure]

3.X MODULE: [Module Name]
------------------------------------------------------------------------------

### 3.X.1 Module Overview
[Brief description]

### 3.X.2 Functional Requirements

#### FR-[MOD]-[NNN]: [Requirement Title]

| Attribute          | Value                                              |
|--------------------|----------------------------------------------------|
| FR ID              | FR-[MOD]-[NNN]                                     |
| Title              | [Descriptive title - verb + object]                |
| Description        | The system shall [action] [object] [conditions]    |
| Actor              | [Primary user role]                                |
| Priority           | Must Have / Should Have / Could Have / Won't Have  |
| Source             | BRD Section [X.X]                                  |
| Module             | [Module Name]                                      |
| Epic Mapping       | [Epic Name/ID]                                     |
| Feature Mapping    | [Feature Name/ID]                                  |

**Pre-conditions:**
- [Condition that must be true before this FR can execute]

**Trigger:**
- [What initiates this functionality]

**Main Flow:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Alternate Flows:**
- AF1: [Condition] → [Alternative steps]
- AF2: [Condition] → [Alternative steps]

**Exception Flows:**
- EF1: [Error condition] → [System response]
- EF2: [Error condition] → [System response]

**Post-conditions:**
- [State after successful execution]

**Business Rules:**
- BR-[NNN]: [Business rule that applies]

**Validation Rules:**
- VR-[NNN]: [Validation that must be performed]

**Data Requirements:**
| Field Name | Type | Required | Validation | Source |

**Acceptance Criteria:**
- [ ] AC1: [Testable criterion]
- [ ] AC2: [Testable criterion]
- [ ] AC3: [Testable criterion]

**UI Reference:**
- Wireframe: [Wireframe ID/Name]
- Screen: [Screen Name]

**Dependencies:**
- Depends on: FR-[XXX]-[NNN]
- Required by: FR-[XXX]-[NNN]

---

==============================================================================
4. NON-FUNCTIONAL REQUIREMENTS (Summary)
==============================================================================

| NFR ID | Category    | Requirement                          |

==============================================================================
5. DATA REQUIREMENTS
==============================================================================

5.1 Data Entities
5.2 Data Flow

==============================================================================
6. INTEGRATION REQUIREMENTS
==============================================================================

| Integration ID | External System | Direction | Purpose | Protocol |

==============================================================================
7. TRACEABILITY MATRIX
==============================================================================

| BRD Requirement | FR ID(s) | Epic | Feature | Priority |

==============================================================================
8. APPENDIX
==============================================================================

8.1 Wireframe References
8.2 Glossary
8.3 Open Issues
```

---

## Naming Conventions (Customize as needed)

**Module Codes (default):**
- MEM = Member
- HOS = Hospital
- TPA = Third Party Administrator
- HRA = HR Admin

**Change these to match your domain:**
- Banking: CUST, OPS, TREAS, ADMIN
- Retail: SHOP, CART, PAY, INV
- Insurance: POL, CLM, UW, FIN

---

*Template Version: 1.0*
*Last Updated: 2026-04-21*
