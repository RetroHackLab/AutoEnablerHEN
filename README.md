# ⚡ AutoEnabler HEN — Toolkit & AutoHEN Settings

![AutoHEN XMB Wave](https://www.picgifs.com/games-gifs/games-gifs/console-playstation-3/picgifs-console-playstation-3-6129901.gif)

A professional, user-space Python toolkit that safely generates PlayStation 3 (PS3) HEN configuration files and homebrew PKG installer structures. 🎮🔒

---

## ⚠️ Disclaimer (Clause de non-responsabilité)

**ENGLISH:**  
This project is an independent educational tool designed exclusively for user-space customization on PlayStation 3 systems running HEN. It does **not** modify, patch, or alter the PS3 core firmware, flash memory (`dev_flash`), or system files. 
The software is provided "as is", without warranty of any kind. The authors and contributors are not responsible for any console bans, data loss, hardware freezes, or accidental damage resulting from the use or misuse of this toolkit. Use at your own risk.

**FRANÇAIS :**  
Ce projet est un outil éducatif indépendant conçu exclusivement pour la personnalisation en espace utilisateur (*user-space*) des systèmes PS3 avec HEN. Il **ne modifie pas**, ne patch pas et n'altère en aucun cas le micrologiciel officiel, la mémoire flash (`dev_flash`) ou les fichiers système de la console. 
Le logiciel est fourni "tel quel", sans aucune garantie. Les auteurs et contributeurs déclinent toute responsabilité en cas de bannissement du PSN, perte de données, gels matériels ou dommages accidentels résultant de l'utilisation de cette boîte à outils. Vous l'utilisez à vos propres risques.

---

## 🎯 Main Purpose

**AutoHEN Settings** is a safe, reversible user-space application that removes the need for clicking the manual "Enable HEN" button on boot. 

It orchestrates system startup behavior, injects necessary configs, and operates with **zero modifications** to the PS3 permanent firmware or system flash (`dev_flash`).

---

## 🚀 Key Features

* ⚡ **AutoHEN Control**: Toggles background HEN activation and features a **Fast Mode** to reduce startup delays.
* 🛠️ **Startup Services**: Automates startup orchestration for webMAN MOD, mmCM, and custom Package Manager shortcuts.
* 🌐 **System Tweaks**: Prevents accidental console bans by blocking PSN Sign-in and skipping intrusive system update prompts.
* 🛡️ **Anti-Bootloop Protection**: Built-in failsafe mechanisms that automatically disable auto-start scripts after a crash detection.
* 🌍 **Console Native I18n**: Dynamically synchronizes application language strings with the native PS3 system language.
* 🎚️ **XMB Styling**: Package structure built to deliver a modern, neon-glow XMB style configuration utility.

---

## 📂 Repository Layout

```text
AutoEnablerHEN/
├── .gitignore             # Excludes compilation caches and final build folders
├── LICENSE                # Open-source MIT License terms
├── README.md              # Documentation and developer workflow guide
├── main.py                # Unified CLI entry-point
├── pkg_builder.py         # Constructs PS3 structural tree with /PACKAGE_INFO/
├── config_generator.py    # Outputs user-space reversible autohen.cfg files
├── sfo_creator.py         # Low-level binary assembler for PARAM.SFO metadata
├── safety_validator.py    # Security rule analyzer enforcing user-space isolation
└── languages.py           # Multi-language text maps matching the PS3 OS
```

---

## 🎛️ Developer Workflow (CLI)

This project runs using **pure Python** with zero external dependencies. Open your terminal inside the repository and execute:

### 1. 🏗️ Build Package Structure
Generates the standard local PS3 PKG directory tree, isolating installer metadata under `/PACKAGE_INFO/` and target configurations inside `/USRDIR/`:
```bash
python main.py build
```

### 2. ⚙️ Inspect Configuration Layout
Outputs a clean text block representing the future `autohen.cfg` structure tailored for homebrew deployment loaders:
```bash
python main.py config
```

### 3. 🌍 Test System Translations
Simulates how the homebrew core handles multi-language rendering and falls back safely to English when an unsupported language is encountered:
```bash
python main.py test-lang
```

### 🛡️ 4. Execute Safety Validation
Runs a critical static code analysis on the generated structure to verify that no forbidden firmware paths or hardware registers are targeted:
```bash
python main.py export-pkg
```

---

## 📦 PS3 Structural Deployment Output

After successfully triggering the build sequence, your `build_pkg/` directory will look as follows, matching the exact format required by binary bundlers like `make_package_npdimm`:

```text
build_pkg/
├── PACKAGE_INFO/            # Metadata read by the PS3 OS during installation
│   ├── ICON0.PNG            # Neon-blue "H" asset preview placeholder
│   ├── PARAM.SFO            # Binary application identification block
│   └── package.txt          # Informational installer package manifest
└── USRDIR/                  # Safe space payload copied into dev_hdd0/game/
    └── autohen.cfg          # Reversible plain-text configuration switches
```

---

## 📄 License

Distributed under the **MIT License**. Project is 100% reversible and completely uninstallable via the standard XMB interface. 📜
