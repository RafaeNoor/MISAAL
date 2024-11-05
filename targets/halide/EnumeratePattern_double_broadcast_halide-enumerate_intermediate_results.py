{
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:xBroadcast_is32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 4)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:xBroadcast_is32_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 32)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+2048+typed:xBroadcast_is16_os2048_signed_None+typed:xBroadcast_is32_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 64)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os2048_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:xBroadcast_is32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 8)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:xBroadcast_is32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 16)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:xBroadcast_is32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 2)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:xBroadcast_is16_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 64)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:xBroadcast_is32_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 32)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:xBroadcast_is16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 8)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:xBroadcast_is32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 4)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:xBroadcast_is16_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 16)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+2048+typed:xBroadcast_is8_os2048_signed_None+typed:xBroadcast_is32_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 256)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 64)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os2048_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+2048+typed:xBroadcast_is8_os2048_signed_None+typed:xBroadcast_is16_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 256)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 128)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os2048_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:xBroadcast_is32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 8)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:xBroadcast_is16_os32_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 2)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os32_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:xBroadcast_is16_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 32)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:xBroadcast_is32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 16)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:xBroadcast_is16_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 4)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:xBroadcast_is32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 2)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:xBroadcast_is32_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 32)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:xBroadcast_is32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 4)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+2048+typed:xBroadcast_is16_os2048_signed_None+typed:xBroadcast_is32_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 64)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os2048_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:xBroadcast_is32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 8)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:xBroadcast_is32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 16)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:xBroadcast_is32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 2)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:xBroadcast_is32_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:xBroadcast_is16_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 64)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:xBroadcast_is16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 8)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+2048+typed:xBroadcast_is8_os2048_signed_None+typed:xBroadcast_is16_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 256)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 128)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os2048_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:xBroadcast_is16_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 16)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:xBroadcast_is16_os32_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 2)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os32_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:xBroadcast_is16_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 32)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:xBroadcast_is16_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 4)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os512_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip8_is16_op8_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t16\n\t )\n\t32\n\t32\n\t16\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:xBroadcast_is16_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 0 1 64 16 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 64 1 64 16 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 0 1 32 32 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 32 1 32 32 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 0 1 16 64 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 16 1 16 64 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 0 1 128 8 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 128) 128 1 128 8 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 8 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 4 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 2 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 16 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 16 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 8 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 4 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 32 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is16_os32_signed_None+typed:slice_vectors_ip16_is64_op16_os32_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 0 1 2 16 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is64_op16_os32_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is16_os32_signed_None+typed:slice_vectors_ip16_is64_op16_os32_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 2 1 2 16 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is64_op16_os32_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is16_os32_signed_None+typed:slice_vectors_ip32_is64_op32_os32_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 0 1 1 32 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is64_op32_os32_signed_None_0_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is16_os32_signed_None+typed:slice_vectors_ip32_is64_op32_os32_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 1 1 1 32 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is64_op32_os32_signed_None_1_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is16_os32_signed_None+typed:slice_vectors_ip8_is64_op8_os32_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 4 1 4 8 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is64_op8_os32_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is16_os32_signed_None+typed:slice_vectors_ip8_is64_op8_os32_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 0 1 4 8 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is64_op8_os32_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 32 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 16 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 8 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 64 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 4 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 2 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 1 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 8 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 0 1 64 16 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 64 1 64 16 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 0 1 32 32 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 32 1 32 32 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 0 1 16 64 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 16 1 16 64 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 0 1 128 8 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 128 1 128 8 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 8 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 4 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 2 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 16 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 16 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 8 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 4 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 32 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 32 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 16 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 8 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 64 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 4 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 2 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 1 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is32_os64_signed_None+typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 8 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is32_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 0 1 64 16 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 0 1 32 32 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 64 1 64 16 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 32 1 32 32 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 0 1 16 64 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 16 1 16 64 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is2048_op64_os1024_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 0 1 128 8 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 256) 128 1 128 8 2048)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 8 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 4 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 2 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 16 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+16+typed:xBroadcast_is8_os16_signed_None+typed:slice_vectors_ip16_is32_op16_os16_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 0 1 1 16 32)",
                "output_size": 16,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os16_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is32_op16_os16_signed_None_0_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+16+typed:xBroadcast_is8_os16_signed_None+typed:slice_vectors_ip16_is32_op16_os16_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 1 1 1 16 32)",
                "output_size": 16,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os16_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is32_op16_os16_signed_None_1_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+16+typed:xBroadcast_is8_os16_signed_None+typed:slice_vectors_ip8_is32_op8_os16_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 0 1 2 8 32)",
                "output_size": 16,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os16_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is32_op8_os16_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+16+typed:xBroadcast_is8_os16_signed_None+typed:slice_vectors_ip8_is32_op8_os16_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 2)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 2 1 2 8 32)",
                "output_size": 16,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os16_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is32_op8_os16_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 16 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 8 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 4 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 32 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:slice_vectors_ip16_is64_op16_os32_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 0 1 2 16 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is64_op16_os32_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:slice_vectors_ip16_is64_op16_os32_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 2 1 2 16 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is64_op16_os32_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:slice_vectors_ip32_is64_op32_os32_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 0 1 1 32 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is64_op32_os32_signed_None_0_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:slice_vectors_ip8_is64_op8_os32_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 0 1 4 8 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is64_op8_os32_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:slice_vectors_ip32_is64_op32_os32_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 1 1 1 32 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is64_op32_os32_signed_None_1_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:slice_vectors_ip8_is64_op8_os32_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 4 1 4 8 64)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is64_op8_os32_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 32 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 16 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 8 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 64 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 4 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 2 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 1 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 8 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t1\n\t64\n\t8\n\t1024\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:concat_vectors_ip16_is512_op16_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 16 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is512_op16_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:concat_vectors_ip32_is512_op32_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 32 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is512_op32_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:concat_vectors_ip64_is512_op64_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 64 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is512_op64_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is16_os1024_signed_None+typed:concat_vectors_ip8_is512_op8_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 8 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is512_op8_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:concat_vectors_ip16_is64_op16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 16 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is64_op16_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:concat_vectors_ip32_is64_op32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 32 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is64_op32_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:concat_vectors_ip64_is64_op64_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 64 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is64_op64_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is16_os128_signed_None+typed:concat_vectors_ip8_is64_op8_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 8 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is64_op8_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is16_os2048_signed_None+typed:concat_vectors_ip16_is1024_op16_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 16 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is1024_op16_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is16_os2048_signed_None+typed:concat_vectors_ip32_is1024_op32_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 32 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is1024_op32_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is16_os2048_signed_None+typed:concat_vectors_ip64_is1024_op64_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 64 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is1024_op64_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is16_os2048_signed_None+typed:concat_vectors_ip8_is1024_op8_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 8 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is1024_op8_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:concat_vectors_ip16_is128_op16_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 16 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is128_op16_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:concat_vectors_ip32_is128_op32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 32 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is128_op32_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:concat_vectors_ip64_is128_op64_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 64 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is128_op64_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is16_os256_signed_None+typed:concat_vectors_ip8_is128_op8_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 8 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is128_op8_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:concat_vectors_ip16_is256_op16_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 16 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is256_op16_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:concat_vectors_ip32_is256_op32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 32 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is256_op32_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:concat_vectors_ip64_is256_op64_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 64 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is256_op64_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:concat_vectors_ip16_is32_op16_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 16 32)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is32_op16_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is16_os512_signed_None+typed:concat_vectors_ip8_is256_op8_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 8 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is256_op8_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:concat_vectors_ip32_is32_op32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is32_op32_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+64+typed:xBroadcast_is16_os64_signed_None+typed:concat_vectors_ip8_is32_op8_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 8 32)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is16_os64_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is32_op8_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:concat_vectors_ip16_is512_op16_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 16 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is512_op16_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:concat_vectors_ip32_is512_op32_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 32 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is512_op32_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:concat_vectors_ip64_is512_op64_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 64 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is512_op64_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is32_os1024_signed_None+typed:concat_vectors_ip8_is512_op8_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 8 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is512_op8_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:concat_vectors_ip16_is64_op16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) 16 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is64_op16_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:concat_vectors_ip32_is64_op32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) 32 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is64_op32_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:concat_vectors_ip64_is64_op64_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) 64 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is64_op64_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is32_os128_signed_None+typed:concat_vectors_ip8_is64_op8_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) (typed:xBroadcast (reg (bv #x00 8)) 32 32 2) 8 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is64_op8_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is32_os2048_signed_None+typed:concat_vectors_ip16_is1024_op16_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 16 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is1024_op16_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is32_os2048_signed_None+typed:concat_vectors_ip32_is1024_op32_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 32 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is1024_op32_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is32_os2048_signed_None+typed:concat_vectors_ip64_is1024_op64_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 64 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is1024_op64_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is32_os2048_signed_None+typed:concat_vectors_ip8_is1024_op8_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 8 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is1024_op8_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:concat_vectors_ip16_is128_op16_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 16 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is128_op16_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:concat_vectors_ip32_is128_op32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 32 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is128_op32_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:concat_vectors_ip64_is128_op64_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 64 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is128_op64_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is32_os256_signed_None+typed:concat_vectors_ip8_is128_op8_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 8 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is128_op8_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:concat_vectors_ip16_is256_op16_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 16 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is256_op16_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:concat_vectors_ip32_is256_op32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 32 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is256_op32_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:concat_vectors_ip64_is256_op64_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 64 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is256_op64_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is32_os512_signed_None+typed:concat_vectors_ip8_is256_op8_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 8 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is32_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is256_op8_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:concat_vectors_ip16_is512_op16_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 16 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is512_op16_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:concat_vectors_ip32_is512_op32_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 32 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is512_op32_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:concat_vectors_ip64_is512_op64_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 64 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is512_op64_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+1024+typed:xBroadcast_is8_os1024_signed_None+typed:concat_vectors_ip8_is512_op8_os1024_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 128)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 8 512)",
                "output_size": 1024,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os1024_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is512_op8_os1024_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:concat_vectors_ip16_is64_op16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 16 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is64_op16_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:concat_vectors_ip32_is64_op32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 32 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is64_op32_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:concat_vectors_ip64_is64_op64_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 64 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is64_op64_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+128+typed:xBroadcast_is8_os128_signed_None+typed:concat_vectors_ip8_is64_op8_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 8 64)",
                "output_size": 128,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os128_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is64_op8_os128_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is8_os2048_signed_None+typed:concat_vectors_ip16_is1024_op16_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 256)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 16 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is1024_op16_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:concat_vectors_ip16_is128_op16_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 16 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is128_op16_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is8_os2048_signed_None+typed:concat_vectors_ip32_is1024_op32_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 256)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 32 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is1024_op32_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:concat_vectors_ip32_is128_op32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 32 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is128_op32_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:concat_vectors_ip64_is128_op64_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 64 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is128_op64_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is8_os2048_signed_None+typed:concat_vectors_ip64_is1024_op64_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 256)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 64 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is1024_op64_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+2048+typed:xBroadcast_is8_os2048_signed_None+typed:concat_vectors_ip8_is1024_op8_os2048_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 256)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 8 1024)",
                "output_size": 2048,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os2048_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is1024_op8_os2048_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+256+typed:xBroadcast_is8_os256_signed_None+typed:concat_vectors_ip8_is128_op8_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 8 128)",
                "output_size": 256,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os256_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is128_op8_os256_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:concat_vectors_ip16_is16_op16_os32_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is16_op16_os32_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+32+typed:xBroadcast_is8_os32_signed_None+typed:concat_vectors_ip8_is16_op8_os32_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 8 16)",
                "output_size": 32,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os32_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is16_op8_os32_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:concat_vectors_ip16_is256_op16_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 16 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is256_op16_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:concat_vectors_ip32_is256_op32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 32 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is256_op32_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:concat_vectors_ip64_is256_op64_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 64 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip64_is256_op64_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:concat_vectors_ip16_is32_op16_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 16 32)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:concat_vectors_ip16_is32_op16_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+512+typed:xBroadcast_is8_os512_signed_None+typed:concat_vectors_ip8_is256_op8_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 8 256)",
                "output_size": 512,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os512_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is256_op8_os512_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:concat_vectors_ip32_is32_op32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:concat_vectors_ip32_is32_op32_os64_signed_None"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )+ (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )+64+typed:xBroadcast_is8_os64_signed_None+typed:concat_vectors_ip8_is32_op8_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_double_broadcast",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 8 32)",
                "output_size": 64,
                "original_src_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os512_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:concat_vectors ; typed:concat_vectors_ip8_is256_op8_os512_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os256_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t16\n\t )\n\t8\n\t256\n )",
                "src_ctx": "typed:xBroadcast_is8_os64_signed_None",
                "dst_ctx": "typed:concat_vectors_ip8_is32_op8_os64_signed_None"
            }
        }
    ]
}