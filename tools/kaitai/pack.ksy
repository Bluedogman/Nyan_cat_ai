meta:
  id: nyan_textures
  title: Nyan_textures
  file-extension: p
  endian: le
  bit-endian: le
seq:
  - id: magic
    contents: [0xf1,0xa7,0x51,0x05]
  - id: num_files
    type: u4
  - id: unk_num_2
    type: u4
  - id: file_names
    encoding: ASCII
    type: str
    repeat: expr
    repeat-expr: num_files
    terminator: 0
  - id: file_infos
    type: file_info
    repeat: expr
    repeat-expr: num_files
  - id: file_datas
    size-eos: true
types:
  file_info:
    seq:
      - id: unk_num_3_1
        type: u4
      - id: ukn_num_3_2
        type: u4
      - id: offset
        type: u4
      - id: file_size
        type: u4 