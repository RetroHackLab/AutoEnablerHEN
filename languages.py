class LanguageManager:
    """Gère l'affichage des textes selon la langue native détectée sur la PS3."""
    
    LANG_ENGLISH = 0
    LANG_FRENCH = 1
    LANG_SPANISH = 2

    TRANSLATIONS = {
        LANG_ENGLISH: {
            "title": "AutoHEN Settings",
            "desc": "Automatically enables HEN after system readiness safely.",
            "enable_hen": "Enable AutoHEN",
            "fast_mode": "Fast Mode",
            "btn_on": "ON",
            "btn_off": "OFF"
        },
        LANG_FRENCH: {
            "title": "Options AutoHEN",
            "desc": "Active automatiquement le HEN dès que le système est prêt.",
            "enable_hen": "Activer AutoHEN",
            "fast_mode": "Mode Rapide",
            "btn_on": "OUI",
            "btn_off": "NON"
        },
        LANG_SPANISH: {
            "title": "Ajustes AutoHEN",
            "desc": "Activa automáticamente HEN de forma segura al iniciar el sistema.",
            "enable_hen": "Activar AutoHEN",
            "fast_mode": "Modo Rápido",
            "btn_on": "SI",
            "btn_off": "NO"
        }
    }

    @classmethod
    def get_strings(cls, ps3_system_lang_id):
        return cls.TRANSLATIONS.get(ps3_system_lang_id, cls.TRANSLATIONS[cls.LANG_ENGLISH])
