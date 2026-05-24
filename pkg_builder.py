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

        with open(os.path.join(self.package_info_dir, "PARAM.SFO"), "wb") as f:
            f.write(SFOCreator.create_param_sfo())

        with open(os.path.join(self.package_info_dir, "ICON0.PNG"), "wb") as f:
            f.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")

        desc = "AutoHEN Settings - Automatically enables HEN after system readiness safely."
        with open(os.path.join(self.package_info_dir, "package.txt"), "w") as f:
            f.write(f"PKG_NAME=AutoHEN_Settings\nCOMMENT={desc}\n")

        with open(os.path.join(self.usrdir_dir, "autohen.cfg"), "w") as f:
            f.write(ConfigGenerator.generate())

        return (
            f"{lang_strings['success_build']} -> '{self.output_dir}'\n"
            f"   📂 /PACKAGE_INFO/ (PARAM.SFO, ICON0.PNG)\n"
            f"   📂 /USRDIR/ (autohen.cfg)"
        )
