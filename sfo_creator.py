import struct

class SFOCreator:
    """Générateur binaire autonome pour assembler un fichier PARAM.SFO valide et visible sur le XMB."""
    
    @staticmethod
    def create_param_sfo(title_id="AHEN00001", title="⭐AutoHEN Settings"):
        title_bytes = title.encode('utf-8')
        title_id_bytes = title_id.encode('utf-8')
        category_bytes = b"HG\x00"  # HG = Homebrew/Game Application (Requis pour l'affichage sur le XMB)
        
        # Table contenant les 3 clés requises ordonnées ALPHABÉTIQUEMENT (Obligatoire pour le format PSF)
        key_table = b"CATEGORY\x00TITLE\x00TITLE_ID\x00"
        
        # Alignement strict des structures de données binaires avec bourrage de zéros (\x00)
        val_table = (
            category_bytes.ljust(4, b'\x00') + 
            title_bytes.ljust(64, b'\x00') + 
            title_id_bytes.ljust(12, b'\x00')
        )
        
        # En-tête de 20 octets + 3 descripteurs d'index de 16 octets
        key_start = 0x14 + (3 * 16)
        val_start = key_start + len(key_table)
        
        # En-tête magique du format SFO de la PS3 (Indique 3 entrées)
        header = struct.pack("<4sIHHII", b"\x00PSF", 0x00010100, key_start, val_start, 3, 3)
        
        # Alignement exact des index mémoires (Offset de la clé, Type, Taille réelle, Taille max, Offset de la valeur)
        idx_category = struct.pack("<HHIII", 0, 0x0204, 3, 4, 0)
        idx_title = struct.pack("<HHIII", 9, 0x0204, len(title_bytes), 64, 4)
        idx_title_id = struct.pack("<HHIII", 15, 0x0204, len(title_id_bytes), 12, 68)
        
        return header + idx_category + idx_title + idx_title_id + key_table + val_table
