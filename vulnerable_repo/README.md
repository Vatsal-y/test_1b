# Highly Vulnerable Repository (Target: CRITICAL Risk / Manual Review Required)

This repository is intentionally designed to showcase a **high-risk, dangerous outcome** in TrustLens:
- **Security Agent (CRITICAL)**:
  - 💉 **SQL Injection**: String concatenation and f-strings in SQL execution.
  - ⚡ **Arbitrary Code Execution**: Dangerous `eval()` execution.
  - 💻 **Command Injection**: Unsanitized `os.system()` system shell execution.
  - 🔑 **Hardcoded Secrets**: Plaintext API keys and database passwords.
  - 📦 **Insecure Deserialization**: Arbitrary Python execution via `pickle.loads()`.
  - 📂 **Path Traversal**: Arbitrary file read via unvalidated `open()`.
- **Logic Agent (HIGH / CRITICAL)**:
  - ♾️ **Infinite Loop**: `while True:` without break statement.
  - 💥 **Index Out Of Bounds**: Accessing `items[len(items)]`.
  - 👻 **Unreachable Code**: Statement following `return`.
- **Quality Agent (POOR)**:
  - 🌪️ 6-level deep indentation nesting.
  - Zero comments and non-modular architecture.
- **Decision Agent Outcome**: `MANUAL_REVIEW_REQUIRED` (Red badge, Critical Risk).
