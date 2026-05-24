import os
from sfo_creator import SFOCreator
from config_generator import ConfigGenerator

class PKGBuilder:
    """Assemble l'arborescence et copie les vrais assets graphiques dans /PACKAGE_INFO/."""
    
    def __init__(self, output_dir="build_pkg"):
        self.output_dir = output_dir
        self.package_info_dir = os.path.join(self.output_dir, "PACKAGE_INFO")
        self.usrdir_dir = os.path.join(self.output_dir, "USRDIR")

    def _copy_true_image(self, filename, fallback_header):
        """Vérifie si une vraie image existe à la racine du projet, sinon met une sécurité."""
        target_path = os.path.join(self.package_info_dir, filename)
        
        # Si vous avez généré l'image à la racine (par exemple avec votre script fix_icon0_png.py)
        if os.path.exists(filename):
            with open(filename, "rb") as src, open(target_path, "wb") as dst:
                dst.write(src.read())
        else:
            # Sécurité temporaire pour éviter de faire planter le script Python
            with open(target_path, "wb") as dst:
                dst.write(fallback_header)

    def build(self, lang_strings):
        os.makedirs(self.package_info_dir, exist_ok=True)
        os.makedirs(self.usrdir_dir, exist_ok=True)

        # 1. Dossier /PACKAGE_INFO/ (Métadonnées de l'installateur lues par le XMB)
        with open(os.path.join(self.package_info_dir, "PARAM.SFO"), "wb") as f:
            f.write(SFOCreator.create_param_sfo())

        # COPIE SÉCURISÉE DES VRAIS PIXELS (Évite le masquage sur le XMB)
        self._copy_true_image("ICON0.PNG", b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01@\x00\x00\x00\xb0\x08\x02\x00\x00\x00\xb6\xae\xca\x0b")
        self._copy_true_image("ICON2.PNG", b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x02\x00\x00\x00\x90wS\xde")

        desc = "AutoHEN Settings - Automatically enables HEN after system readiness safely."
        with open(os.path.join(self.package_info_dir, "package.txt"), "w") as f:
            f.write(f"PKG_NAME=AutoHEN_Settings\nCOMMENT={desc}\n")

        # 2. Dossier /USRDIR/ (Contenu copié définitivement sur le stockage PS3)
        # Utilisation de newline='\n' pour garantir la compatibilité Unix LF exigée par la console
        with open(os.path.join(self.usrdir_dir, "autohen.cfg"), "w", newline='\n', encoding='utf-8') as f:
            f.write(ConfigGenerator.generate())

        return (
            f"{lang_strings['success_build']} -> '{self.output_dir}'\n"
            f"   📂 /PACKAGE_INFO/\n"
            f"      ├── PARAM.SFO  (Configuration binaire)\n"
            f"      ├── ICON0.PNG  (Icône XMB de l'application)\n"
            f"      └── ICON2.PNG  (Icône binaire de la bulle d'installation PKG) 📦\n"
            f"   📂 /USRDIR/\n"
            f"      └── autohen.cfg\n"
            f"   ⭐ Application configurée pour l'affichage avec l'étoile requis sur le XMB."
        )
