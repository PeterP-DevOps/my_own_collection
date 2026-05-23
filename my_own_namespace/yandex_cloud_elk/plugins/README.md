DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create text files on remote hosts

version_added: "1.0.0"

description:
  - Creates text files with specified content.
  - Supports idempotent execution.

options:
  path:
    description:
      - Target file path.
    required: true
    type: str

  content:
    description:
      - File content.
    required: true
    type: str

author:
  - ppg
'''