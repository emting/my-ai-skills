# Community Skills

Place third-party skill libraries or references here.

Recommended approaches:

- Git submodule.
- Git subtree.
- Link index to external repositories.
- Curated copied documentation with license notes.

## Included Community Libraries

### awesome-agent-skills

- Source: https://github.com/heilcheng/awesome-agent-skills
- Local path: `community_skills/awesome-agent-skills/`
- Integration: Git submodule
- Use when: looking for external agent skill examples, references, or reusable community skill patterns.

## Submodule Commands

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/YOUR_USERNAME/my-ai-skills.git
```

Initialize after a normal clone:

```bash
git submodule update --init --recursive
```

Update community skills:

```bash
git submodule update --remote --merge
```
