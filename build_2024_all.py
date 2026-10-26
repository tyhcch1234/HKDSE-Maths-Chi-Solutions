#!/usr/bin/env python3
"""重建 2024 年全部頁面（卷一 19 題 + 卷二 45 題）"""
from build_2024 import write_all
from content_2024_p1a import P1_A
from content_2024_p1b import P1_B
from content_2024_p1c import P1_C
from content_2024_p1d import P1_D
from content_2024_p2a import P2_A
from content_2024_p2b import P2_B
from content_2024_p2c import P2_C

NOTE = ('此題原卷附有圖形；題目中已列出全部數據，可按文字自行繪圖。'
        '其餘年份同一題的圖形可在原試卷查閱。')
NEEDS_FIG = {17, 19, 21, 22, 23, 29, 34, 38, 40}

p2 = P2_A + P2_B + P2_C
for it in p2:
    if it['n'] in NEEDS_FIG:
        it['note'] = NOTE

write_all(P1_A + P1_B + P1_C + P1_D)
write_all(p2, paper='P2')
