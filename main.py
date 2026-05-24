import sys
from pkg_builder import PKGBuilder
from config_generator import ConfigGenerator
from safety_validator import SafetyValidator
from languages import LanguageManager

def main():
    pc_lang_id = LanguageManager.detect_pc_language()
    lang = LanguageManager.get_strings(pc_lang_id)
    
    if len(sys.argv) < 2:
        print(lang["cli_usage"])
        sys.exit(1)

    cmd = sys.argv.lower()
    target_dir = "build_pkg"

    if cmd == "build":
        print(PKGBuilder(target_dir).build(lang))
    elif cmd == "config":
        print(ConfigGenerator.generate())
    elif cmd == "export-pkg":
        success, msg = SafetyValidator.validate_structure(target_dir, lang)
        print(msg)
        if not success: sys.exit(1)
    elif cmd == "test-lang":
        print("🌍 Translation Matrix :")
        for lang_id, name in [(0, "English"), (1, "Français"), (2, "Español")]:
            strings = LanguageManager.get_strings(lang_id)
            print(f" -> PS3 ({name:8}) : '{strings['enable_hen']}' [{strings['btn_on']}]")
    else:
        print(f"{lang['err_unknown']} {cmd}")
        print(lang["cli_usage"])

if __name__ == "__main__":
    main()
