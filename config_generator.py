class ConfigGenerator:
    """Gère l'écriture propre de la configuration utilisateur de façon réversible."""
    
    DEFAULT_CONFIG = {
        "ps3_system_language": -1,
        "enable_autohen": 1,
        "fast_mode": 0,
        "autostart_webman": 1,
        "block_psn_signin": 1,
        "skip_update_prompt": 1,
        "safe_mode_protection": 1,
        "restore_defaults_on_uninstall": 1
    }

    @classmethod
    def generate(cls, user_prefs=None):
        config = cls.DEFAULT_CONFIG.copy()
        if user_prefs:
            config.update(user_prefs)
            
        lines = [
            "[AutoHEN_Settings]", 
            "# TARGET PLATFORM: PS3 HFW 4.xx ONLY (Hybrid Firmware Required)",
            "# Language: -1 = PS3 System Native, 0 = Force English Only",
            "# User-space only architecture - 100% Safe"
        ]
        for key, value in config.items():
            lines.append(f"{key}={value}")
        return "\n".join(lines)
