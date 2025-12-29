from nyan_textures import NyanTextures
from pathlib import Path

pack: NyanTextures = NyanTextures.from_file(
    "/home/eric/.local/share/Steam/steamapps/common/Nyan Cat Lost In Space/data_pack/pack01.p"
)

files: list[tuple[str, NyanTextures.FileInfo]] = list(
    zip(pack.file_names, pack.file_infos)
)
files[0][0]  # filename
files[0][1].file_size  # file_info


for file in files:
    file_path = Path("assets") / str(file[0])

    if not file_path.parent.exists():
        file_path.parent.mkdir(exist_ok=True, parents=True)
    file_path.write_bytes(
        pack.file_datas[file[1].offset : file[1].file_size + file[1].offset]
    )
