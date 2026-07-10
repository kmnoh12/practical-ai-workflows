---
title: "Why GPT-5.6 Sol Max and Ultra Are Missing in Hermes Agent"
description: "Hermes Agent can reach GPT-5.6 Sol, but its UI exposes xhigh as Max and cannot reproduce Codex Ultra with one setting. Here is the code-level gap."
slug: "hermes-agent-gpt-5-6-sol-max-ultra"
status: "published"
noindex: false
category: "Agent Runtime Investigations"
order: 0
updated: "2026-07-10"
indexable: true
qa_approved: true
cta: "Copy the Max and Ultra Control-Path Checklist"
social_image: "/assets/social/hermes-max-ultra-og.png"
social_image_alt: "Hermes Agent control path showing GPT-5.6, max reasoning, the xhigh user interface ceiling, and the separate Codex Ultra orchestration layer."
---

Hermes Agent can reach an OpenAI Codex model and still fail to reproduce the experience you selected in Codex.

That is exactly what happens around GPT-5.6 Sol, Max, and Ultra. In the Hermes picker, the option labeled **Max** is backed by the value `xhigh`. The Python parser separately accepts `max`, and the Codex transport can forward that value upstream. But Hermes does not expose an Ultra-equivalent control, and a single reasoning value cannot recreate what OpenAI documents as maximum reasoning plus proactive subagent delegation.

So the model is not necessarily absent. The control surface is incomplete.

## Tested with

| Field | Recorded scope |
|---|---|
| Hermes build | 0.18.2, local commit `d2e64fcb8` |
| Hermes upstream snapshot | `caf557be5`, checked 2026-07-10 |
| Provider path observed locally | `openai-codex` |
| Model identifier observed locally | `gpt-5.6-sol` |
| Public OpenAI model mapping | `gpt-5.6` alias routes to `gpt-5.6-sol` |
| Surfaces inspected | Python config parser, Codex Responses transport, web picker, desktop status label |
| External evidence | OpenAI docs, Hermes docs, Hermes source, open GitHub issues |

## What this is based on

This investigation combines a sanitized local observation with public source inspection.

The local Hermes logs showed requests routed through `openai-codex` with the model identifier `gpt-5.6-sol`. No account IDs, session IDs, credentials, prompts, or private paths are reproduced here. OpenAI's current model guidance publicly confirms that the `gpt-5.6` alias routes to `gpt-5.6-sol`, its flagship-capability model. The local route therefore matches a documented public model name.

The implementation findings are reproducible in the public Hermes repository:

