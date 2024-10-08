# Request Tracker

Request Tracker, commonly abbreviated to 'RT' is the software
used by the NAISS ticket system.

## Workflow

### As presented

As presented by Henric Zazzi on 2024-10-03 at the NAISS All-Hands:

```mermaid
flowchart TD
  new_ticket[New ticket]
  owned_ticket[Owned ticket]
  stalled_ticket[Stalled ticket]
  resolved_ticket[Resolved ticket]

  new_ticket --> |time and knowledge| owned_ticket
  owned_ticket --> |when solution has been sent| resolved_ticket
  owned_ticket --> |When ticket cannot be solved yet| stalled_ticket
  stalled_ticket --> |When ticket can be solved| owned_ticket
```

### Alternative

As discussed at the whiteboard discussion:

```mermaid
flowchart TD
  new_ticket[New ticket]
  owned_ticket[Owned ticket]
  stalled_ticket[Stalled ticket]
  resolved_ticket[Resolved ticket]

  new_ticket --> |time and knowledge| owned_ticket
  owned_ticket --> |When ticket cannot be solved yet| stalled_ticket
  owned_ticket --> |When use has not confirmed the ticket is solved yet| stalled_ticket
  stalled_ticket --> |When ticket can be solved| owned_ticket
  stalled_ticket --> |When the user has confirmed the ticket has been solved| resolved_ticket
```
