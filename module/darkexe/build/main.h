#define key0 0x5a
#define key1 0x5f
#define key2 0x2a
#define key3 0x4a
#define key4 0x62

VOID FixImageIAT(PIMAGE_DOS_HEADER dos_header, PIMAGE_NT_HEADERS nt_header);
LPVOID MapImageToMemory(LPVOID base_addr);
