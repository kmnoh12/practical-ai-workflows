# Custom Domain and Email Capture Blockers

These require user/account action and cannot be completed safely by the agent without credentials or purchase approval.

## Custom domain

Needed from user:

- choose/buy domain,
- grant DNS registrar access or provide Cloudflare nameserver/DNS UI access,
- confirm final canonical domain.

After that, agent can:

1. configure Cloudflare Pages custom domain,
2. update `site-manifest.json` `public_base_url`,
3. rebuild/push,
4. verify canonical/sitemap/robots,
5. resubmit sitemap in GSC.

## Email capture

Needed from user:

- choose provider: Kit, beehiiv, Buttondown, Tally, ConvertKit/Kit form, or another service,
- create form/list or provide public embed/action URL,
- confirm privacy policy wording.

After that, agent can:

1. wire CTA to the form,
2. add `email_signup_click` GA4 event,
3. update Privacy Policy,
4. test submit if provider supports non-secret public form actions.

Current fallback: direct ungated Markdown downloads remain available so distribution is not blocked.
