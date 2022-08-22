eda-hooks
============

Pre-commit hooks for Ansible EDA.


### Add the following to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/ttuffin/eda-hooks/
  rev: v1.0.0
  hooks:
    - id: run_ansible_test
      args: [sanity]
```