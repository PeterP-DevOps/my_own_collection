# create_file role

Role for creating text files using custom Ansible module.

## Variables

| Variable | Default |
|---|---|
| file_path | /tmp/default.txt |
| file_content | Default content |

## Example

```yaml
roles:
  - role: create_file
    vars:
      file_path: "/tmp/example.txt"
      file_content: "Hello"