- The core parser accepts `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
- The web picker stops at `xhigh` and labels it `Max`.
- The desktop label also maps `xhigh` to `Max`.
- The Codex Responses transport forwards the active value as `reasoning.effort`.

Sources: the [OpenAI GPT-5.6 launch announcement](https://openai.com/index/gpt-5-6/), [OpenAI model and reasoning guidance](https://developers.openai.com/api/docs/guides/latest-model), [OpenAI subagent and Ultra guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents#choosing-models-and-reasoning), [Hermes reasoning configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#reasoning-effort), and the pinned [Hermes source snapshot](https://github.com/NousResearch/hermes-agent/tree/caf557be5b4c9ae75b3a7566d65d3df2c701c5df).

The evidence labels and redaction rules follow this site's [editorial policy](../editorial-policy/).

![Control-path diagram showing where Hermes exposes xhigh, accepts max, and lacks an Ultra-equivalent switch](../assets/evidence/hermes-max-ultra-control-gap.png)

## The short answer

There are four separate layers, and most explanations collapse them into one:

1. **Model availability:** Is GPT-5.6 actually available to the account and provider route?
2. **Request-level reasoning:** Does the request send `reasoning.effort` as `xhigh` or `max`?
3. **Agent runtime behavior:** Does the harness preserve that setting across the main agent, background jobs, and delegated agents?
4. **Product mode:** Does the client implement the orchestration behavior bundled into Codex Ultra?

Hermes has partial support at layers one through three. It does not expose a Codex Ultra product mode.

That distinction explains the apparently contradictory evidence. Hermes can accept and forward `max` while still failing to offer Max correctly in its picker. It can run GPT-5.6 while still behaving differently from Codex. And it can spawn subagents while still not reproducing Ultra's proactive delegation policy.

## What changed on July 9

OpenAI's GPT-5.6 launch made three details public that matter for this diagnosis:

1. The `gpt-5.6` alias routes to the flagship `gpt-5.6-sol` model.
2. `max` gives GPT-5.6 more reasoning time than `xhigh`.
3. `ultra` coordinates four agents in parallel by default, and developers can build ultra-like API experiences with the separate multi-agent beta.

The launch announcement also separates entitlement from third-party client support. Max is available to users who have GPT-5.6 access in ChatGPT Work and Codex. Ultra is available in ChatGPT Work for Pro and Enterprise users, and in Codex for Plus and higher plans. That does not force Hermes to expose either control correctly. Account eligibility and client implementation are different gates.

This is why an old explanation such as "Sol is only an internal slug" or "Max is just another name for xhigh" is now wrong.

## The exact control-path gap

| Layer | What the source says | What the user sees | Practical consequence |
|---|---|---|---|
| OpenAI model | GPT-5.6 supports `max` reasoning | Depends on account, model, and client | The capability can exist upstream |
| OpenAI Ultra | Maximum reasoning plus proactive delegation on eligible accounts and models | Ultra is a distinct intelligence mode | It is more than one request parameter |
| Hermes parser | `max` is accepted | Not directly visible | Manual configuration can enter a state the picker does not represent |
| Hermes web picker | Highest option is `xhigh` labeled Max | Max appears selectable | The label hides the underlying value |
| Hermes desktop label | `xhigh` renders as Max | Status bar says Max | The same naming mismatch persists |
| Hermes transport | Active effort is forwarded to `reasoning.effort` | Invisible unless inspected | The wire can carry `max` even when the UI cannot select it |
| Hermes delegation | Separate provider, model, depth, and concurrency controls | Configured independently | It does not automatically become Codex Ultra |

The key bug is not that every request is forced to medium. The key bug is that the user-facing state, the parser state, the request state, and the orchestration state are not one coherent control.

## Why the Hermes picker says Max when it means xhigh

The current web helper defines this final option:

```text
{ value: "xhigh", label: "Max" }
```

It then builds the set of valid picker values from that list. A raw value outside the list is normalized to `medium` for the picker. Because `max` is absent from the options, the UI cannot faithfully represent the parser's full accepted range.

The desktop status formatter follows the same convention:

```text
xhigh: "Max"
```

This is not a philosophical naming complaint. It creates an observable diagnostic problem:

- Selecting Max in Hermes means selecting `xhigh`.
- Setting `max` outside the picker can create a valid backend state that the picker does not understand as a selectable state.
- Reading the status label alone cannot prove that the upstream request used `max`.

The exact public code is visible in [the web reasoning picker](https://github.com/NousResearch/hermes-agent/blob/caf557be5b4c9ae75b3a7566d65d3df2c701c5df/web/src/lib/reasoning-effort.ts#L17-L35) and [the desktop status label](https://github.com/NousResearch/hermes-agent/blob/caf557be5b4c9ae75b3a7566d65d3df2c701c5df/apps/desktop/src/lib/model-status-label.ts#L3-L20).

## But the Hermes core really does accept max

The Python side tells a different story. `VALID_REASONING_EFFORTS` explicitly includes `max`, and `parse_reasoning_effort()` returns an enabled config for it. `ultra` is not in that parser list.

The Codex transport starts with `medium`, replaces it with the configured effort when present, and sends:

```json
{
  "reasoning": {
    "effort": "max",
    "summary": "auto"
  }
}
```

That payload is a simplified representation of the relevant fields, not a captured private request.

The implementation is visible in [the Hermes parser](https://github.com/NousResearch/hermes-agent/blob/caf557be5b4c9ae75b3a7566d65d3df2c701c5df/hermes_constants.py#L794-L819) and [the Codex Responses transport](https://github.com/NousResearch/hermes-agent/blob/caf557be5b4c9ae75b3a7566d65d3df2c701c5df/agent/transports/codex.py#L155-L166).

This means a careful statement is:

> Hermes 0.18.2 has a backend path that can accept and forward max. Its public configuration and picker treat xhigh as the selectable ceiling and label xhigh as Max.

That is narrower and more useful than saying either "Hermes supports Max" or "Hermes does not support Max." Both slogans hide the control-path split.

## Why max still does not equal Ultra

OpenAI documents `ultra`, `max`, and `xhigh` as distinct reasoning choices when the selected model supports them. It also describes Ultra as an eligible-account mode that uses maximum reasoning and can proactively delegate suitable work to subagents. The GPT-5.6 launch announcement is even more concrete: Ultra coordinates four agents in parallel by default.

That gives Ultra at least two observable dimensions:

1. **Reasoning depth:** the selected model runs at the maximum supported reasoning level.
2. **Orchestration policy:** the product can decide to split independent work across agents without waiting for a separate delegation instruction.

Sending `reasoning.effort=max` addresses only the first dimension.

Hermes has delegation features, including child limits, depth controls, provider overrides, and model overrides. Those are useful, but they are Hermes controls. They do not prove behavioral parity with Codex Ultra's eligibility rules, proactive delegation policy, thread management, or mode-level defaults.

The OpenAI API documentation makes the same architectural distinction from another angle. It describes GPT-5.6 `max` reasoning as one capability, and [Multi-agent](https://developers.openai.com/api/docs/guides/tools-multi-agent) as a separate beta capability similar to Ultra mode.

That API path is not a dropdown alias. It requires the Responses Multi-agent beta, an explicit `multi_agent.enabled` request field, and support for new output items such as `multi_agent_call` and `agent_message`. OpenAI also says `reasoning.summary` is not supported when Multi-agent is enabled. The reviewed Hermes Codex transport builds a normal reasoning payload with `summary: "auto"` and does not build that hosted Multi-agent request.

Hermes can still delegate through its own `delegate_task` system. The point is not that Hermes lacks subagents. The point is that its subagent system is separate from the OpenAI hosted Multi-agent protocol and is not exposed as a first-class Ultra mode.

So there is no honest one-line Hermes setting that means "be Codex Ultra." A wrapper must implement the orchestration contract, not just pass a larger effort string.

## Four scenarios that look similar but are not

### Scenario 1: You choose Max in the Hermes UI

The picker stores `xhigh`. The status label says Max. Assuming the setting reaches the main Codex request, the request is an xhigh request, not proof of a max request.

### Scenario 2: You manually configure max

In the inspected 0.18.2 code, the parser accepts `max` and the normal Codex transport can forward it. This is a useful diagnostic experiment on a supported model.

It is not a clean product guarantee. Hermes' own documentation says `max` is accepted on the wire but is not a selectable reasoning value, with `xhigh` as the configurable ceiling. The picker also lacks a stable visual state for `max`.

### Scenario 3: You ask Hermes to use Ultra

There is no inspected Hermes control that maps an Ultra mode into maximum reasoning plus Codex-style proactive orchestration. Hermes may reason deeply. It may delegate when instructed or when its own agent behavior decides to use delegation. That is still not evidence that the Codex Ultra contract is active.

### Scenario 4: The main agent is high effort but an internal agent is not

Configuration inheritance is another failure point. [Hermes issue #18871](https://github.com/NousResearch/hermes-agent/issues/18871) documents a background review path that can create a fresh agent without the parent's reasoning config, causing the Codex transport to fall back to `medium`.

That does not mean every Hermes subagent falls back to medium. It proves that checking only the main session is insufficient. Every internal construction path has to preserve model, effort, service tier, and provider state if parity is the goal.

## Why your Codex settings may not carry over

Hermes can reuse Codex authentication without behaving like the Codex client.

[Hermes issue #9603](https://github.com/NousResearch/hermes-agent/issues/9603) describes inconsistent inheritance of Codex CLI defaults such as model, reasoning effort, and service tier across chat, gateway, cron, and picker flows. The expected precedence in that issue is explicit Hermes config first, Codex CLI fallback second, and Hermes defaults third.

Until that behavior is complete and verified across entry points, treat Hermes and Codex as separate configuration domains:

- Authentication reuse does not imply setting reuse.
- Model discovery does not imply reasoning-mode reuse.
- A matching model label does not imply matching orchestration.
- A main-session setting does not imply child-session inheritance.

This is the broader lesson for any third-party AI agent. The wrapper owns more of the behavior than the model name suggests.

## What you can safely configure today

For the documented Hermes control surface, use `xhigh` when you want its highest selectable effort:

```yaml
agent:
  reasoning_effort: xhigh
