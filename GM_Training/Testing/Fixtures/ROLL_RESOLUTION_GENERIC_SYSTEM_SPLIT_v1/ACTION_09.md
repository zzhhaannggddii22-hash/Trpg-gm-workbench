# ACTION 09｜Playwall authorization missing

Player asks to use a Playwall ability, but the current test state contains no unlocked code or authorization evidence.

Follow the current Playwall protocol: record authorization as BLOCKED_OR_UNKNOWN, do not retrieve a document, do not infer its identity/content, and do not treat this as a dice-pipeline integration decision.
