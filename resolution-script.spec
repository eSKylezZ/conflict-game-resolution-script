# -*- mode: python ; coding: utf-8 -*-

datas = [
    ('images/CD-BoxArt.jpg', 'images'),
    ('images/CD2-BoxArt.jpg', 'images'),
    ('images/Vietnam-BoxArt.jpg', 'images'),
    ('images/Global-BoxArt.jpg', 'images')
]

a = Analysis(
    ['resolution-script.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='resolution-script',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
