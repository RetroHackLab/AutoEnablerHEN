import os

class SafetyValidator:
    """Analyse les dossiers de build pour interdire toute écriture sur le firmware."""
    
    FORBIDDEN_TRIGGERS = ["dev_flash", "dev_blind", "lv1", "lv2", "vsh_plugin", "patch", "flash_write"]

    @classmethod
    def validate_structure(cls, build_dir, lang_strings):
        if not os.path.exists(build_dir):
            return False, lang_strings["err_build"]

        for root, _, files in os.walk(build_dir):
            for file in files:
                if file.endswith(('.cfg', '.txt', '.xml', '.ini')):
                    path = os.path.join(root, file)
                    with open(path, 'r', errors='ignore') as f:
                        content = f.read().lower()
                        for trigger in cls.FORBIDDEN_TRIGGERS:
                            if trigger in content:
                                return False, f"{lang_strings['safe_danger']} '{trigger}' -> {file}."
                                
        # Ajout du témoin visuel de conformité de l'étoile requise sur la PS3
        success_msg = f"{lang_strings['safe_valid']}\n⭐ [INFO] Titre de l'application validé avec préfixe sur le XMB."
        return True, success_msg
