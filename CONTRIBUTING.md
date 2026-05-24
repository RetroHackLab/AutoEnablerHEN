# 🤝 Contributing to AutoEnabler HEN

Thank you for your interest in contributing to this Computer Science student portfolio project! To maintain a clean, secure, and reliable codebase for the PlayStation 3 HFW 4.xx homebrew scene, please adhere to the following guidelines:

## 📋 Contribution Rules

*   **Strict User-Space Isolation**: No code or script interacting with `dev_flash`, `dev_blind`, or attempting to execute unauthorized writes to LV1/LV2 hypervisor registers will be accepted.
*   **Zero External Dependencies**: All tools must continue to run using **pure Python** without requiring any external `pip install` commands. This ensures seamless native execution on automated cloud environments like GitHub Actions.
*   **Respect the Star and Language Matrix**: Any changes made to the graphical user interface strings must be mirrored inside the multi-language dictionary of `languages.py` and must preserve the `⭐` title prefix.

## 🔧 Workflow Guidelines

1. Fork the repository to your own GitHub account.
2. Create a local branch for your fix or feature (`git checkout -b feature/UI-Enhancement`).
3. Run the safety check script locally (`python main.py export-pkg`) to ensure no forbidden system keywords are triggered.
4. Submit a Pull Request (PR) to the `main` branch. The automated automated CI pipeline (`.github/workflows/validate.yml`) will verify your code integrity.
