import sys
import base64
import urllib.parse
import binascii
import codecs
import random

# Codificações

def base64_encode(data):
    return base64.b64encode(data.encode()).decode()

def base16_encode(data):
    return base64.b16encode(data.encode()).decode()

def base32_encode(data):
    return base64.b32encode(data.encode()).decode()

def hex_encode(data):
    return ''.join(f'\\x{ord(c):02x}' for c in data)

def url_encode(data):
    return urllib.parse.quote(data)

def html_entities(data):
    return ''.join(f'&#{ord(c)};' for c in data)

def js_escape(data):
    return ''.join(f'\\x{ord(c):02x}' for c in data)

def unicode_escape(data):
    return data.encode('unicode_escape').decode()

def unicode_codepoints(data):
    return ''.join(f'\\u{ord(c):04x}' for c in data)

def utf8_bytes(data):
    return ' '.join(f'\\x{b:02x}' for b in data.encode('utf-8'))

def rot13_encode(data):
    return codecs.encode(data, 'rot_13')

def xor_encode(data, key=0x42):
    return ''.join(f'\\x{ord(c) ^ key:02x}' for c in data)

def reversed_base64(data):
    return base64.b64encode(data[::-1].encode()).decode()

def double_base64(data):
    once = base64.b64encode(data.encode())
    return base64.b64encode(once).decode()

def fake_characters(data):
    return ''.join(c + '\u200B' for c in data)  # adiciona zero-width space após cada caractere

# Embaralhamentos

def reverse_string(data):
    return data[::-1]

def python_chr_encode(data):
    return ' + '.join(f'chr({ord(c)})' for c in data)

def js_concat_encode(data):
    return ' + '.join(f'"{c}"' for c in data)

def split_concat(data):
    return '+'.join(f'"{c}"' for c in data)

def odd_even_swap(data):
    chars = list(data)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)

# Junções de técnicas

def reverse_then_base64(data):
    return base64.b64encode(reverse_string(data).encode()).decode()

def base64_then_url(data):
    return url_encode(base64_encode(data))

def xor_then_base64(data):
    xor = ''.join(chr(ord(c) ^ 0x42) for c in data)
    return base64.b64encode(xor.encode()).decode()

def html_then_url(data):
    return url_encode(html_entities(data))

def chr_then_join(data):
    return 'exec(' + repr(''.join([f"chr({ord(c)})+" for c in data])[:-1]) + ')'

def base64_url_reverse(data):
    return reverse_string(url_encode(base64_encode(data)))

def xor_then_unicode(data):
    return ''.join(f'\\u{ord(chr(ord(c) ^ 0x42)):04x}' for c in data)

def char_concat(data):
    return '||'.join(f"char({ord(c)})" for c in data)

def hex_concat(data):
    return '0x' + ''.join(f'{ord(c):02x}' for c in data)

def unicode_concat(data):
    return ' + '.join(f"nchar({ord(c)})" for c in data)

# Randomizador e Mutações

def mutate_payload(data):
    techniques = [
        base64_encode, base16_encode, base32_encode, hex_encode,
        url_encode, html_entities, js_escape, unicode_escape,
        unicode_codepoints, utf8_bytes, rot13_encode, xor_encode,
        reversed_base64, double_base64, reverse_string, python_chr_encode,
        js_concat_encode, split_concat, odd_even_swap, reverse_then_base64,
        base64_then_url, xor_then_base64, html_then_url, chr_then_join,
        base64_url_reverse, xor_then_unicode, char_concat, hex_concat,
        unicode_concat, fake_characters
    ]
    chosen = random.sample(techniques, k=min(3, len(techniques)))
    result = data
    for fn in chosen:
        try:
            result = fn(result)
        except:
            continue
    return result

def combo_mutations(data, rounds=5):
    outputs = []
    for _ in range(rounds):
        outputs.append(mutate_payload(data))
    return outputs

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 ufuscator.py '<código>' [--random | --combo | --deep]")
        sys.exit(1)

    payload = sys.argv[1]
    flags = sys.argv[2:] if len(sys.argv) > 2 else []

    print("\n💣 Entrada:")
    print(payload)

    if '--random' in flags:
        print("\n🎲 Randomizador com Mutação:")
        print(mutate_payload(payload))
        return

    if '--combo' in flags:
        print("\n🎰 Combo de Mutações:")
        for i, out in enumerate(combo_mutations(payload, rounds=5), 1):
            print(f"[{i}] {out}")
        return

    if '--deep' in flags:
        print("\n🧬 Mutação Profunda (10x):")
        for i, out in enumerate(combo_mutations(payload, rounds=10), 1):
            print(f"[{i}] {out}")
        return

    print("\n🎭 Ofuscações:")
    print(f"[Base64]               {base64_encode(payload)}")
    print(f"[Double Base64]        {double_base64(payload)}")
    print(f"[Reversed Base64]      {reversed_base64(payload)}")
    print(f"[Base16]               {base16_encode(payload)}")
    print(f"[Base32]               {base32_encode(payload)}")
    print(f"[Hex]                  {hex_encode(payload)}")
    print(f"[URL Encoded]          {url_encode(payload)}")
    print(f"[HTML Entities]        {html_entities(payload)}")
    print(f"[JS Escape]            {js_escape(payload)}")
    print(f"[Unicode Escape]       {unicode_escape(payload)}")
    print(f"[Unicode Codepoints]   {unicode_codepoints(payload)}")
    print(f"[UTF-8 Bytes]          {utf8_bytes(payload)}")
    print(f"[ROT13]                {rot13_encode(payload)}")
    print(f"[XOR ^ 0x42]           {xor_encode(payload)}")
    print(f"[Fake Characters]      {fake_characters(payload)}")
    print(f"[Reverse]              {reverse_string(payload)}")
    print(f"[Python chr()]         {python_chr_encode(payload)}")
    print(f"[JS concat]            {js_concat_encode(payload)}")
    print(f"[Split + Concat]       {split_concat(payload)}")
    print(f"[Odd-Even Swap]        {odd_even_swap(payload)}")

    print("\n🧪 Junções de Técnicas:")
    print(f"[Reverse + Base64]     {reverse_then_base64(payload)}")
    print(f"[Base64 + URL]         {base64_then_url(payload)}")
    print(f"[XOR + Base64]         {xor_then_base64(payload)}")
    print(f"[HTML + URL]           {html_then_url(payload)}")
    print(f"[Chr() + Join]         {chr_then_join(payload)}")
    print(f"[Base64 + URL + Rev]   {base64_url_reverse(payload)}")
    print(f"[XOR + Unicode]        {xor_then_unicode(payload)}")

    print("\n🛠 Técnicas adicionais:")
    print(f"[Char Concat]          {char_concat(payload)}")
    print(f"[Hex Concat]           {hex_concat(payload)}")
    print(f"[Unicode Concat]       {unicode_concat(payload)}")

if __name__ == "__main__":
    main()