```

If you are diagnosing GPT-5.6 `max` specifically on Hermes 0.18.2, the inspected parser suggests this experimental configuration:

```yaml
agent:
  reasoning_effort: max
```

Use the second form only with three caveats:

1. The selected upstream model must support `max`.
2. The Hermes UI does not expose `max` as its own option and may not display that state faithfully.
3. A max main request still does not activate Codex Ultra orchestration.

Do not judge the result from response length or subjective intelligence. Those are noisy signals. Inspect configuration resolution and request metadata where your client safely exposes them, then run a repeatable workload.

## A practical verification playbook

Use one test task with several independent workstreams, such as:

- inspect three unrelated modules,
- run separate test groups,
- compare two implementation strategies,
- synthesize one final decision.

Then record these fields:

| Check | Evidence to collect | What it answers |
|---|---|---|
| Model route | Sanitized model and provider metadata | Did the request reach the intended model path? |
| Main effort | Resolved config or sanitized request field | Was `xhigh` or `max` sent? |
| Child effort | Same field for every child or background agent | Was reasoning inherited? |
| Delegation trigger | User instruction, runtime policy, or automatic event | Was delegation requested or proactive? |
| Agent count | Number of child threads actually created | Did orchestration happen? |
| Synthesis | Parent result references child outputs | Were results combined rather than merely spawned? |
| Failure path | Unsupported-mode error or fallback record | Did the runtime fail clearly or silently downgrade? |

Run the same task across four configurations:

1. In Codex with Max.
2. In Codex with Ultra, if your account and model expose it.
3. In Hermes with `xhigh`.
4. In Hermes with the diagnostic `max` value.

Do not compare only the prose answer. Compare the execution trace: effort, delegation decision, number of agents, inheritance, tool work, and synthesis.

## What Hermes would need for real Ultra parity

A credible implementation would need more than another dropdown item.

### 1. Honest effort labels

Expose `xhigh` and `max` as distinct values when the selected model supports both. Do not label `xhigh` as Max if a higher `max` state exists on the route.

### 2. Capability-aware selection

The picker should use provider and model capabilities, not a universal static list. Unsupported values should produce a clear message instead of a silent normalization.

### 3. An explicit Ultra-equivalent mode

If Hermes wants to offer Ultra parity through its own harness, the mode needs a documented bundle: maximum supported reasoning, proactive delegation policy, agent-depth defaults, concurrency behavior, synthesis rules, and cost warnings. If it instead adopts OpenAI's hosted Multi-agent beta, it also needs the beta request field and output-item handling required by that protocol.

### 4. Full runtime inheritance

Main agents, delegated agents, background reviews, cron jobs, gateway sessions, and auxiliary tasks need deliberate inheritance rules. A child falling back to medium can invalidate the mode even when the parent is configured correctly.

### 5. Observable execution

The UI should show the resolved model, actual effort, service tier, child count, and whether delegation was automatic or user-requested. A label is not enough.

### 6. Parity tests

Tests should assert both payload and behavior:

- `max` survives config parsing and UI round trips.
- Every agent clone inherits the intended reasoning config.
- Unsupported models fail clearly.
- Ultra-equivalent mode delegates suitable independent work without an extra prompt.
- The parent waits for and synthesizes child results.

Without those tests, "supports Ultra" would be marketing language, not an engineering claim.

## Copy the control-path checklist

Use this whenever a third-party agent claims support for a new model or reasoning mode:

- [ ] Record the exact client, version, provider route, model ID, and date.
- [ ] Separate public model names from local or private runtime slugs.
- [ ] Check what the UI label stores, not only what it displays.
- [ ] Check which values the config parser accepts.
- [ ] Check which value the transport actually sends.
- [ ] Check whether unsupported values error, clamp, or silently normalize.
- [ ] Check main-agent and child-agent settings separately.
- [ ] Distinguish reasoning depth from orchestration behavior.
- [ ] Record whether delegation was explicit, policy-driven, or proactive.
- [ ] Compare execution traces, not only final prose.
- [ ] Preserve account and model eligibility limits.
- [ ] Recheck after every client update.

## FAQ

### Is xhigh the same as max in GPT-5.6?

No. OpenAI lists `xhigh` and `max` as separate GPT-5.6 reasoning efforts and recommends comparing them on representative workloads. Max gives the model more time than xhigh.

### Can I enable Codex Ultra in Hermes by setting reasoning_effort to max?

No. The inspected Hermes path can parse and forward the `max` request value, but Ultra also includes a multi-agent execution mode. A max request does not activate that orchestration contract.

### Does Codex OAuth make Hermes inherit the same model and mode settings?

Not reliably across every surface in the reviewed version. Authentication reuse, model selection, reasoning effort, fast mode, and orchestration are separate state. Hermes issue #9603 tracks part of that inheritance gap.

### Why can native Codex and Hermes behave differently with the same model?

The client controls the system prompt, tools, context, retries, configuration precedence, background jobs, delegation, and user interface. Matching the model name aligns only one layer of the runtime.

## Limits

This is a source and control-path investigation, not a benchmark.

I did not measure answer quality, token consumption, latency, or success rates across repeated Max and Ultra runs. I did not inspect OpenAI's private server implementation. The local observation covers one Hermes 0.18.2 installation and one point-in-time upstream snapshot.

The public OpenAI docs support `gpt-5.6-sol`, `max` reasoning, and the documented Ultra behavior. Hermes and OpenAI can change these controls after the date above.

GitHub issues are evidence of reported, inspectable gaps. An open issue is not proof that every user hits the bug on every path.

## Bottom line

The Hermes problem is not simply "GPT-5.6 Sol is unavailable."

The inspected runtime can route to the model, the parser can accept `max`, and the Codex transport can forward it. But the user interface calls `xhigh` Max, cannot faithfully select the separate `max` state, and exposes no equivalent to Codex Ultra's combined reasoning and proactive orchestration behavior.

Use `xhigh` as the documented Hermes ceiling. Treat `max` as a version-specific diagnostic path until the UI and docs make it a first-class capability. Treat Ultra as a harness mode that requires orchestration parity, not a magic string.

That is the difference between reaching the same model and running the same agent.
