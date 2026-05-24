# 🔒 Security Policy — AutoEnabler HEN (PS3 HFW 4.xx)

## ⚠️ Security Commitment & Compatibility

This project is an open-source educational utility developed for Computer Science research and software architecture analysis. 

The application operates strictly within **User-Space** and exclusively targets PlayStation 3 consoles running **HFW (Hybrid Firmware) 4.xx** (such as HFW 4.90 or 4.91). Any pull request, injection, or modification aiming to alter or patch permanent system files, official core firmware, or flash memory partitions (`dev_flash` / `dev_blind`) is strictly forbidden and violates the integrity of this repository.

## 🐛 Reporting a Vulnerability / System Bug

If you discover a critical bug, a boot freeze, or any abnormal behavior that could lead to console stability issues or user data corruption:

1. **Do NOT** open a public GitHub Issue. This helps keep the repository stable and protects the community.
2. Send a detailed report via a private message directly on **Reddit** to the core developer: [One_Status_8555](https://reddit.com).
3. Please include your generated `autohen.cfg` file, your active PS3 HFW firmware version, the HEN version, and any active background plugins (like webMAN MOD).

We will analyze your report as an academic case study and update the anti-bootloop logic in our safety validator accordingly. ⚡
