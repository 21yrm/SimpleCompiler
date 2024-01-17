# Generated from Cgrammer.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,73,450,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,1,0,1,0,1,0,3,0,85,8,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,93,8,2,1,
        3,1,3,1,3,1,3,3,3,99,8,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,107,8,4,1,5,
        1,5,1,5,3,5,112,8,5,1,6,3,6,115,8,6,1,6,1,6,3,6,119,8,6,1,6,1,6,
        3,6,123,8,6,1,6,1,6,3,6,127,8,6,5,6,129,8,6,10,6,12,6,132,9,6,1,
        7,1,7,1,7,5,7,137,8,7,10,7,12,7,140,9,7,1,8,1,8,3,8,144,8,8,1,8,
        1,8,3,8,148,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,159,8,9,
        1,10,1,10,1,10,1,10,1,10,3,10,166,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,178,8,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        197,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,211,8,13,10,13,12,13,214,9,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,5,14,225,8,14,10,14,12,14,228,9,14,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,239,8,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,258,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        5,17,269,8,17,10,17,12,17,272,9,17,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,1,19,3,19,282,8,19,1,20,1,20,5,20,286,8,20,10,20,12,20,289,
        9,20,1,20,1,20,1,20,1,21,1,21,3,21,296,8,21,1,21,1,21,1,21,5,21,
        301,8,21,10,21,12,21,304,9,21,1,22,1,22,1,22,1,22,3,22,310,8,22,
        1,23,1,23,3,23,314,8,23,1,23,1,23,1,23,3,23,319,8,23,1,23,1,23,1,
        23,1,23,1,23,1,24,1,24,1,25,1,25,5,25,330,8,25,10,25,12,25,333,9,
        25,1,25,3,25,336,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,
        27,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,
        31,3,31,373,8,31,1,32,1,32,3,32,377,8,32,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,4,33,389,8,33,11,33,12,33,390,1,33,1,33,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,404,8,34,3,34,
        406,8,34,1,35,3,35,409,8,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,3,
        36,418,8,36,1,37,1,37,1,37,1,37,1,37,3,37,425,8,37,1,38,5,38,428,
        8,38,10,38,12,38,431,9,38,1,39,1,39,1,39,3,39,436,8,39,1,39,1,39,
        5,39,440,8,39,10,39,12,39,443,9,39,1,39,4,39,446,8,39,11,39,12,39,
        447,1,39,0,3,26,28,34,40,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,0,0,498,0,84,1,0,0,0,2,86,1,0,0,0,4,92,1,0,0,0,6,94,1,0,
        0,0,8,106,1,0,0,0,10,108,1,0,0,0,12,114,1,0,0,0,14,133,1,0,0,0,16,
        143,1,0,0,0,18,158,1,0,0,0,20,165,1,0,0,0,22,177,1,0,0,0,24,196,
        1,0,0,0,26,198,1,0,0,0,28,215,1,0,0,0,30,238,1,0,0,0,32,257,1,0,
        0,0,34,259,1,0,0,0,36,273,1,0,0,0,38,281,1,0,0,0,40,283,1,0,0,0,
        42,295,1,0,0,0,44,309,1,0,0,0,46,313,1,0,0,0,48,325,1,0,0,0,50,327,
        1,0,0,0,52,337,1,0,0,0,54,343,1,0,0,0,56,349,1,0,0,0,58,352,1,0,
        0,0,60,358,1,0,0,0,62,372,1,0,0,0,64,376,1,0,0,0,66,378,1,0,0,0,
        68,405,1,0,0,0,70,408,1,0,0,0,72,417,1,0,0,0,74,424,1,0,0,0,76,429,
        1,0,0,0,78,441,1,0,0,0,80,85,5,14,0,0,81,85,5,15,0,0,82,85,5,16,
        0,0,83,85,5,17,0,0,84,80,1,0,0,0,84,81,1,0,0,0,84,82,1,0,0,0,84,
        83,1,0,0,0,85,1,1,0,0,0,86,87,5,45,0,0,87,3,1,0,0,0,88,93,3,0,0,
        0,89,90,3,0,0,0,90,91,3,2,1,0,91,93,1,0,0,0,92,88,1,0,0,0,92,89,
        1,0,0,0,93,5,1,0,0,0,94,98,5,66,0,0,95,99,3,18,9,0,96,99,3,36,18,
        0,97,99,3,16,8,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,100,
        1,0,0,0,100,101,5,67,0,0,101,7,1,0,0,0,102,107,5,10,0,0,103,107,
        5,11,0,0,104,107,5,12,0,0,105,107,5,13,0,0,106,102,1,0,0,0,106,103,
        1,0,0,0,106,104,1,0,0,0,106,105,1,0,0,0,107,9,1,0,0,0,108,109,3,
        4,2,0,109,111,5,71,0,0,110,112,3,6,3,0,111,110,1,0,0,0,111,112,1,
        0,0,0,112,11,1,0,0,0,113,115,5,55,0,0,114,113,1,0,0,0,114,115,1,
        0,0,0,115,118,1,0,0,0,116,119,3,36,18,0,117,119,5,71,0,0,118,116,
        1,0,0,0,118,117,1,0,0,0,119,130,1,0,0,0,120,122,5,63,0,0,121,123,
        5,55,0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,126,1,0,0,0,124,127,
        3,36,18,0,125,127,5,71,0,0,126,124,1,0,0,0,126,125,1,0,0,0,127,129,
        1,0,0,0,128,120,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,13,1,0,0,0,132,130,1,0,0,0,133,138,3,10,5,0,134,135,
        5,63,0,0,135,137,3,10,5,0,136,134,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,15,1,0,0,0,140,138,1,0,0,0,141,144,5,
        71,0,0,142,144,3,8,4,0,143,141,1,0,0,0,143,142,1,0,0,0,144,145,1,
        0,0,0,145,147,5,64,0,0,146,148,3,12,6,0,147,146,1,0,0,0,147,148,
        1,0,0,0,148,149,1,0,0,0,149,150,5,65,0,0,150,17,1,0,0,0,151,159,
        5,71,0,0,152,159,5,6,0,0,153,159,5,5,0,0,154,159,5,7,0,0,155,159,
        5,8,0,0,156,159,5,9,0,0,157,159,3,16,8,0,158,151,1,0,0,0,158,152,
        1,0,0,0,158,153,1,0,0,0,158,154,1,0,0,0,158,155,1,0,0,0,158,156,
        1,0,0,0,158,157,1,0,0,0,159,19,1,0,0,0,160,161,5,64,0,0,161,162,
        3,36,18,0,162,163,5,65,0,0,163,166,1,0,0,0,164,166,3,18,9,0,165,
        160,1,0,0,0,165,164,1,0,0,0,166,21,1,0,0,0,167,168,5,45,0,0,168,
        178,3,20,10,0,169,170,5,55,0,0,170,178,3,20,10,0,171,172,3,20,10,
        0,172,173,5,66,0,0,173,174,3,36,18,0,174,175,5,67,0,0,175,178,1,
        0,0,0,176,178,3,20,10,0,177,167,1,0,0,0,177,169,1,0,0,0,177,171,
        1,0,0,0,177,176,1,0,0,0,178,23,1,0,0,0,179,180,5,41,0,0,180,197,
        3,22,11,0,181,182,3,22,11,0,182,183,5,41,0,0,183,197,1,0,0,0,184,
        185,5,42,0,0,185,197,3,22,11,0,186,187,3,22,11,0,187,188,5,42,0,
        0,188,197,1,0,0,0,189,190,5,54,0,0,190,197,3,22,11,0,191,192,5,43,
        0,0,192,197,3,22,11,0,193,194,5,44,0,0,194,197,3,22,11,0,195,197,
        3,22,11,0,196,179,1,0,0,0,196,181,1,0,0,0,196,184,1,0,0,0,196,186,
        1,0,0,0,196,189,1,0,0,0,196,191,1,0,0,0,196,193,1,0,0,0,196,195,
        1,0,0,0,197,25,1,0,0,0,198,199,6,13,-1,0,199,200,3,24,12,0,200,212,
        1,0,0,0,201,202,10,4,0,0,202,203,5,45,0,0,203,211,3,24,12,0,204,
        205,10,3,0,0,205,206,5,46,0,0,206,211,3,24,12,0,207,208,10,2,0,0,
        208,209,5,47,0,0,209,211,3,24,12,0,210,201,1,0,0,0,210,204,1,0,0,
        0,210,207,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,
        0,213,27,1,0,0,0,214,212,1,0,0,0,215,216,6,14,-1,0,216,217,3,26,
        13,0,217,226,1,0,0,0,218,219,10,3,0,0,219,220,5,43,0,0,220,225,3,
        26,13,0,221,222,10,2,0,0,222,223,5,44,0,0,223,225,3,26,13,0,224,
        218,1,0,0,0,224,221,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,
        227,1,0,0,0,227,29,1,0,0,0,228,226,1,0,0,0,229,230,3,28,14,0,230,
        231,5,33,0,0,231,232,3,28,14,0,232,239,1,0,0,0,233,234,3,28,14,0,
        234,235,5,34,0,0,235,236,3,28,14,0,236,239,1,0,0,0,237,239,3,28,
        14,0,238,229,1,0,0,0,238,233,1,0,0,0,238,237,1,0,0,0,239,31,1,0,
        0,0,240,241,3,30,15,0,241,242,5,49,0,0,242,243,3,30,15,0,243,258,
        1,0,0,0,244,245,3,30,15,0,245,246,5,48,0,0,246,247,3,30,15,0,247,
        258,1,0,0,0,248,249,3,30,15,0,249,250,5,51,0,0,250,251,3,30,15,0,
        251,258,1,0,0,0,252,253,3,30,15,0,253,254,5,50,0,0,254,255,3,30,
        15,0,255,258,1,0,0,0,256,258,3,30,15,0,257,240,1,0,0,0,257,244,1,
        0,0,0,257,248,1,0,0,0,257,252,1,0,0,0,257,256,1,0,0,0,258,33,1,0,
        0,0,259,260,6,17,-1,0,260,261,3,32,16,0,261,270,1,0,0,0,262,263,
        10,3,0,0,263,264,5,52,0,0,264,269,3,32,16,0,265,266,10,2,0,0,266,
        267,5,53,0,0,267,269,3,32,16,0,268,262,1,0,0,0,268,265,1,0,0,0,269,
        272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,35,1,0,0,0,272,270,
        1,0,0,0,273,274,3,34,17,0,274,37,1,0,0,0,275,282,5,35,0,0,276,282,
        5,36,0,0,277,282,5,37,0,0,278,282,5,38,0,0,279,282,5,39,0,0,280,
        282,5,40,0,0,281,275,1,0,0,0,281,276,1,0,0,0,281,277,1,0,0,0,281,
        278,1,0,0,0,281,279,1,0,0,0,281,280,1,0,0,0,282,39,1,0,0,0,283,287,
        5,71,0,0,284,286,3,6,3,0,285,284,1,0,0,0,286,289,1,0,0,0,287,285,
        1,0,0,0,287,288,1,0,0,0,288,290,1,0,0,0,289,287,1,0,0,0,290,291,
        3,38,19,0,291,292,3,36,18,0,292,41,1,0,0,0,293,296,3,4,2,0,294,296,
        5,31,0,0,295,293,1,0,0,0,295,294,1,0,0,0,296,297,1,0,0,0,297,302,
        3,40,20,0,298,299,5,63,0,0,299,301,3,40,20,0,300,298,1,0,0,0,301,
        304,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,43,1,0,0,0,304,302,
        1,0,0,0,305,310,5,1,0,0,306,310,5,2,0,0,307,310,5,3,0,0,308,310,
        5,4,0,0,309,305,1,0,0,0,309,306,1,0,0,0,309,307,1,0,0,0,309,308,
        1,0,0,0,310,45,1,0,0,0,311,314,3,4,2,0,312,314,5,31,0,0,313,311,
        1,0,0,0,313,312,1,0,0,0,314,315,1,0,0,0,315,316,5,71,0,0,316,318,
        5,64,0,0,317,319,3,14,7,0,318,317,1,0,0,0,318,319,1,0,0,0,319,320,
        1,0,0,0,320,321,5,65,0,0,321,322,5,68,0,0,322,323,3,76,38,0,323,
        324,5,69,0,0,324,47,1,0,0,0,325,326,3,36,18,0,326,49,1,0,0,0,327,
        331,3,52,26,0,328,330,3,54,27,0,329,328,1,0,0,0,330,333,1,0,0,0,
        331,329,1,0,0,0,331,332,1,0,0,0,332,335,1,0,0,0,333,331,1,0,0,0,
        334,336,3,56,28,0,335,334,1,0,0,0,335,336,1,0,0,0,336,51,1,0,0,0,
        337,338,5,19,0,0,338,339,5,64,0,0,339,340,3,48,24,0,340,341,5,65,
        0,0,341,342,3,74,37,0,342,53,1,0,0,0,343,344,5,21,0,0,344,345,5,
        64,0,0,345,346,3,48,24,0,346,347,5,65,0,0,347,348,3,74,37,0,348,
        55,1,0,0,0,349,350,5,20,0,0,350,351,3,74,37,0,351,57,1,0,0,0,352,
        353,5,27,0,0,353,354,5,64,0,0,354,355,3,48,24,0,355,356,5,65,0,0,
        356,357,3,74,37,0,357,59,1,0,0,0,358,359,5,25,0,0,359,360,5,64,0,
        0,360,361,3,62,31,0,361,362,5,62,0,0,362,363,3,48,24,0,363,364,5,
        62,0,0,364,365,3,64,32,0,365,366,5,65,0,0,366,367,3,74,37,0,367,
        61,1,0,0,0,368,373,3,10,5,0,369,373,3,42,21,0,370,373,3,40,20,0,
        371,373,3,36,18,0,372,368,1,0,0,0,372,369,1,0,0,0,372,370,1,0,0,
        0,372,371,1,0,0,0,372,373,1,0,0,0,373,63,1,0,0,0,374,377,3,40,20,
        0,375,377,3,36,18,0,376,374,1,0,0,0,376,375,1,0,0,0,376,377,1,0,
        0,0,377,65,1,0,0,0,378,379,5,22,0,0,379,380,5,64,0,0,380,381,3,36,
        18,0,381,382,5,65,0,0,382,388,5,68,0,0,383,384,5,23,0,0,384,385,
        3,18,9,0,385,386,5,70,0,0,386,387,3,76,38,0,387,389,1,0,0,0,388,
        383,1,0,0,0,389,390,1,0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,
        392,1,0,0,0,392,393,5,69,0,0,393,67,1,0,0,0,394,406,3,10,5,0,395,
        406,3,42,21,0,396,406,3,40,20,0,397,406,3,36,18,0,398,406,3,44,22,
        0,399,406,5,28,0,0,400,406,5,29,0,0,401,403,5,30,0,0,402,404,3,36,
        18,0,403,402,1,0,0,0,403,404,1,0,0,0,404,406,1,0,0,0,405,394,1,0,
        0,0,405,395,1,0,0,0,405,396,1,0,0,0,405,397,1,0,0,0,405,398,1,0,
        0,0,405,399,1,0,0,0,405,400,1,0,0,0,405,401,1,0,0,0,406,69,1,0,0,
        0,407,409,3,68,34,0,408,407,1,0,0,0,408,409,1,0,0,0,409,410,1,0,
        0,0,410,411,5,62,0,0,411,71,1,0,0,0,412,418,3,50,25,0,413,418,3,
        58,29,0,414,418,3,60,30,0,415,418,3,66,33,0,416,418,3,70,35,0,417,
        412,1,0,0,0,417,413,1,0,0,0,417,414,1,0,0,0,417,415,1,0,0,0,417,
        416,1,0,0,0,418,73,1,0,0,0,419,425,3,76,38,0,420,421,5,68,0,0,421,
        422,3,76,38,0,422,423,5,69,0,0,423,425,1,0,0,0,424,419,1,0,0,0,424,
        420,1,0,0,0,425,75,1,0,0,0,426,428,3,72,36,0,427,426,1,0,0,0,428,
        431,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,77,1,0,0,0,431,429,
        1,0,0,0,432,436,3,44,22,0,433,436,3,10,5,0,434,436,3,42,21,0,435,
        432,1,0,0,0,435,433,1,0,0,0,435,434,1,0,0,0,436,437,1,0,0,0,437,
        438,5,62,0,0,438,440,1,0,0,0,439,435,1,0,0,0,440,443,1,0,0,0,441,
        439,1,0,0,0,441,442,1,0,0,0,442,445,1,0,0,0,443,441,1,0,0,0,444,
        446,3,46,23,0,445,444,1,0,0,0,446,447,1,0,0,0,447,445,1,0,0,0,447,
        448,1,0,0,0,448,79,1,0,0,0,46,84,92,98,106,111,114,118,122,126,130,
        138,143,147,158,165,177,196,210,212,224,226,238,257,268,270,281,
        287,295,302,309,313,318,331,335,372,376,390,403,405,408,417,424,
        429,435,441,447
    ]

