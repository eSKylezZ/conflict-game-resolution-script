# resolution-script.spec

# Import necessary modules
from PyInstaller.utils.hooks import collect_data_files
import os

# Define the data files to include
datas = [
    ('images/CD-BoxArt.jpg', 'images'),
    ('images/CD2-BoxArt.jpg', 'images'),
    ('images/Vietnam-BoxArt.jpg', 'images'),
    ('images/Global-BoxArt.jpg', 'images')
]

# Define the Analysis object
a = Analysis(
    ['resolution-script.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

# Define the rest of the spec file as usual
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='resolution-script',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='resolution-script'
)
