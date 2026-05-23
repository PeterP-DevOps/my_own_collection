#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create text files on remote hosts

version_added: "1.0.0"

description:
    - Creates a text file on remote hosts.
    - Writes content into the file.
    - Supports idempotency.

options:
    path:
        description:
            - Path to target file.
        required: true
        type: str

    content:
        description:
            - Content for the target file.
        required: true
        type: str

author:
    - Your Name
'''

EXAMPLES = r'''
- name: Create file
  my_own_module:
    path: /tmp/test.txt
    content: "Hello DevOps"
'''

RETURN = r'''
changed:
    description: Shows whether file was changed.
    type: bool
    returned: always

message:
    description: Result message.
    type: str
    returned: always
'''

import os

from ansible.module_utils.basic import AnsibleModule


def run_module():

    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    # check mode support
    if module.check_mode:
        module.exit_json(**result)

    file_exists = os.path.exists(path)

    current_content = ''

    if file_exists:
        with open(path, 'r') as f:
            current_content = f.read()

    # idempotency check
    if not file_exists or current_content != content:

        with open(path, 'w') as f:
            f.write(content)

        result['changed'] = True
        result['message'] = 'File created or updated'

    else:
        result['message'] = 'File already exists with same content'

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()