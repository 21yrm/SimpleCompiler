# Generated from Cgrammer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,74,626,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,4,4,4,309,8,4,11,4,12,4,310,1,4,1,4,4,4,315,8,
        4,11,4,12,4,316,1,5,3,5,320,8,5,1,5,1,5,5,5,324,8,5,10,5,12,5,327,
        9,5,1,5,3,5,330,8,5,1,6,1,6,1,6,3,6,335,8,6,1,7,1,7,1,7,1,7,1,8,
        1,8,5,8,343,8,8,10,8,12,8,346,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,359,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,
        1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,41,
        1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,45,1,45,1,46,
        1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,51,1,51,1,51,
        1,52,1,52,1,53,1,53,1,53,1,54,1,54,1,54,1,55,1,55,1,56,1,56,1,57,
        1,57,1,58,1,58,1,59,1,59,1,60,1,60,1,60,1,61,1,61,1,61,1,62,1,62,
        1,62,1,62,1,63,1,63,1,64,1,64,1,65,1,65,1,66,1,66,1,67,1,67,1,68,
        1,68,1,69,1,69,1,70,1,70,1,71,1,71,1,72,1,72,5,72,599,8,72,10,72,
        12,72,602,9,72,1,73,4,73,605,8,73,11,73,12,73,606,1,73,1,73,1,74,
        1,74,1,74,1,74,5,74,615,8,74,10,74,12,74,618,9,74,1,74,3,74,621,
        8,74,1,74,1,74,1,74,1,74,1,344,0,75,1,1,3,2,5,3,7,4,9,5,11,6,13,
        0,15,7,17,8,19,9,21,10,23,11,25,12,27,13,29,14,31,15,33,16,35,17,
        37,18,39,19,41,20,43,21,45,22,47,23,49,24,51,25,53,26,55,27,57,28,
        59,29,61,30,63,31,65,32,67,33,69,34,71,35,73,36,75,37,77,38,79,39,
        81,40,83,41,85,42,87,43,89,44,91,45,93,46,95,47,97,48,99,49,101,
        50,103,51,105,52,107,53,109,54,111,55,113,56,115,57,117,58,119,59,
        121,60,123,61,125,62,127,63,129,64,131,65,133,66,135,67,137,68,139,
        69,141,70,143,71,145,72,147,73,149,74,1,0,8,1,0,48,57,2,0,43,43,
        45,45,1,0,49,57,11,0,34,34,39,39,48,48,63,63,92,92,97,98,102,102,
        110,110,114,114,116,116,118,118,3,0,65,90,95,95,97,122,4,0,48,57,
        65,90,95,95,97,122,3,0,9,10,13,13,32,32,2,0,10,10,13,13,636,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,
        0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,
        0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,
        0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,
        0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,
        0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,
        0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,
        113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,
        0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,
        1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,
        0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,
        0,0,0,1,151,1,0,0,0,3,191,1,0,0,0,5,223,1,0,0,0,7,270,1,0,0,0,9,
        308,1,0,0,0,11,319,1,0,0,0,13,334,1,0,0,0,15,336,1,0,0,0,17,340,
        1,0,0,0,19,358,1,0,0,0,21,360,1,0,0,0,23,367,1,0,0,0,25,374,1,0,
        0,0,27,381,1,0,0,0,29,387,1,0,0,0,31,391,1,0,0,0,33,397,1,0,0,0,
        35,402,1,0,0,0,37,407,1,0,0,0,39,414,1,0,0,0,41,420,1,0,0,0,43,423,
        1,0,0,0,45,428,1,0,0,0,47,436,1,0,0,0,49,443,1,0,0,0,51,448,1,0,
        0,0,53,456,1,0,0,0,55,460,1,0,0,0,57,463,1,0,0,0,59,469,1,0,0,0,
        61,475,1,0,0,0,63,484,1,0,0,0,65,491,1,0,0,0,67,496,1,0,0,0,69,503,
        1,0,0,0,71,506,1,0,0,0,73,509,1,0,0,0,75,511,1,0,0,0,77,514,1,0,
        0,0,79,517,1,0,0,0,81,520,1,0,0,0,83,523,1,0,0,0,85,526,1,0,0,0,
        87,529,1,0,0,0,89,532,1,0,0,0,91,534,1,0,0,0,93,536,1,0,0,0,95,538,
        1,0,0,0,97,540,1,0,0,0,99,542,1,0,0,0,101,545,1,0,0,0,103,547,1,
        0,0,0,105,550,1,0,0,0,107,552,1,0,0,0,109,555,1,0,0,0,111,558,1,
        0,0,0,113,560,1,0,0,0,115,562,1,0,0,0,117,564,1,0,0,0,119,566,1,
        0,0,0,121,568,1,0,0,0,123,571,1,0,0,0,125,574,1,0,0,0,127,578,1,
        0,0,0,129,580,1,0,0,0,131,582,1,0,0,0,133,584,1,0,0,0,135,586,1,
        0,0,0,137,588,1,0,0,0,139,590,1,0,0,0,141,592,1,0,0,0,143,594,1,
        0,0,0,145,596,1,0,0,0,147,604,1,0,0,0,149,610,1,0,0,0,151,152,5,
        118,0,0,152,153,5,111,0,0,153,154,5,105,0,0,154,155,5,100,0,0,155,
        156,5,32,0,0,156,157,5,42,0,0,157,158,5,109,0,0,158,159,5,101,0,
        0,159,160,5,109,0,0,160,161,5,115,0,0,161,162,5,101,0,0,162,163,
        5,116,0,0,163,164,5,40,0,0,164,165,5,118,0,0,165,166,5,111,0,0,166,
        167,5,105,0,0,167,168,5,100,0,0,168,169,5,32,0,0,169,170,5,42,0,
        0,170,171,5,115,0,0,171,172,5,44,0,0,172,173,5,32,0,0,173,174,5,
        105,0,0,174,175,5,110,0,0,175,176,5,116,0,0,176,177,5,32,0,0,177,
        178,5,99,0,0,178,179,5,104,0,0,179,180,5,44,0,0,180,181,5,32,0,0,
        181,182,5,115,0,0,182,183,5,105,0,0,183,184,5,122,0,0,184,185,5,
        101,0,0,185,186,5,95,0,0,186,187,5,116,0,0,187,188,5,32,0,0,188,
        189,5,110,0,0,189,190,5,41,0,0,190,2,1,0,0,0,191,192,5,115,0,0,192,
        193,5,105,0,0,193,194,5,122,0,0,194,195,5,101,0,0,195,196,5,95,0,
        0,196,197,5,116,0,0,197,198,5,32,0,0,198,199,5,115,0,0,199,200,5,
        116,0,0,200,201,5,114,0,0,201,202,5,108,0,0,202,203,5,101,0,0,203,
        204,5,110,0,0,204,205,5,40,0,0,205,206,5,99,0,0,206,207,5,111,0,
        0,207,208,5,110,0,0,208,209,5,115,0,0,209,210,5,116,0,0,210,211,
        5,32,0,0,211,212,5,99,0,0,212,213,5,104,0,0,213,214,5,97,0,0,214,
        215,5,114,0,0,215,216,5,32,0,0,216,217,5,42,0,0,217,218,5,95,0,0,
        218,219,5,83,0,0,219,220,5,116,0,0,220,221,5,114,0,0,221,222,5,41,
        0,0,222,4,1,0,0,0,223,224,5,105,0,0,224,225,5,110,0,0,225,226,5,
        116,0,0,226,227,5,32,0,0,227,228,5,112,0,0,228,229,5,114,0,0,229,
        230,5,105,0,0,230,231,5,110,0,0,231,232,5,116,0,0,232,233,5,102,
        0,0,233,234,5,40,0,0,234,235,5,32,0,0,235,236,5,99,0,0,236,237,5,
        111,0,0,237,238,5,110,0,0,238,239,5,115,0,0,239,240,5,116,0,0,240,
        241,5,32,0,0,241,242,5,99,0,0,242,243,5,104,0,0,243,244,5,97,0,0,
        244,245,5,114,0,0,245,246,5,32,0,0,246,247,5,42,0,0,247,248,5,114,
        0,0,248,249,5,101,0,0,249,250,5,115,0,0,250,251,5,116,0,0,251,252,
        5,114,0,0,252,253,5,105,0,0,253,254,5,99,0,0,254,255,5,116,0,0,255,
        256,5,32,0,0,256,257,5,102,0,0,257,258,5,111,0,0,258,259,5,114,0,
        0,259,260,5,109,0,0,260,261,5,97,0,0,261,262,5,116,0,0,262,263,5,
        44,0,0,263,264,5,32,0,0,264,265,5,46,0,0,265,266,5,46,0,0,266,267,
        5,46,0,0,267,268,5,32,0,0,268,269,5,41,0,0,269,6,1,0,0,0,270,271,
        5,105,0,0,271,272,5,110,0,0,272,273,5,116,0,0,273,274,5,32,0,0,274,
        275,5,115,0,0,275,276,5,99,0,0,276,277,5,97,0,0,277,278,5,110,0,
        0,278,279,5,102,0,0,279,280,5,40,0,0,280,281,5,99,0,0,281,282,5,
        111,0,0,282,283,5,110,0,0,283,284,5,115,0,0,284,285,5,116,0,0,285,
        286,5,32,0,0,286,287,5,99,0,0,287,288,5,104,0,0,288,289,5,97,0,0,
        289,290,5,114,0,0,290,291,5,32,0,0,291,292,5,42,0,0,292,293,5,95,
        0,0,293,294,5,95,0,0,294,295,5,102,0,0,295,296,5,111,0,0,296,297,
        5,114,0,0,297,298,5,109,0,0,298,299,5,97,0,0,299,300,5,116,0,0,300,
        301,5,44,0,0,301,302,5,32,0,0,302,303,5,46,0,0,303,304,5,46,0,0,
        304,305,5,46,0,0,305,306,5,41,0,0,306,8,1,0,0,0,307,309,7,0,0,0,
        308,307,1,0,0,0,309,310,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,
        311,312,1,0,0,0,312,314,5,46,0,0,313,315,7,0,0,0,314,313,1,0,0,0,
        315,316,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,10,1,0,0,0,318,
        320,7,1,0,0,319,318,1,0,0,0,319,320,1,0,0,0,320,329,1,0,0,0,321,
        325,7,2,0,0,322,324,7,0,0,0,323,322,1,0,0,0,324,327,1,0,0,0,325,
        323,1,0,0,0,325,326,1,0,0,0,326,330,1,0,0,0,327,325,1,0,0,0,328,
        330,5,48,0,0,329,321,1,0,0,0,329,328,1,0,0,0,330,12,1,0,0,0,331,
        332,5,39,0,0,332,335,7,3,0,0,333,335,9,0,0,0,334,331,1,0,0,0,334,
        333,1,0,0,0,335,14,1,0,0,0,336,337,5,39,0,0,337,338,3,13,6,0,338,
        339,5,39,0,0,339,16,1,0,0,0,340,344,5,34,0,0,341,343,3,13,6,0,342,
        341,1,0,0,0,343,346,1,0,0,0,344,345,1,0,0,0,344,342,1,0,0,0,345,
        347,1,0,0,0,346,344,1,0,0,0,347,348,5,34,0,0,348,18,1,0,0,0,349,
        350,5,116,0,0,350,351,5,114,0,0,351,352,5,117,0,0,352,359,5,101,
        0,0,353,354,5,102,0,0,354,355,5,97,0,0,355,356,5,108,0,0,356,357,
        5,115,0,0,357,359,5,101,0,0,358,349,1,0,0,0,358,353,1,0,0,0,359,
        20,1,0,0,0,360,361,5,109,0,0,361,362,5,101,0,0,362,363,5,109,0,0,
        363,364,5,115,0,0,364,365,5,101,0,0,365,366,5,116,0,0,366,22,1,0,
        0,0,367,368,5,115,0,0,368,369,5,116,0,0,369,370,5,114,0,0,370,371,
        5,108,0,0,371,372,5,101,0,0,372,373,5,110,0,0,373,24,1,0,0,0,374,
        375,5,112,0,0,375,376,5,114,0,0,376,377,5,105,0,0,377,378,5,110,
        0,0,378,379,5,116,0,0,379,380,5,102,0,0,380,26,1,0,0,0,381,382,5,
        115,0,0,382,383,5,99,0,0,383,384,5,97,0,0,384,385,5,110,0,0,385,
        386,5,102,0,0,386,28,1,0,0,0,387,388,5,105,0,0,388,389,5,110,0,0,
        389,390,5,116,0,0,390,30,1,0,0,0,391,392,5,102,0,0,392,393,5,108,
        0,0,393,394,5,111,0,0,394,395,5,97,0,0,395,396,5,116,0,0,396,32,
        1,0,0,0,397,398,5,99,0,0,398,399,5,104,0,0,399,400,5,97,0,0,400,
        401,5,114,0,0,401,34,1,0,0,0,402,403,5,98,0,0,403,404,5,111,0,0,
        404,405,5,111,0,0,405,406,5,108,0,0,406,36,1,0,0,0,407,408,5,115,
        0,0,408,409,5,116,0,0,409,410,5,114,0,0,410,411,5,105,0,0,411,412,
        5,110,0,0,412,413,5,103,0,0,413,38,1,0,0,0,414,415,5,99,0,0,415,
        416,5,111,0,0,416,417,5,110,0,0,417,418,5,115,0,0,418,419,5,116,
        0,0,419,40,1,0,0,0,420,421,5,105,0,0,421,422,5,102,0,0,422,42,1,
        0,0,0,423,424,5,101,0,0,424,425,5,108,0,0,425,426,5,115,0,0,426,
        427,5,101,0,0,427,44,1,0,0,0,428,429,5,101,0,0,429,430,5,108,0,0,
        430,431,5,115,0,0,431,432,5,101,0,0,432,433,5,32,0,0,433,434,5,105,
        0,0,434,435,5,102,0,0,435,46,1,0,0,0,436,437,5,115,0,0,437,438,5,
        119,0,0,438,439,5,105,0,0,439,440,5,116,0,0,440,441,5,99,0,0,441,
        442,5,104,0,0,442,48,1,0,0,0,443,444,5,99,0,0,444,445,5,97,0,0,445,
        446,5,115,0,0,446,447,5,101,0,0,447,50,1,0,0,0,448,449,5,100,0,0,
        449,450,5,101,0,0,450,451,5,102,0,0,451,452,5,97,0,0,452,453,5,117,
        0,0,453,454,5,108,0,0,454,455,5,116,0,0,455,52,1,0,0,0,456,457,5,
        102,0,0,457,458,5,111,0,0,458,459,5,114,0,0,459,54,1,0,0,0,460,461,
        5,100,0,0,461,462,5,111,0,0,462,56,1,0,0,0,463,464,5,119,0,0,464,
        465,5,104,0,0,465,466,5,105,0,0,466,467,5,108,0,0,467,468,5,101,
        0,0,468,58,1,0,0,0,469,470,5,98,0,0,470,471,5,114,0,0,471,472,5,
        101,0,0,472,473,5,97,0,0,473,474,5,107,0,0,474,60,1,0,0,0,475,476,
        5,99,0,0,476,477,5,111,0,0,477,478,5,110,0,0,478,479,5,116,0,0,479,
        480,5,105,0,0,480,481,5,110,0,0,481,482,5,117,0,0,482,483,5,101,
        0,0,483,62,1,0,0,0,484,485,5,114,0,0,485,486,5,101,0,0,486,487,5,
        116,0,0,487,488,5,117,0,0,488,489,5,114,0,0,489,490,5,110,0,0,490,
        64,1,0,0,0,491,492,5,118,0,0,492,493,5,111,0,0,493,494,5,105,0,0,
        494,495,5,100,0,0,495,66,1,0,0,0,496,497,5,115,0,0,497,498,5,116,
        0,0,498,499,5,114,0,0,499,500,5,117,0,0,500,501,5,99,0,0,501,502,
        5,116,0,0,502,68,1,0,0,0,503,504,5,61,0,0,504,505,5,61,0,0,505,70,
        1,0,0,0,506,507,5,33,0,0,507,508,5,61,0,0,508,72,1,0,0,0,509,510,
        5,61,0,0,510,74,1,0,0,0,511,512,5,43,0,0,512,513,5,61,0,0,513,76,
        1,0,0,0,514,515,5,45,0,0,515,516,5,61,0,0,516,78,1,0,0,0,517,518,
        5,42,0,0,518,519,5,61,0,0,519,80,1,0,0,0,520,521,5,47,0,0,521,522,
        5,61,0,0,522,82,1,0,0,0,523,524,5,37,0,0,524,525,5,61,0,0,525,84,
        1,0,0,0,526,527,5,43,0,0,527,528,5,43,0,0,528,86,1,0,0,0,529,530,
        5,45,0,0,530,531,5,45,0,0,531,88,1,0,0,0,532,533,5,43,0,0,533,90,
        1,0,0,0,534,535,5,45,0,0,535,92,1,0,0,0,536,537,5,42,0,0,537,94,
        1,0,0,0,538,539,5,47,0,0,539,96,1,0,0,0,540,541,5,37,0,0,541,98,
        1,0,0,0,542,543,5,62,0,0,543,544,5,61,0,0,544,100,1,0,0,0,545,546,
        5,62,0,0,546,102,1,0,0,0,547,548,5,60,0,0,548,549,5,61,0,0,549,104,
        1,0,0,0,550,551,5,60,0,0,551,106,1,0,0,0,552,553,5,38,0,0,553,554,
        5,38,0,0,554,108,1,0,0,0,555,556,5,124,0,0,556,557,5,124,0,0,557,
        110,1,0,0,0,558,559,5,33,0,0,559,112,1,0,0,0,560,561,5,38,0,0,561,
        114,1,0,0,0,562,563,5,124,0,0,563,116,1,0,0,0,564,565,5,126,0,0,
        565,118,1,0,0,0,566,567,5,94,0,0,567,120,1,0,0,0,568,569,5,60,0,
        0,569,570,5,60,0,0,570,122,1,0,0,0,571,572,5,62,0,0,572,573,5,62,
        0,0,573,124,1,0,0,0,574,575,5,46,0,0,575,576,5,46,0,0,576,577,5,
        46,0,0,577,126,1,0,0,0,578,579,5,59,0,0,579,128,1,0,0,0,580,581,
        5,44,0,0,581,130,1,0,0,0,582,583,5,40,0,0,583,132,1,0,0,0,584,585,
        5,41,0,0,585,134,1,0,0,0,586,587,5,91,0,0,587,136,1,0,0,0,588,589,
        5,93,0,0,589,138,1,0,0,0,590,591,5,123,0,0,591,140,1,0,0,0,592,593,
        5,125,0,0,593,142,1,0,0,0,594,595,5,58,0,0,595,144,1,0,0,0,596,600,
        7,4,0,0,597,599,7,5,0,0,598,597,1,0,0,0,599,602,1,0,0,0,600,598,
        1,0,0,0,600,601,1,0,0,0,601,146,1,0,0,0,602,600,1,0,0,0,603,605,
        7,6,0,0,604,603,1,0,0,0,605,606,1,0,0,0,606,604,1,0,0,0,606,607,
        1,0,0,0,607,608,1,0,0,0,608,609,6,73,0,0,609,148,1,0,0,0,610,611,
        5,47,0,0,611,612,5,47,0,0,612,616,1,0,0,0,613,615,8,7,0,0,614,613,
        1,0,0,0,615,618,1,0,0,0,616,614,1,0,0,0,616,617,1,0,0,0,617,620,
        1,0,0,0,618,616,1,0,0,0,619,621,5,13,0,0,620,619,1,0,0,0,620,621,
        1,0,0,0,621,622,1,0,0,0,622,623,5,10,0,0,623,624,1,0,0,0,624,625,
        6,74,0,0,625,150,1,0,0,0,13,0,310,316,319,325,329,334,344,358,600,
        606,616,620,1,6,0,0
    ]

class CgrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MEMSET = 1
    STRLEN = 2
    PRINTF = 3
    SCANF = 4
    FLOATVALUE = 5
    INTVALUE = 6
    CHARVALUE = 7
    STRINGVALUE = 8
    BOOLVALUE = 9
    MEMSETFUNC = 10
    STRLENFUC = 11
    PRINTFFUNC = 12
    SCANFFUNC = 13
    INT = 14
    FLOAT = 15
    CHAR = 16
    BOOL = 17
    STRING = 18
    CONST = 19
    IF = 20
    ELSE = 21
    ELIF = 22
    SWITCH = 23
    CASE = 24
    DEFAULT = 25
    FOR = 26
    DO = 27
    WHILE = 28
    BREAK = 29
    CONTINUE = 30
    RETURN = 31
    VOID = 32
    STRUCT = 33
    EQUAL = 34
    NOTEQUAL = 35
    ASSIGN = 36
    PLUSASSIGN = 37
    MINUSASSIGN = 38
    MULTIPLYASSIGN = 39
    DIVIDEASSIGN = 40
    MODULOASSIGN = 41
    SELFPLUS = 42
    SELFMINUS = 43
    PLUS = 44
    MINUS = 45
    MULTIPLYorREFERENCEorPTR = 46
    DIVIDE = 47
    MODULO = 48
    GEQUAL = 49
    GREATER = 50
    LEQUAL = 51
    LESS = 52
    AND = 53
    OR = 54
    NOT = 55
    BITANDorADDRESS = 56
    BITOR = 57
    BITNOT = 58
    BITXOR = 59
    LSHIFT = 60
    RSHIFT = 61
    ELLIPSIS = 62
    SEMICOLON = 63
    COMMA = 64
    LROUND = 65
    RROUND = 66
    LSQUARE = 67
    RSQUARE = 68
    LCURLY = 69
    RCURLY = 70
    COLON = 71
    IDENTIFIER = 72
    WS = 73
    COMMENT = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void *memset(void *s, int ch, size_t n)'", "'size_t strlen(const char *_Str)'", 
            "'int printf( const char *restrict format, ... )'", "'int scanf(const char *__format, ...)'", 
            "'memset'", "'strlen'", "'printf'", "'scanf'", "'int'", "'float'", 
            "'char'", "'bool'", "'string'", "'const'", "'if'", "'else'", 
            "'else if'", "'switch'", "'case'", "'default'", "'for'", "'do'", 
            "'while'", "'break'", "'continue'", "'return'", "'void'", "'struct'", 
            "'=='", "'!='", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", "'%'", "'>='", "'>'", 
            "'<='", "'<'", "'&&'", "'||'", "'!'", "'&'", "'|'", "'~'", "'^'", 
            "'<<'", "'>>'", "'...'", "';'", "','", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "MEMSET", "STRLEN", "PRINTF", "SCANF", "FLOATVALUE", "INTVALUE", 
            "CHARVALUE", "STRINGVALUE", "BOOLVALUE", "MEMSETFUNC", "STRLENFUC", 
            "PRINTFFUNC", "SCANFFUNC", "INT", "FLOAT", "CHAR", "BOOL", "STRING", 
            "CONST", "IF", "ELSE", "ELIF", "SWITCH", "CASE", "DEFAULT", 
            "FOR", "DO", "WHILE", "BREAK", "CONTINUE", "RETURN", "VOID", 
            "STRUCT", "EQUAL", "NOTEQUAL", "ASSIGN", "PLUSASSIGN", "MINUSASSIGN", 
            "MULTIPLYASSIGN", "DIVIDEASSIGN", "MODULOASSIGN", "SELFPLUS", 
            "SELFMINUS", "PLUS", "MINUS", "MULTIPLYorREFERENCEorPTR", "DIVIDE", 
            "MODULO", "GEQUAL", "GREATER", "LEQUAL", "LESS", "AND", "OR", 
            "NOT", "BITANDorADDRESS", "BITOR", "BITNOT", "BITXOR", "LSHIFT", 
            "RSHIFT", "ELLIPSIS", "SEMICOLON", "COMMA", "LROUND", "RROUND", 
            "LSQUARE", "RSQUARE", "LCURLY", "RCURLY", "COLON", "IDENTIFIER", 
            "WS", "COMMENT" ]

    ruleNames = [ "MEMSET", "STRLEN", "PRINTF", "SCANF", "FLOATVALUE", "INTVALUE", 
                  "CHARCONTENT", "CHARVALUE", "STRINGVALUE", "BOOLVALUE", 
                  "MEMSETFUNC", "STRLENFUC", "PRINTFFUNC", "SCANFFUNC", 
                  "INT", "FLOAT", "CHAR", "BOOL", "STRING", "CONST", "IF", 
                  "ELSE", "ELIF", "SWITCH", "CASE", "DEFAULT", "FOR", "DO", 
                  "WHILE", "BREAK", "CONTINUE", "RETURN", "VOID", "STRUCT", 
                  "EQUAL", "NOTEQUAL", "ASSIGN", "PLUSASSIGN", "MINUSASSIGN", 
                  "MULTIPLYASSIGN", "DIVIDEASSIGN", "MODULOASSIGN", "SELFPLUS", 
                  "SELFMINUS", "PLUS", "MINUS", "MULTIPLYorREFERENCEorPTR", 
                  "DIVIDE", "MODULO", "GEQUAL", "GREATER", "LEQUAL", "LESS", 
                  "AND", "OR", "NOT", "BITANDorADDRESS", "BITOR", "BITNOT", 
                  "BITXOR", "LSHIFT", "RSHIFT", "ELLIPSIS", "SEMICOLON", 
                  "COMMA", "LROUND", "RROUND", "LSQUARE", "RSQUARE", "LCURLY", 
                  "RCURLY", "COLON", "IDENTIFIER", "WS", "COMMENT" ]

    grammarFileName = "Cgrammer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