class CgrammerParser ( Parser ):

    grammarFileName = "Cgrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'void *memset(void *s, int ch, size_t n)'", 
                     "'size_t strlen(const char *_Str)'", "'int printf( const char *restrict format, ... )'", 
                     "'int scanf(const char *__format, ...)'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'memset'", "'strlen'", "'printf'", "'scanf'", "'int'", 
                     "'float'", "'char'", "'bool'", "'const'", "'if'", "'else'", 
                     "'else if'", "'switch'", "'case'", "'default'", "'for'", 
                     "'do'", "'while'", "'break'", "'continue'", "'return'", 
                     "'void'", "'struct'", "'=='", "'!='", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'++'", "'--'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'>='", "'>'", "'<='", 
                     "'<'", "'&&'", "'||'", "'!'", "'&'", "'|'", "'~'", 
                     "'^'", "'<<'", "'>>'", "'...'", "';'", "','", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "':'" ]

    symbolicNames = [ "<INVALID>", "MEMSET", "STRLEN", "PRINTF", "SCANF", 
                      "FLOATVALUE", "INTVALUE", "CHARVALUE", "STRINGVALUE", 
                      "BOOLVALUE", "MEMSETFUNC", "STRLENFUC", "PRINTFFUNC", 
                      "SCANFFUNC", "INT", "FLOAT", "CHAR", "BOOL", "CONST", 
                      "IF", "ELSE", "ELIF", "SWITCH", "CASE", "DEFAULT", 
                      "FOR", "DO", "WHILE", "BREAK", "CONTINUE", "RETURN", 
                      "VOID", "STRUCT", "EQUAL", "NOTEQUAL", "ASSIGN", "PLUSASSIGN", 
                      "MINUSASSIGN", "MULTIPLYASSIGN", "DIVIDEASSIGN", "MODULOASSIGN", 
                      "SELFPLUS", "SELFMINUS", "PLUS", "MINUS", "MULTIPLYorREFERENCEorPTR", 
                      "DIVIDE", "MODULO", "GEQUAL", "GREATER", "LEQUAL", 
                      "LESS", "AND", "OR", "NOT", "BITANDorADDRESS", "BITOR", 
                      "BITNOT", "BITXOR", "LSHIFT", "RSHIFT", "ELLIPSIS", 
                      "SEMICOLON", "COMMA", "LROUND", "RROUND", "LSQUARE", 
                      "RSQUARE", "LCURLY", "RCURLY", "COLON", "IDENTIFIER", 
                      "WS", "COMMENT" ]

    RULE_announcer = 0
    RULE_pointer_flag = 1
    RULE_type = 2
    RULE_index = 3
    RULE_lib_function = 4
    RULE_variable_declaration = 5
    RULE_params = 6
    RULE_params_definition = 7
    RULE_function_call = 8
    RULE_value = 9
    RULE_expr_unit = 10
    RULE_expr_addr = 11
    RULE_expr_unary = 12
    RULE_expr_calc1 = 13
    RULE_expr_calc2 = 14
    RULE_expr_rop1 = 15
    RULE_expr_rop2 = 16
    RULE_expr_logic = 17
    RULE_expression = 18
    RULE_assignment_operator = 19
    RULE_assignment = 20
    RULE_variable_definition = 21
    RULE_lib_announce = 22
    RULE_function_definition = 23
    RULE_condition = 24
    RULE_if_block = 25
    RULE_pure_if_block = 26
    RULE_elif_block = 27
    RULE_else_block = 28
    RULE_while_block = 29
    RULE_for_block = 30
    RULE_for_var = 31
    RULE_for_iter = 32
    RULE_switch_block = 33
    RULE_statement = 34
    RULE_line = 35
    RULE_block = 36
    RULE_code_with_domain = 37
    RULE_code = 38
    RULE_program = 39

    ruleNames =  [ "announcer", "pointer_flag", "type", "index", "lib_function", 
                   "variable_declaration", "params", "params_definition", 
                   "function_call", "value", "expr_unit", "expr_addr", "expr_unary", 
                   "expr_calc1", "expr_calc2", "expr_rop1", "expr_rop2", 
                   "expr_logic", "expression", "assignment_operator", "assignment", 
                   "variable_definition", "lib_announce", "function_definition", 
                   "condition", "if_block", "pure_if_block", "elif_block", 
                   "else_block", "while_block", "for_block", "for_var", 
                   "for_iter", "switch_block", "statement", "line", "block", 
                   "code_with_domain", "code", "program" ]

    EOF = Token.EOF
    MEMSET=1
    STRLEN=2
    PRINTF=3
    SCANF=4
    FLOATVALUE=5
    INTVALUE=6
    CHARVALUE=7
    STRINGVALUE=8
    BOOLVALUE=9
    MEMSETFUNC=10
    STRLENFUC=11
    PRINTFFUNC=12
    SCANFFUNC=13
    INT=14
    FLOAT=15
    CHAR=16
    BOOL=17
    CONST=18
    IF=19
    ELSE=20
    ELIF=21
    SWITCH=22
    CASE=23
    DEFAULT=24
    FOR=25
    DO=26
    WHILE=27
    BREAK=28
    CONTINUE=29
    RETURN=30
    VOID=31
    STRUCT=32
    EQUAL=33
    NOTEQUAL=34
    ASSIGN=35
    PLUSASSIGN=36
    MINUSASSIGN=37
    MULTIPLYASSIGN=38
    DIVIDEASSIGN=39
    MODULOASSIGN=40
    SELFPLUS=41
    SELFMINUS=42
    PLUS=43
    MINUS=44
    MULTIPLYorREFERENCEorPTR=45
    DIVIDE=46
    MODULO=47
    GEQUAL=48
    GREATER=49
    LEQUAL=50
    LESS=51
    AND=52
    OR=53
    NOT=54
    BITANDorADDRESS=55
    BITOR=56
    BITNOT=57
    BITXOR=58
    LSHIFT=59
    RSHIFT=60
    ELLIPSIS=61
    SEMICOLON=62
    COMMA=63
    LROUND=64
    RROUND=65
    LSQUARE=66
    RSQUARE=67
    LCURLY=68
    RCURLY=69
    COLON=70
    IDENTIFIER=71
    WS=72
    COMMENT=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AnnouncerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_announcer

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolContext(AnnouncerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.AnnouncerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(CgrammerParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class CharContext(AnnouncerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.AnnouncerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(CgrammerParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar" ):
                return visitor.visitChar(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(AnnouncerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.AnnouncerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(CgrammerParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(AnnouncerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.AnnouncerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CgrammerParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def announcer(self):

        localctx = CgrammerParser.AnnouncerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_announcer)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = CgrammerParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(CgrammerParser.INT)
                pass
            elif token in [15]:
                localctx = CgrammerParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(CgrammerParser.FLOAT)
                pass
            elif token in [16]:
                localctx = CgrammerParser.CharContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.match(CgrammerParser.CHAR)
                pass
            elif token in [17]:
                localctx = CgrammerParser.BoolContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.match(CgrammerParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pointer_flagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLYorREFERENCEorPTR(self):
            return self.getToken(CgrammerParser.MULTIPLYorREFERENCEorPTR, 0)

        def getRuleIndex(self):
            return CgrammerParser.RULE_pointer_flag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer_flag" ):
                listener.enterPointer_flag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer_flag" ):
                listener.exitPointer_flag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer_flag" ):
                return visitor.visitPointer_flag(self)
            else:
                return visitor.visitChildren(self)




    def pointer_flag(self):

        localctx = CgrammerParser.Pointer_flagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pointer_flag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(CgrammerParser.MULTIPLYorREFERENCEorPTR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PointerContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def announcer(self):
            return self.getTypedRuleContext(CgrammerParser.AnnouncerContext,0)

        def pointer_flag(self):
            return self.getTypedRuleContext(CgrammerParser.Pointer_flagContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer" ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer" ):
                listener.exitPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)


    class OriginalTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def announcer(self):
            return self.getTypedRuleContext(CgrammerParser.AnnouncerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOriginalType" ):
                listener.enterOriginalType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOriginalType" ):
                listener.exitOriginalType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOriginalType" ):
                return visitor.visitOriginalType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = CgrammerParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CgrammerParser.OriginalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.announcer()
                pass

            elif la_ == 2:
                localctx = CgrammerParser.PointerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.announcer()
                self.state = 90
                self.pointer_flag()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(CgrammerParser.LSQUARE, 0)

        def RSQUARE(self):
            return self.getToken(CgrammerParser.RSQUARE, 0)

        def value(self):
            return self.getTypedRuleContext(CgrammerParser.ValueContext,0)


        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def function_call(self):
            return self.getTypedRuleContext(CgrammerParser.Function_callContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = CgrammerParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(CgrammerParser.LSQUARE)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 95
                self.value()
                pass

            elif la_ == 2:
                self.state = 96
                self.expression()
                pass

            elif la_ == 3:
                self.state = 97
                self.function_call()
                pass


            self.state = 100
            self.match(CgrammerParser.RSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lib_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_lib_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StrlenContext(Lib_functionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_functionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRLENFUC(self):
            return self.getToken(CgrammerParser.STRLENFUC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrlen" ):
                listener.enterStrlen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrlen" ):
                listener.exitStrlen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrlen" ):
                return visitor.visitStrlen(self)
            else:
                return visitor.visitChildren(self)


    class ScanfContext(Lib_functionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_functionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCANFFUNC(self):
            return self.getToken(CgrammerParser.SCANFFUNC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanf" ):
                listener.enterScanf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanf" ):
                listener.exitScanf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanf" ):
                return visitor.visitScanf(self)
            else:
                return visitor.visitChildren(self)


    class MemsetContext(Lib_functionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_functionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MEMSETFUNC(self):
            return self.getToken(CgrammerParser.MEMSETFUNC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemset" ):
                listener.enterMemset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemset" ):
                listener.exitMemset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemset" ):
                return visitor.visitMemset(self)
            else:
                return visitor.visitChildren(self)


    class PrintfContext(Lib_functionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_functionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINTFFUNC(self):
            return self.getToken(CgrammerParser.PRINTFFUNC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf" ):
                listener.enterPrintf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf" ):
                listener.exitPrintf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf" ):
                return visitor.visitPrintf(self)
            else:
                return visitor.visitChildren(self)



    def lib_function(self):

        localctx = CgrammerParser.Lib_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lib_function)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = CgrammerParser.MemsetContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(CgrammerParser.MEMSETFUNC)
                pass
            elif token in [11]:
                localctx = CgrammerParser.StrlenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(CgrammerParser.STRLENFUC)
                pass
            elif token in [12]:
                localctx = CgrammerParser.PrintfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(CgrammerParser.PRINTFFUNC)
                pass
            elif token in [13]:
                localctx = CgrammerParser.ScanfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.match(CgrammerParser.SCANFFUNC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CgrammerParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(CgrammerParser.IDENTIFIER, 0)

        def index(self):
            return self.getTypedRuleContext(CgrammerParser.IndexContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = CgrammerParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.type_()
            self.state = 109
            self.match(CgrammerParser.IDENTIFIER)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 110
                self.index()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.ExpressionContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.IDENTIFIER)
            else:
                return self.getToken(CgrammerParser.IDENTIFIER, i)

        def BITANDorADDRESS(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.BITANDorADDRESS)
            else:
                return self.getToken(CgrammerParser.BITANDorADDRESS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.COMMA)
            else:
                return self.getToken(CgrammerParser.COMMA, i)

        def getRuleIndex(self):
            return CgrammerParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = CgrammerParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 113
                self.match(CgrammerParser.BITANDorADDRESS)


            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 116
                self.expression()
                pass

            elif la_ == 2:
                self.state = 117
                self.match(CgrammerParser.IDENTIFIER)
                pass


            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 120
                self.match(CgrammerParser.COMMA)
                self.state = 122
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 121
                    self.match(CgrammerParser.BITANDorADDRESS)


                self.state = 126
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 124
                    self.expression()
                    pass

                elif la_ == 2:
                    self.state = 125
                    self.match(CgrammerParser.IDENTIFIER)
                    pass


                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.Variable_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.COMMA)
            else:
                return self.getToken(CgrammerParser.COMMA, i)

        def getRuleIndex(self):
            return CgrammerParser.RULE_params_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_definition" ):
                listener.enterParams_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_definition" ):
                listener.exitParams_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_definition" ):
                return visitor.visitParams_definition(self)
            else:
                return visitor.visitChildren(self)




    def params_definition(self):

        localctx = CgrammerParser.Params_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.variable_declaration()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 134
                self.match(CgrammerParser.COMMA)
                self.state = 135
                self.variable_declaration()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)

        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def IDENTIFIER(self):
            return self.getToken(CgrammerParser.IDENTIFIER, 0)

        def lib_function(self):
            return self.getTypedRuleContext(CgrammerParser.Lib_functionContext,0)


        def params(self):
            return self.getTypedRuleContext(CgrammerParser.ParamsContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = CgrammerParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [71]:
                self.state = 141
                self.match(CgrammerParser.IDENTIFIER)
                pass
            elif token in [10, 11, 12, 13]:
                self.state = 142
                self.lib_function()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 145
            self.match(CgrammerParser.LROUND)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 54111365249384416) != 0) or _la==64 or _la==71:
                self.state = 146
                self.params()


            self.state = 149
            self.match(CgrammerParser.RROUND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class String_valueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRINGVALUE(self):
            return self.getToken(CgrammerParser.STRINGVALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_value" ):
                listener.enterString_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_value" ):
                listener.exitString_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_value" ):
                return visitor.visitString_value(self)
            else:
                return visitor.visitChildren(self)


    class Function_call_Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_call(self):
            return self.getTypedRuleContext(CgrammerParser.Function_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_" ):
                listener.enterFunction_call_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_" ):
                listener.exitFunction_call_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_" ):
                return visitor.visitFunction_call_(self)
            else:
                return visitor.visitChildren(self)


    class Bool_valueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLVALUE(self):
            return self.getToken(CgrammerParser.BOOLVALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_value" ):
                listener.enterBool_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_value" ):
                listener.exitBool_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_value" ):
                return visitor.visitBool_value(self)
            else:
                return visitor.visitChildren(self)


    class Float_valueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOATVALUE(self):
            return self.getToken(CgrammerParser.FLOATVALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_value" ):
                listener.enterFloat_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_value" ):
                listener.exitFloat_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_value" ):
                return visitor.visitFloat_value(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(CgrammerParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class Char_valueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHARVALUE(self):
            return self.getToken(CgrammerParser.CHARVALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar_value" ):
                listener.enterChar_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar_value" ):
                listener.exitChar_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar_value" ):
                return visitor.visitChar_value(self)
            else:
                return visitor.visitChildren(self)


    class Int_valueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTVALUE(self):
            return self.getToken(CgrammerParser.INTVALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_value" ):
                listener.enterInt_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_value" ):
                listener.exitInt_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_value" ):
                return visitor.visitInt_value(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = CgrammerParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = CgrammerParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(CgrammerParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = CgrammerParser.Int_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(CgrammerParser.INTVALUE)
                pass

            elif la_ == 3:
                localctx = CgrammerParser.Float_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(CgrammerParser.FLOATVALUE)
                pass

            elif la_ == 4:
                localctx = CgrammerParser.Char_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.match(CgrammerParser.CHARVALUE)
                pass

            elif la_ == 5:
                localctx = CgrammerParser.String_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.match(CgrammerParser.STRINGVALUE)
                pass

            elif la_ == 6:
                localctx = CgrammerParser.Bool_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.match(CgrammerParser.BOOLVALUE)
                pass

            elif la_ == 7:
                localctx = CgrammerParser.Function_call_Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 157
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_unit

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RoundContext(Expr_unitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)
        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)

        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRound" ):
                listener.enterRound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRound" ):
                listener.exitRound(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRound" ):
                return visitor.visitRound(self)
            else:
                return visitor.visitChildren(self)


    class Expr_valueContext(Expr_unitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(CgrammerParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_value" ):
                listener.enterExpr_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_value" ):
                listener.exitExpr_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_value" ):
                return visitor.visitExpr_value(self)
            else:
                return visitor.visitChildren(self)



    def expr_unit(self):

        localctx = CgrammerParser.Expr_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_unit)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                localctx = CgrammerParser.RoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(CgrammerParser.LROUND)
                self.state = 161
                self.expression()
                self.state = 162
                self.match(CgrammerParser.RROUND)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 71]:
                localctx = CgrammerParser.Expr_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_addrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_addr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UnitContext(Expr_addrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_addrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_unit(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)


    class ArrayContext(Expr_addrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_addrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_unit(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unitContext,0)

        def LSQUARE(self):
            return self.getToken(CgrammerParser.LSQUARE, 0)
        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)

        def RSQUARE(self):
            return self.getToken(CgrammerParser.RSQUARE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)


    class Content_ofContext(Expr_addrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_addrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MULTIPLYorREFERENCEorPTR(self):
            return self.getToken(CgrammerParser.MULTIPLYorREFERENCEorPTR, 0)
        def expr_unit(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent_of" ):
                listener.enterContent_of(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent_of" ):
                listener.exitContent_of(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent_of" ):
                return visitor.visitContent_of(self)
            else:
                return visitor.visitChildren(self)


    class Address_ofContext(Expr_addrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_addrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BITANDorADDRESS(self):
            return self.getToken(CgrammerParser.BITANDorADDRESS, 0)
        def expr_unit(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddress_of" ):
                listener.enterAddress_of(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddress_of" ):
                listener.exitAddress_of(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddress_of" ):
                return visitor.visitAddress_of(self)
            else:
                return visitor.visitChildren(self)



    def expr_addr(self):

        localctx = CgrammerParser.Expr_addrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr_addr)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = CgrammerParser.Content_ofContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(CgrammerParser.MULTIPLYorREFERENCEorPTR)
                self.state = 168
                self.expr_unit()
                pass

            elif la_ == 2:
                localctx = CgrammerParser.Address_ofContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(CgrammerParser.BITANDorADDRESS)
                self.state = 170
                self.expr_unit()
                pass

            elif la_ == 3:
                localctx = CgrammerParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.expr_unit()
                self.state = 172
                self.match(CgrammerParser.LSQUARE)
                self.state = 173
                self.expression()
                self.state = 174
                self.match(CgrammerParser.RSQUARE)
                pass

            elif la_ == 4:
                localctx = CgrammerParser.UnitContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.expr_unit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_unaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_unary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NotContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(CgrammerParser.NOT, 0)
        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class NegativeContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(CgrammerParser.MINUS, 0)
        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative" ):
                listener.enterNegative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative" ):
                listener.exitNegative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative" ):
                return visitor.visitNegative(self)
            else:
                return visitor.visitChildren(self)


    class RincreaseContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)

        def SELFPLUS(self):
            return self.getToken(CgrammerParser.SELFPLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRincrease" ):
                listener.enterRincrease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRincrease" ):
                listener.exitRincrease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRincrease" ):
                return visitor.visitRincrease(self)
            else:
                return visitor.visitChildren(self)


    class LdecreaseContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SELFMINUS(self):
            return self.getToken(CgrammerParser.SELFMINUS, 0)
        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLdecrease" ):
                listener.enterLdecrease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLdecrease" ):
                listener.exitLdecrease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLdecrease" ):
                return visitor.visitLdecrease(self)
            else:
                return visitor.visitChildren(self)


    class RdecreaseContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)

        def SELFMINUS(self):
            return self.getToken(CgrammerParser.SELFMINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdecrease" ):
                listener.enterRdecrease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdecrease" ):
                listener.exitRdecrease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRdecrease" ):
                return visitor.visitRdecrease(self)
            else:
                return visitor.visitChildren(self)


    class PositiveContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(CgrammerParser.PLUS, 0)
        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositive" ):
                listener.enterPositive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositive" ):
                listener.exitPositive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositive" ):
                return visitor.visitPositive(self)
            else:
                return visitor.visitChildren(self)


    class AddrContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddr" ):
                listener.enterAddr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddr" ):
                listener.exitAddr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddr" ):
                return visitor.visitAddr(self)
            else:
                return visitor.visitChildren(self)


    class LincreseContext(Expr_unaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_unaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SELFPLUS(self):
            return self.getToken(CgrammerParser.SELFPLUS, 0)
        def expr_addr(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_addrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLincrese" ):
                listener.enterLincrese(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLincrese" ):
                listener.exitLincrese(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLincrese" ):
                return visitor.visitLincrese(self)
            else:
                return visitor.visitChildren(self)



    def expr_unary(self):

        localctx = CgrammerParser.Expr_unaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr_unary)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = CgrammerParser.LincreseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(CgrammerParser.SELFPLUS)
                self.state = 180
                self.expr_addr()
                pass

            elif la_ == 2:
                localctx = CgrammerParser.RincreaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.expr_addr()
                self.state = 182
                self.match(CgrammerParser.SELFPLUS)
                pass

            elif la_ == 3:
                localctx = CgrammerParser.LdecreaseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(CgrammerParser.SELFMINUS)
                self.state = 185
                self.expr_addr()
                pass

            elif la_ == 4:
                localctx = CgrammerParser.RdecreaseContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.expr_addr()
                self.state = 187
                self.match(CgrammerParser.SELFMINUS)
                pass

            elif la_ == 5:
                localctx = CgrammerParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.match(CgrammerParser.NOT)
                self.state = 190
                self.expr_addr()
                pass

            elif la_ == 6:
                localctx = CgrammerParser.PositiveContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 191
                self.match(CgrammerParser.PLUS)
                self.state = 192
                self.expr_addr()
                pass

            elif la_ == 7:
                localctx = CgrammerParser.NegativeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 193
                self.match(CgrammerParser.MINUS)
                self.state = 194
                self.expr_addr()
                pass

            elif la_ == 8:
                localctx = CgrammerParser.AddrContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 195
                self.expr_addr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_calc1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_calc1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivideContext(Expr_calc1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_calc1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc1(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc1Context,0)

        def DIVIDE(self):
            return self.getToken(CgrammerParser.DIVIDE, 0)
        def expr_unary(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class UnaryContext(Expr_calc1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_calc1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_unary(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(Expr_calc1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_calc1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc1(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc1Context,0)

        def MULTIPLYorREFERENCEorPTR(self):
            return self.getToken(CgrammerParser.MULTIPLYorREFERENCEorPTR, 0)
        def expr_unary(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class ModuloContext(Expr_calc1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_calc1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc1(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc1Context,0)

        def MODULO(self):
            return self.getToken(CgrammerParser.MODULO, 0)
        def expr_unary(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_unaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo" ):
                listener.enterModulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo" ):
                listener.exitModulo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulo" ):
                return visitor.visitModulo(self)
            else:
                return visitor.visitChildren(self)



    def expr_calc1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CgrammerParser.Expr_calc1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr_calc1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CgrammerParser.UnaryContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 199
            self.expr_unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = CgrammerParser.MultiplyContext(self, CgrammerParser.Expr_calc1Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_calc1)
                        self.state = 201
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 202
                        self.match(CgrammerParser.MULTIPLYorREFERENCEorPTR)
                        self.state = 203
                        self.expr_unary()
                        pass

                    elif la_ == 2:
                        localctx = CgrammerParser.DivideContext(self, CgrammerParser.Expr_calc1Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_calc1)
                        self.state = 204
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 205
                        self.match(CgrammerParser.DIVIDE)
                        self.state = 206
                        self.expr_unary()
                        pass

                    elif la_ == 3:
                        localctx = CgrammerParser.ModuloContext(self, CgrammerParser.Expr_calc1Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_calc1)
                        self.state = 207
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 208
                        self.match(CgrammerParser.MODULO)
                        self.state = 209
                        self.expr_unary()
                        pass

             
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_calc2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_calc2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(Expr_calc2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_calc2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc2(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc2Context,0)

        def PLUS(self):
            return self.getToken(CgrammerParser.PLUS, 0)
        def expr_calc1(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubtractContext(Expr_calc2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_calc2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc2(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc2Context,0)

        def MINUS(self):
            return self.getToken(CgrammerParser.MINUS, 0)
        def expr_calc1(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtract" ):
                listener.enterSubtract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtract" ):
                listener.exitSubtract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtract" ):
                return visitor.visitSubtract(self)
            else:
                return visitor.visitChildren(self)


    class Calc1Context(Expr_calc2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_calc2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc1(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalc1" ):
                listener.enterCalc1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalc1" ):
                listener.exitCalc1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc1" ):
                return visitor.visitCalc1(self)
            else:
                return visitor.visitChildren(self)



    def expr_calc2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CgrammerParser.Expr_calc2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr_calc2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CgrammerParser.Calc1Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 216
            self.expr_calc1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 224
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = CgrammerParser.AddContext(self, CgrammerParser.Expr_calc2Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_calc2)
                        self.state = 218
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 219
                        self.match(CgrammerParser.PLUS)
                        self.state = 220
                        self.expr_calc1(0)
                        pass

                    elif la_ == 2:
                        localctx = CgrammerParser.SubtractContext(self, CgrammerParser.Expr_calc2Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_calc2)
                        self.state = 221
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 222
                        self.match(CgrammerParser.MINUS)
                        self.state = 223
                        self.expr_calc1(0)
                        pass

             
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_rop1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_rop1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualContext(Expr_rop1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Expr_calc2Context)
            else:
                return self.getTypedRuleContext(CgrammerParser.Expr_calc2Context,i)

        def EQUAL(self):
            return self.getToken(CgrammerParser.EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class Calc2Context(Expr_rop1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc2(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_calc2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalc2" ):
                listener.enterCalc2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalc2" ):
                listener.exitCalc2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc2" ):
                return visitor.visitCalc2(self)
            else:
                return visitor.visitChildren(self)


    class NequalContext(Expr_rop1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_calc2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Expr_calc2Context)
            else:
                return self.getTypedRuleContext(CgrammerParser.Expr_calc2Context,i)

        def NOTEQUAL(self):
            return self.getToken(CgrammerParser.NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNequal" ):
                listener.enterNequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNequal" ):
                listener.exitNequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNequal" ):
                return visitor.visitNequal(self)
            else:
                return visitor.visitChildren(self)



    def expr_rop1(self):

        localctx = CgrammerParser.Expr_rop1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_rop1)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = CgrammerParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.expr_calc2(0)
                self.state = 230
                self.match(CgrammerParser.EQUAL)
                self.state = 231
                self.expr_calc2(0)
                pass

            elif la_ == 2:
                localctx = CgrammerParser.NequalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.expr_calc2(0)
                self.state = 234
                self.match(CgrammerParser.NOTEQUAL)
                self.state = 235
                self.expr_calc2(0)
                pass

            elif la_ == 3:
                localctx = CgrammerParser.Calc2Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.expr_calc2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_rop2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_rop2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LeuqalContext(Expr_rop2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_rop1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Expr_rop1Context)
            else:
                return self.getTypedRuleContext(CgrammerParser.Expr_rop1Context,i)

        def LEQUAL(self):
            return self.getToken(CgrammerParser.LEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeuqal" ):
                listener.enterLeuqal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeuqal" ):
                listener.exitLeuqal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeuqal" ):
                return visitor.visitLeuqal(self)
            else:
                return visitor.visitChildren(self)


    class GequalContext(Expr_rop2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_rop1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Expr_rop1Context)
            else:
                return self.getTypedRuleContext(CgrammerParser.Expr_rop1Context,i)

        def GEQUAL(self):
            return self.getToken(CgrammerParser.GEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGequal" ):
                listener.enterGequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGequal" ):
                listener.exitGequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGequal" ):
                return visitor.visitGequal(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(Expr_rop2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_rop1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Expr_rop1Context)
            else:
                return self.getTypedRuleContext(CgrammerParser.Expr_rop1Context,i)

        def LESS(self):
            return self.getToken(CgrammerParser.LESS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)


    class Rop1Context(Expr_rop2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_rop1(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_rop1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRop1" ):
                listener.enterRop1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRop1" ):
                listener.exitRop1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRop1" ):
                return visitor.visitRop1(self)
            else:
                return visitor.visitChildren(self)


    class GreaterContext(Expr_rop2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_rop2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_rop1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Expr_rop1Context)
            else:
                return self.getTypedRuleContext(CgrammerParser.Expr_rop1Context,i)

        def GREATER(self):
            return self.getToken(CgrammerParser.GREATER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater" ):
                listener.enterGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater" ):
                listener.exitGreater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater" ):
                return visitor.visitGreater(self)
            else:
                return visitor.visitChildren(self)



    def expr_rop2(self):

        localctx = CgrammerParser.Expr_rop2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr_rop2)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = CgrammerParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.expr_rop1()
                self.state = 241
                self.match(CgrammerParser.GREATER)
                self.state = 242
                self.expr_rop1()
                pass

            elif la_ == 2:
                localctx = CgrammerParser.GequalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.expr_rop1()
                self.state = 245
                self.match(CgrammerParser.GEQUAL)
                self.state = 246
                self.expr_rop1()
                pass

            elif la_ == 3:
                localctx = CgrammerParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.expr_rop1()
                self.state = 249
                self.match(CgrammerParser.LESS)
                self.state = 250
                self.expr_rop1()
                pass

            elif la_ == 4:
                localctx = CgrammerParser.LeuqalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.expr_rop1()
                self.state = 253
                self.match(CgrammerParser.LEQUAL)
                self.state = 254
                self.expr_rop1()
                pass

            elif la_ == 5:
                localctx = CgrammerParser.Rop1Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.expr_rop1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_logicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_expr_logic

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrContext(Expr_logicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_logicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_logic(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_logicContext,0)

        def OR(self):
            return self.getToken(CgrammerParser.OR, 0)
        def expr_rop2(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_rop2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(Expr_logicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_logicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_logic(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_logicContext,0)

        def AND(self):
            return self.getToken(CgrammerParser.AND, 0)
        def expr_rop2(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_rop2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class Rop2Context(Expr_logicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Expr_logicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_rop2(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_rop2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRop2" ):
                listener.enterRop2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRop2" ):
                listener.exitRop2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRop2" ):
                return visitor.visitRop2(self)
            else:
                return visitor.visitChildren(self)



    def expr_logic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CgrammerParser.Expr_logicContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_logic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CgrammerParser.Rop2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 260
            self.expr_rop2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 268
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = CgrammerParser.AndContext(self, CgrammerParser.Expr_logicContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logic)
                        self.state = 262
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 263
                        self.match(CgrammerParser.AND)
                        self.state = 264
                        self.expr_rop2()
                        pass

                    elif la_ == 2:
                        localctx = CgrammerParser.OrContext(self, CgrammerParser.Expr_logicContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logic)
                        self.state = 265
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 266
                        self.match(CgrammerParser.OR)
                        self.state = 267
                        self.expr_rop2()
                        pass

             
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_logic(self):
            return self.getTypedRuleContext(CgrammerParser.Expr_logicContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CgrammerParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.expr_logic(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_assignment_operator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SuvequalContext(Assignment_operatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Assignment_operatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUSASSIGN(self):
            return self.getToken(CgrammerParser.MINUSASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuvequal" ):
                listener.enterSuvequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuvequal" ):
                listener.exitSuvequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuvequal" ):
                return visitor.visitSuvequal(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyequalContext(Assignment_operatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Assignment_operatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MULTIPLYASSIGN(self):
            return self.getToken(CgrammerParser.MULTIPLYASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyequal" ):
                listener.enterMultiplyequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyequal" ):
                listener.exitMultiplyequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplyequal" ):
                return visitor.visitMultiplyequal(self)
            else:
                return visitor.visitChildren(self)


    class AddeqaulContext(Assignment_operatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Assignment_operatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUSASSIGN(self):
            return self.getToken(CgrammerParser.PLUSASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddeqaul" ):
                listener.enterAddeqaul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddeqaul" ):
                listener.exitAddeqaul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddeqaul" ):
                return visitor.visitAddeqaul(self)
            else:
                return visitor.visitChildren(self)


    class ModuloequalContext(Assignment_operatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Assignment_operatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MODULOASSIGN(self):
            return self.getToken(CgrammerParser.MODULOASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuloequal" ):
                listener.enterModuloequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuloequal" ):
                listener.exitModuloequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuloequal" ):
                return visitor.visitModuloequal(self)
            else:
                return visitor.visitChildren(self)


    class DivideequalContext(Assignment_operatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Assignment_operatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIVIDEASSIGN(self):
            return self.getToken(CgrammerParser.DIVIDEASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivideequal" ):
                listener.enterDivideequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivideequal" ):
                listener.exitDivideequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivideequal" ):
                return visitor.visitDivideequal(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(Assignment_operatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Assignment_operatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(CgrammerParser.ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignment_operator(self):

        localctx = CgrammerParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment_operator)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                localctx = CgrammerParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(CgrammerParser.ASSIGN)
                pass
            elif token in [36]:
                localctx = CgrammerParser.AddeqaulContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(CgrammerParser.PLUSASSIGN)
                pass
            elif token in [37]:
                localctx = CgrammerParser.SuvequalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.match(CgrammerParser.MINUSASSIGN)
                pass
            elif token in [38]:
                localctx = CgrammerParser.MultiplyequalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 278
                self.match(CgrammerParser.MULTIPLYASSIGN)
                pass
            elif token in [39]:
                localctx = CgrammerParser.DivideequalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 279
                self.match(CgrammerParser.DIVIDEASSIGN)
                pass
            elif token in [40]:
                localctx = CgrammerParser.ModuloequalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 280
                self.match(CgrammerParser.MODULOASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CgrammerParser.IDENTIFIER, 0)

        def assignment_operator(self):
            return self.getTypedRuleContext(CgrammerParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.IndexContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.IndexContext,i)


        def getRuleIndex(self):
            return CgrammerParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = CgrammerParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(CgrammerParser.IDENTIFIER)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==66:
                self.state = 284
                self.index()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self.assignment_operator()
            self.state = 291
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.AssignmentContext,i)


        def type_(self):
            return self.getTypedRuleContext(CgrammerParser.TypeContext,0)


        def VOID(self):
            return self.getToken(CgrammerParser.VOID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.COMMA)
            else:
                return self.getToken(CgrammerParser.COMMA, i)

        def getRuleIndex(self):
            return CgrammerParser.RULE_variable_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_definition" ):
                listener.enterVariable_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_definition" ):
                listener.exitVariable_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_definition" ):
                return visitor.visitVariable_definition(self)
            else:
                return visitor.visitChildren(self)




    def variable_definition(self):

        localctx = CgrammerParser.Variable_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variable_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 17]:
                self.state = 293
                self.type_()
                pass
            elif token in [31]:
                self.state = 294
                self.match(CgrammerParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 297
            self.assignment()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 298
                self.match(CgrammerParser.COMMA)
                self.state = 299
                self.assignment()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lib_announceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_lib_announce

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Strlen_announceContext(Lib_announceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_announceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRLEN(self):
            return self.getToken(CgrammerParser.STRLEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrlen_announce" ):
                listener.enterStrlen_announce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrlen_announce" ):
                listener.exitStrlen_announce(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrlen_announce" ):
                return visitor.visitStrlen_announce(self)
            else:
                return visitor.visitChildren(self)


    class Memest_announceContext(Lib_announceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_announceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MEMSET(self):
            return self.getToken(CgrammerParser.MEMSET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemest_announce" ):
                listener.enterMemest_announce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemest_announce" ):
                listener.exitMemest_announce(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemest_announce" ):
                return visitor.visitMemest_announce(self)
            else:
                return visitor.visitChildren(self)


    class Printf_announceContext(Lib_announceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_announceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINTF(self):
            return self.getToken(CgrammerParser.PRINTF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf_announce" ):
                listener.enterPrintf_announce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf_announce" ):
                listener.exitPrintf_announce(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf_announce" ):
                return visitor.visitPrintf_announce(self)
            else:
                return visitor.visitChildren(self)


    class Scanf_annouceContext(Lib_announceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Lib_announceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCANF(self):
            return self.getToken(CgrammerParser.SCANF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanf_annouce" ):
                listener.enterScanf_annouce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanf_annouce" ):
                listener.exitScanf_annouce(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanf_annouce" ):
                return visitor.visitScanf_annouce(self)
            else:
                return visitor.visitChildren(self)



    def lib_announce(self):

        localctx = CgrammerParser.Lib_announceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lib_announce)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CgrammerParser.Memest_announceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(CgrammerParser.MEMSET)
                pass
            elif token in [2]:
                localctx = CgrammerParser.Strlen_announceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(CgrammerParser.STRLEN)
                pass
            elif token in [3]:
                localctx = CgrammerParser.Printf_announceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.match(CgrammerParser.PRINTF)
                pass
            elif token in [4]:
                localctx = CgrammerParser.Scanf_annouceContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 308
                self.match(CgrammerParser.SCANF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CgrammerParser.IDENTIFIER, 0)

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)

        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def LCURLY(self):
            return self.getToken(CgrammerParser.LCURLY, 0)

        def code(self):
            return self.getTypedRuleContext(CgrammerParser.CodeContext,0)


        def RCURLY(self):
            return self.getToken(CgrammerParser.RCURLY, 0)

        def type_(self):
            return self.getTypedRuleContext(CgrammerParser.TypeContext,0)


        def VOID(self):
            return self.getToken(CgrammerParser.VOID, 0)

        def params_definition(self):
            return self.getTypedRuleContext(CgrammerParser.Params_definitionContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition" ):
                listener.enterFunction_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition" ):
                listener.exitFunction_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = CgrammerParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_function_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 17]:
                self.state = 311
                self.type_()
                pass
            elif token in [31]:
                self.state = 312
                self.match(CgrammerParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 315
            self.match(CgrammerParser.IDENTIFIER)
            self.state = 316
            self.match(CgrammerParser.LROUND)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                self.state = 317
                self.params_definition()


            self.state = 320
            self.match(CgrammerParser.RROUND)
            self.state = 321
            self.match(CgrammerParser.LCURLY)
            self.state = 322
            self.code()
            self.state = 323
            self.match(CgrammerParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = CgrammerParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pure_if_block(self):
            return self.getTypedRuleContext(CgrammerParser.Pure_if_blockContext,0)


        def elif_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Elif_blockContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.Elif_blockContext,i)


        def else_block(self):
            return self.getTypedRuleContext(CgrammerParser.Else_blockContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_block" ):
                return visitor.visitIf_block(self)
            else:
                return visitor.visitChildren(self)




    def if_block(self):

        localctx = CgrammerParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.pure_if_block()
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 328
                    self.elif_block() 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 334
                self.else_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pure_if_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CgrammerParser.IF, 0)

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)

        def condition(self):
            return self.getTypedRuleContext(CgrammerParser.ConditionContext,0)


        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def code_with_domain(self):
            return self.getTypedRuleContext(CgrammerParser.Code_with_domainContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_pure_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPure_if_block" ):
                listener.enterPure_if_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPure_if_block" ):
                listener.exitPure_if_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPure_if_block" ):
                return visitor.visitPure_if_block(self)
            else:
                return visitor.visitChildren(self)




    def pure_if_block(self):

        localctx = CgrammerParser.Pure_if_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_pure_if_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(CgrammerParser.IF)
            self.state = 338
            self.match(CgrammerParser.LROUND)
            self.state = 339
            self.condition()
            self.state = 340
            self.match(CgrammerParser.RROUND)
            self.state = 341
            self.code_with_domain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(CgrammerParser.ELIF, 0)

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)

        def condition(self):
            return self.getTypedRuleContext(CgrammerParser.ConditionContext,0)


        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def code_with_domain(self):
            return self.getTypedRuleContext(CgrammerParser.Code_with_domainContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_elif_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_block" ):
                listener.enterElif_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_block" ):
                listener.exitElif_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_block" ):
                return visitor.visitElif_block(self)
            else:
                return visitor.visitChildren(self)




    def elif_block(self):

        localctx = CgrammerParser.Elif_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elif_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(CgrammerParser.ELIF)
            self.state = 344
            self.match(CgrammerParser.LROUND)
            self.state = 345
            self.condition()
            self.state = 346
            self.match(CgrammerParser.RROUND)
            self.state = 347
            self.code_with_domain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CgrammerParser.ELSE, 0)

        def code_with_domain(self):
            return self.getTypedRuleContext(CgrammerParser.Code_with_domainContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_else_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_block" ):
                listener.enterElse_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_block" ):
                listener.exitElse_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_block" ):
                return visitor.visitElse_block(self)
            else:
                return visitor.visitChildren(self)




    def else_block(self):

        localctx = CgrammerParser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(CgrammerParser.ELSE)
            self.state = 350
            self.code_with_domain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CgrammerParser.WHILE, 0)

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)

        def condition(self):
            return self.getTypedRuleContext(CgrammerParser.ConditionContext,0)


        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def code_with_domain(self):
            return self.getTypedRuleContext(CgrammerParser.Code_with_domainContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_while_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_block" ):
                listener.enterWhile_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_block" ):
                listener.exitWhile_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_block" ):
                return visitor.visitWhile_block(self)
            else:
                return visitor.visitChildren(self)




    def while_block(self):

        localctx = CgrammerParser.While_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_while_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(CgrammerParser.WHILE)
            self.state = 353
            self.match(CgrammerParser.LROUND)
            self.state = 354
            self.condition()
            self.state = 355
            self.match(CgrammerParser.RROUND)
            self.state = 356
            self.code_with_domain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CgrammerParser.FOR, 0)

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)

        def for_var(self):
            return self.getTypedRuleContext(CgrammerParser.For_varContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.SEMICOLON)
            else:
                return self.getToken(CgrammerParser.SEMICOLON, i)

        def condition(self):
            return self.getTypedRuleContext(CgrammerParser.ConditionContext,0)


        def for_iter(self):
            return self.getTypedRuleContext(CgrammerParser.For_iterContext,0)


        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def code_with_domain(self):
            return self.getTypedRuleContext(CgrammerParser.Code_with_domainContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_for_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_block" ):
                listener.enterFor_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_block" ):
                listener.exitFor_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_block" ):
                return visitor.visitFor_block(self)
            else:
                return visitor.visitChildren(self)




    def for_block(self):

        localctx = CgrammerParser.For_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(CgrammerParser.FOR)
            self.state = 359
            self.match(CgrammerParser.LROUND)
            self.state = 360
            self.for_var()
            self.state = 361
            self.match(CgrammerParser.SEMICOLON)
            self.state = 362
            self.condition()
            self.state = 363
            self.match(CgrammerParser.SEMICOLON)
            self.state = 364
            self.for_iter()
            self.state = 365
            self.match(CgrammerParser.RROUND)
            self.state = 366
            self.code_with_domain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(CgrammerParser.Variable_declarationContext,0)


        def variable_definition(self):
            return self.getTypedRuleContext(CgrammerParser.Variable_definitionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(CgrammerParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_for_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_var" ):
                listener.enterFor_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_var" ):
                listener.exitFor_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_var" ):
                return visitor.visitFor_var(self)
            else:
                return visitor.visitChildren(self)




    def for_var(self):

        localctx = CgrammerParser.For_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 368
                self.variable_declaration()

            elif la_ == 2:
                self.state = 369
                self.variable_definition()

            elif la_ == 3:
                self.state = 370
                self.assignment()

            elif la_ == 4:
                self.state = 371
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_iterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CgrammerParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_for_iter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_iter" ):
                listener.enterFor_iter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_iter" ):
                listener.exitFor_iter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_iter" ):
                return visitor.visitFor_iter(self)
            else:
                return visitor.visitChildren(self)




    def for_iter(self):

        localctx = CgrammerParser.For_iterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_iter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 374
                self.assignment()

            elif la_ == 2:
                self.state = 375
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(CgrammerParser.SWITCH, 0)

        def LROUND(self):
            return self.getToken(CgrammerParser.LROUND, 0)

        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def RROUND(self):
            return self.getToken(CgrammerParser.RROUND, 0)

        def LCURLY(self):
            return self.getToken(CgrammerParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(CgrammerParser.RCURLY, 0)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.CASE)
            else:
                return self.getToken(CgrammerParser.CASE, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.ValueContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.ValueContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.COLON)
            else:
                return self.getToken(CgrammerParser.COLON, i)

        def code(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.CodeContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.CodeContext,i)


        def getRuleIndex(self):
            return CgrammerParser.RULE_switch_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_block" ):
                listener.enterSwitch_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_block" ):
                listener.exitSwitch_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_block" ):
                return visitor.visitSwitch_block(self)
            else:
                return visitor.visitChildren(self)




    def switch_block(self):

        localctx = CgrammerParser.Switch_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_switch_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(CgrammerParser.SWITCH)
            self.state = 379
            self.match(CgrammerParser.LROUND)
            self.state = 380
            self.expression()
            self.state = 381
            self.match(CgrammerParser.RROUND)
            self.state = 382
            self.match(CgrammerParser.LCURLY)
            self.state = 388 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 383
                self.match(CgrammerParser.CASE)
                self.state = 384
                self.value()
                self.state = 385
                self.match(CgrammerParser.COLON)
                self.state = 386
                self.code()
                self.state = 390 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==23):
                    break

            self.state = 392
            self.match(CgrammerParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BreakContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(CgrammerParser.BREAK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)


    class ContinueContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(CgrammerParser.CONTINUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue" ):
                listener.enterContinue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue" ):
                listener.exitContinue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)


    class Assign_stateContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(CgrammerParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_state" ):
                listener.enterAssign_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_state" ):
                listener.exitAssign_state(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_state" ):
                return visitor.visitAssign_state(self)
            else:
                return visitor.visitChildren(self)


    class DefinitionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable_definition(self):
            return self.getTypedRuleContext(CgrammerParser.Variable_definitionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)


    class ExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable_declaration(self):
            return self.getTypedRuleContext(CgrammerParser.Variable_declarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class Lib_funcContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lib_announce(self):
            return self.getTypedRuleContext(CgrammerParser.Lib_announceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLib_func" ):
                listener.enterLib_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLib_func" ):
                listener.exitLib_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLib_func" ):
                return visitor.visitLib_func(self)
            else:
                return visitor.visitChildren(self)


    class ReturnContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(CgrammerParser.RETURN, 0)
        def expression(self):
            return self.getTypedRuleContext(CgrammerParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = CgrammerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = CgrammerParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.variable_declaration()
                pass

            elif la_ == 2:
                localctx = CgrammerParser.DefinitionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.variable_definition()
                pass

            elif la_ == 3:
                localctx = CgrammerParser.Assign_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.assignment()
                pass

            elif la_ == 4:
                localctx = CgrammerParser.ExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.expression()
                pass

            elif la_ == 5:
                localctx = CgrammerParser.Lib_funcContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 398
                self.lib_announce()
                pass

            elif la_ == 6:
                localctx = CgrammerParser.BreakContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 399
                self.match(CgrammerParser.BREAK)
                pass

            elif la_ == 7:
                localctx = CgrammerParser.ContinueContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 400
                self.match(CgrammerParser.CONTINUE)
                pass

            elif la_ == 8:
                localctx = CgrammerParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 401
                self.match(CgrammerParser.RETURN)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 54111365249384416) != 0) or _la==64 or _la==71:
                    self.state = 402
                    self.expression()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CgrammerParser.SEMICOLON, 0)

        def statement(self):
            return self.getTypedRuleContext(CgrammerParser.StatementContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = CgrammerParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 54111369276162046) != 0) or _la==64 or _la==71:
                self.state = 407
                self.statement()


            self.state = 410
            self.match(CgrammerParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_block(self):
            return self.getTypedRuleContext(CgrammerParser.If_blockContext,0)


        def while_block(self):
            return self.getTypedRuleContext(CgrammerParser.While_blockContext,0)


        def for_block(self):
            return self.getTypedRuleContext(CgrammerParser.For_blockContext,0)


        def switch_block(self):
            return self.getTypedRuleContext(CgrammerParser.Switch_blockContext,0)


        def line(self):
            return self.getTypedRuleContext(CgrammerParser.LineContext,0)


        def getRuleIndex(self):
            return CgrammerParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CgrammerParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_block)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.if_block()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.while_block()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.for_block()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.switch_block()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 28, 29, 30, 31, 41, 42, 43, 44, 45, 54, 55, 62, 64, 71]:
                self.enterOuterAlt(localctx, 5)
                self.state = 416
                self.line()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_with_domainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CgrammerParser.RULE_code_with_domain

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Domained_codeContext(Code_with_domainContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Code_with_domainContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LCURLY(self):
            return self.getToken(CgrammerParser.LCURLY, 0)
        def code(self):
            return self.getTypedRuleContext(CgrammerParser.CodeContext,0)

        def RCURLY(self):
            return self.getToken(CgrammerParser.RCURLY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomained_code" ):
                listener.enterDomained_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomained_code" ):
                listener.exitDomained_code(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomained_code" ):
                return visitor.visitDomained_code(self)
            else:
                return visitor.visitChildren(self)


    class Simple_codeContext(Code_with_domainContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CgrammerParser.Code_with_domainContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def code(self):
            return self.getTypedRuleContext(CgrammerParser.CodeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_code" ):
                listener.enterSimple_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_code" ):
                listener.exitSimple_code(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_code" ):
                return visitor.visitSimple_code(self)
            else:
                return visitor.visitChildren(self)



    def code_with_domain(self):

        localctx = CgrammerParser.Code_with_domainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_code_with_domain)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 27, 28, 29, 30, 31, 41, 42, 43, 44, 45, 54, 55, 62, 64, 69, 71]:
                localctx = CgrammerParser.Simple_codeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.code()
                pass
            elif token in [68]:
                localctx = CgrammerParser.Domained_codeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(CgrammerParser.LCURLY)
                self.state = 421
                self.code()
                self.state = 422
                self.match(CgrammerParser.RCURLY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.BlockContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.BlockContext,i)


        def getRuleIndex(self):
            return CgrammerParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = CgrammerParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 426
                    self.block() 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CgrammerParser.SEMICOLON)
            else:
                return self.getToken(CgrammerParser.SEMICOLON, i)

        def function_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Function_definitionContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.Function_definitionContext,i)


        def lib_announce(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Lib_announceContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.Lib_announceContext,i)


        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.Variable_declarationContext,i)


        def variable_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CgrammerParser.Variable_definitionContext)
            else:
                return self.getTypedRuleContext(CgrammerParser.Variable_definitionContext,i)


        def getRuleIndex(self):
            return CgrammerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CgrammerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 435
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        self.state = 432
                        self.lib_announce()
                        pass

                    elif la_ == 2:
                        self.state = 433
                        self.variable_declaration()
                        pass

                    elif la_ == 3:
                        self.state = 434
                        self.variable_definition()
                        pass


                    self.state = 437
                    self.match(CgrammerParser.SEMICOLON) 
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 445 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 444
                self.function_definition()
                self.state = 447 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147729408) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_calc1_sempred
        self._predicates[14] = self.expr_calc2_sempred
        self._predicates[17] = self.expr_logic_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_calc1_sempred(self, localctx:Expr_calc1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_calc2_sempred(self, localctx:Expr_calc2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr_logic_sempred(self, localctx:Expr_logicContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




