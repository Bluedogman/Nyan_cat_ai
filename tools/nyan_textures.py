# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class NyanTextures(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(NyanTextures, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\xF1\xA7\x51\x05":
            raise kaitaistruct.ValidationNotEqualError(b"\xF1\xA7\x51\x05", self.magic, self._io, u"/seq/0")
        self.num_files = self._io.read_u4le()
        self.unk_num_2 = self._io.read_u4le()
        self.file_names = []
        for i in range(self.num_files):
            self.file_names.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))

        self.file_infos = []
        for i in range(self.num_files):
            self.file_infos.append(NyanTextures.FileInfo(self._io, self, self._root))

        self.file_datas = self._io.read_bytes_full()


    def _fetch_instances(self):
        pass
        for i in range(len(self.file_names)):
            pass

        for i in range(len(self.file_infos)):
            pass
            self.file_infos[i]._fetch_instances()


    class FileInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(NyanTextures.FileInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unk_num_3_1 = self._io.read_u4le()
            self.ukn_num_3_2 = self._io.read_u4le()
            self.offset = self._io.read_u4le()
            self.file_size = self._io.read_u4le()


        def _fetch_instances(self):
            pass



