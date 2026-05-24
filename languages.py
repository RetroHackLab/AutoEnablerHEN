import locale

class LanguageManager:
    """Gère l'affichage des textes selon la langue du PC (CLI) et de la PS3."""
    
    # Identifiants de langue officiels de la PS3 OS
    LANG_ENGLISH = 0
    LANG_FRENCH = 1
    LANG_SPANISH = 2

    TRANSLATIONS = {
        LANG_ENGLISH: {
            "title": "⭐AutoHEN Settings",
            "desc": "Automatically enables HEN after system readiness safely.",
            "enable_hen": "Enable AutoHEN",
            "fast_mode": "Fast Mode",
            "btn_on": "ON",
            "btn_off": "OFF",
            "cli_usage": "Usage: python main.py [build | config | export-pkg | test-lang]",
            "err_unknown": "❌ Unknown command:",
            "success_build": "⚡ PKG Structure successfully generated",
            "err_build": "❌ Error: Build directory does not exist.",
            "safe_valid": "✅ User-Space isolation validated. No Flash modification detected.",
            "safe_danger": "🚨 SYSTEM DANGER detected:"
        },
        LANG_FRENCH: {
            "title": "⭐Options AutoHEN",
            "desc": "Active automatiquement le HEN dès que le système est prêt.",
            "enable_hen": "Activer AutoHEN",
            "fast_mode": "Mode Rapide",
            "btn_on": "OUI",
            "btn_off": "NON",
            "cli_usage": "Utilisation : python main.py [build | config | export-pkg | test-lang]",
            "err_unknown": "❌ Commande inconnue :",
            "success_build": "⚡ Structure PKG générée avec succès",
            "err_build": "❌ Erreur : Le dossier de build n'existe pas.",
            "safe_valid": "✅ Isolation Espace Utilisateur validée. Aucune modification du Flash détectée.",
            "safe_danger": "🚨 DANGER SYSTEME détecté :"
        },
        LANG_SPANISH: {
            "title": "⭐Ajustes AutoHEN",
            "desc": "Activa automáticamente HEN de forma segura al iniciar el sistema.",
            "enable_hen": "Activar AutoHEN",
            "fast_mode": "Modo Rápido",
            "btn_on": "SI",
            "btn_off": "NO",
            "cli_usage": "Uso: python main.py [build | config | export-pkg | test-lang]",
            "err_unknown": "❌ Comando desconocido:",
            "success_build": "⚡ Estructura PKG generada con éxito",
            "err_build": "❌ Error: El directorio de build no existe.",
            "safe_valid": "✅ Aislamiento de Espacio de Usuario validado. No se detectó modificación de Flash.",
            "safe_danger": "🚨 DANGER SISTEMA detectado:"
        }
    }

    @classmethod
    def get_strings(cls, ps3_system_lang_id):
        """Retourne les chaînes pour la PS3 ou applique l'anglais par défaut."""
        return cls.TRANSLATIONS.get(ps3_system_lang_id, cls.TRANSLATIONS[cls.LANG_ENGLISH])

    @classmethod
    def detect_pc_language(cls):
        """Détecte la langue actuelle de l'ordinateur pour traduire le terminal CLI."""
        try:
            default_lang, _ = locale.getdefaultlocale()
            if default_lang:
                default_lang = default_lang.lower()
                if "fr" in default_lang:
                    return cls.LANG_FRENCH
                elif "es" in default_lang:
                    return cls.LANG_SPANISH
        except Exception:
            pass
        return cls.LANG_ENGLISH
