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


### cloudflare-skills

- Source: https://github.com/cloudflare/skills
- Local path: `community_skills/cloudflare-skills/`
- Integration: Git submodule
- Use when: working with Cloudflare Workers, Pages, KV, D1, R2, AI, Tunnel, WAF, Wrangler, Durable Objects, Agents SDK, Cloudflare Email Service, Workers best practices, or Cloudflare MCP server setup.
- Notes: Read the relevant `skills/<name>/SKILL.md` before executing commands. Treat `.mcp.json` as a reference until credentials and permissions are explicitly configured.

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
