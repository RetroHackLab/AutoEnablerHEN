import os
from sfo_creator import SFOCreator
from config_generator import ConfigGenerator

class PKGBuilder:
    """Assemble l'arborescence et isole les métadonnées dans /PACKAGE_INFO/."""
    
    def __init__(self, output_dir="build_pkg"):
        self.output_dir = output_dir
        self.package_info_dir = os.path.join(self.output_dir, "PACKAGE_INFO")
        self.usrdir_dir = os.path.join(self.output_dir, "USRDIR")

    def build(self, lang_strings):
        os.makedirs(self.package_info_dir, exist_ok=True)
        os.makedirs(self.usrdir_dir, exist_ok=True)

        # 1. Dossier /PACKAGE_INFO/ (Métadonnées de l'installateur lues par le XMB)
        with open(os.path.join(self.package_info_dir, "PARAM.SFO"), "wb") as f:
            f.write(SFOCreator.create_param_sfo())

        # ICON0.PNG : Icône finale de l'application affichée sur le XMB
        with open(os.path.join(self.package_info_dir, "ICON0.PNG"), "wb") as f:
            f.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")

        # ICON2.PNG : Icône spécifique de la bulle d'installation du PKG
        with open(os.path.join(self.package_info_dir, "ICON2.PNG"), "wb") as f:
            f.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")

        desc = "AutoHEN Settings - Automatically enables HEN after system readiness safely."
        with open(os.path.join(self.package_info_dir, "package.txt"), "w") as f:
            f.write(f"PKG_NAME=AutoHEN_Settings\nCOMMENT={desc}\n")

        # 2. Dossier /USRDIR/ (Contenu copié définitivement sur le stockage PS3)
        with open(os.path.join(self.usrdir_dir, "autohen.cfg"), "w") as f:
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
