"""Compile .po files to .mo using Python's Tools/i18n/msgfmt logic."""
import os
import sys
import struct
import array

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_mo(po_path, mo_path):
    """Parse PO and generate MO with proper escape handling."""
    messages = {}
    msgid_parts = []
    msgstr_parts = []
    in_msgid = False
    in_msgstr = False

    with open(po_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith('#'):
                # Save previous entry
                if in_msgstr:
                    mid = ''.join(msgid_parts)
                    mstr = ''.join(msgstr_parts)
                    if mid or mstr:  # Keep header (empty msgid)
                        messages[mid] = mstr
                msgid_parts = []
                msgstr_parts = []
                in_msgid = False
                in_msgstr = False
                continue

            if line.startswith('msgid '):
                # Save previous entry
                if in_msgstr:
                    mid = ''.join(msgid_parts)
                    mstr = ''.join(msgstr_parts)
                    if mid or mstr:
                        messages[mid] = mstr
                msgid_parts = []
                msgstr_parts = []
                in_msgid = True
                in_msgstr = False
                # Extract string content
                s = line[6:].strip()
                if s.startswith('"') and s.endswith('"'):
                    msgid_parts.append(s[1:-1])
                continue

            if line.startswith('msgstr '):
                in_msgid = False
                in_msgstr = True
                s = line[7:].strip()
                if s.startswith('"') and s.endswith('"'):
                    msgstr_parts.append(s[1:-1])
                continue

            if line.startswith('"') and line.endswith('"'):
                s = line[1:-1]
                if in_msgid:
                    msgid_parts.append(s)
                elif in_msgstr:
                    msgstr_parts.append(s)

    # Save last entry
    if in_msgstr:
        mid = ''.join(msgid_parts)
        mstr = ''.join(msgstr_parts)
        if mid or mstr:
            messages[mid] = mstr

    # Process escape sequences in all messages
    processed = {}
    for k, v in messages.items():
        # Handle common escape sequences
        k2 = k.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
        v2 = v.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
        processed[k2] = v2

    # Verify header has charset
    header = processed.get('', '')
    if 'charset=' not in header:
        processed[''] = (
            "Project-Id-Version: VR Creation 1.0\n"
            "MIME-Version: 1.0\n"
            "Content-Type: text/plain; charset=UTF-8\n"
            "Content-Transfer-Encoding: 8bit\n"
        )

    # Generate MO
    keys = sorted(processed.keys())
    offsets = []
    ids = b''
    strs = b''

    for k in keys:
        kid = k.encode('utf-8')
        val = processed[k].encode('utf-8')
        offsets.append((len(ids), len(kid), len(strs), len(val)))
        ids += kid + b'\x00'
        strs += val + b'\x00'

    keystart = 7 * 4 + 16 * len(keys)
    valstart = keystart + len(ids)
    koffsets = []
    voffsets = []

    for o in offsets:
        koffsets.append((o[1], o[0] + keystart))
        voffsets.append((o[3], o[2] + valstart))

    output = struct.pack('Iiiiiii',
                         0x950412de,  # magic
                         0,           # version
                         len(keys),   # nstrings
                         7 * 4,       # offset of key table
                         7 * 4 + len(keys) * 8,  # offset of value table
                         0,           # size of hashing table
                         0)           # offset of hashing table

    for length, offset in koffsets:
        output += struct.pack('ii', length, offset)
    for length, offset in voffsets:
        output += struct.pack('ii', length, offset)
    output += ids + strs

    os.makedirs(os.path.dirname(mo_path), exist_ok=True)
    with open(mo_path, 'wb') as f:
        f.write(output)

    return len(keys)


for lang in ['fr', 'en', 'ar']:
    po_path = os.path.join(BASE_DIR, 'locale', lang, 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join(BASE_DIR, 'locale', lang, 'LC_MESSAGES', 'django.mo')

    if not os.path.exists(po_path):
        print(f'  SKIP {lang} (no .po file)')
        continue

    count = generate_mo(po_path, mo_path)
    print(f'  OK {lang}/LC_MESSAGES/django.mo ({count} entries)')

print('Done!')
