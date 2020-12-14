import sys
from module.darkexe.lib import compile
from module.darkexe.lib  import auxiliary
from module.darkexe.lib  import encryption
from termcolor import colored


class Darkexe(object):
    def __init__(self):
        super(Darkexe, self).__init__()
        self.enc_algos = ["xor"]
        self.compile_binary = compile.Binary()

    def _do_encrypt(self):
        print(f"[i] Begining encryption via {self.crypt_type.upper()}")
        keys_used = {}
        for loop in range(self.loops):
            if self.crypt_type == "xor":
                crypt = encryption.XOR()
            if loop == 0:
                bytes, len, key = crypt.crypt_file(True, crypt.key, infile=self.in_file)
            else:
                bytes, len, key = crypt.crypt_file(True, crypt.key, infile=None, data=bytes, data_length=len)
            keys_used[str(loop)] = key
            if loop != self.loops - 1:
                bytes = auxiliary.clean_hex_output(bytes)
        return bytes, len, keys_used


    def _do_jmp(self):
        bytes, length, keys_used = self._do_encrypt()

        keys = []
        for i in keys_used: keys.append(hex(int(i)))

        pe_image = auxiliary.prepare_pe_image(length, bytes)
        auxiliary.write_pe_image(pe_image)

        auxiliary.write_header_file(keys_used, jmp=True)
        file_clean = auxiliary.write_decrypt("./module/darkexe/src/jmp_loader/main.c", self.loops)

        self.compile_binary.compile("./module/darkexe/src/jmp_loader/main.c", self.out_file)
        auxiliary.clean_up("./module/darkexe/src/jmp_loader/main.c", file_clean)
        print(f"[+] Wrote {auxiliary.get_size('/root/' + self.out_file)} bytes to /root/{self.out_file}")



    def _parse_args(self, args):
        self.jmp = True
        self.in_file = args
        self.crypt_type = 'xor'
        self.loops = 5
        self.out_file = auxiliary.gen_rand_filename() + ".exe"

    def _do_crypt(self):
        print(f"[i] Started armouring {self.in_file} ({auxiliary.get_size(self.in_file)} bytes)")
        if self.jmp:
            self._do_jmp()

    def run(self, args):

        file_add = args

        self._parse_args(args=file_add)
        self._do_crypt()

