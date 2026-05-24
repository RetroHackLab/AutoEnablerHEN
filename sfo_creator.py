import struct

class SFOCreator:
    """Générateur binaire autonome pour assembler un fichier PARAM.SFO valide."""
    
    @staticmethod
    def create_param_sfo(title_id="AHEN00001", title="⭐AutoHEN Settings"):
        # Encodage explicite en UTF-8 pour le calcul des octets réels (Requis pour l'étoile ⭐)
        title_bytes = title.encode('utf-8')
        title_id_bytes = title_id.encode('utf-8')
        
        key_table = b"TITLE_ID\x00TITLE\x00"
        val_table = title_id_bytes.ljust(12, b'\x00') + title_bytes.ljust(64, b'\x00')
        
        key_start = 0x14 + (2 * 16)
        val_start = key_start + len(key_table)
        
        header = struct.pack("<4sIHHII", b"\x00PSF", 0x00010100, key_start, val_start, 2, 2)
        idx_title_id = struct.pack("<HHIII", 0, 0x0204, len(title_id_bytes), 12, 0)
        
        # Utilisation de len(title_bytes) au lieu de len(title) pour éviter la corruption binaire sur PS3
        idx_title = struct.pack("<HHIII", 9, 0x0204, len(title_bytes), 64, 12)
        
        return header + idx_title_id + idx_title + key_table + val_table
