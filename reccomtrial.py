def recc(mids,type):
    m = {15324: ['Action', 'Comedy', 'Romance'], 15864: ['Adventure', 'Comedy', 'Drama', 'Western'],
         17136: ['Drama', 'Sci-Fi'], 17925: ['Action', 'Adventure', 'Comedy', 'Drama', 'War'],
         19254: ['Biography', 'Drama', 'History'], 21749: ['Comedy', 'Drama', 'Romance'],
         22100: ['Crime', 'Mystery', 'Thriller'], 25316: ['Comedy', 'Romance'],
         27977: ['Comedy', 'Drama', 'Family', 'Romance'], 31381: ['Drama', 'History', 'Romance', 'War'],
         31679: ['Comedy', 'Drama'], 32553: ['Comedy', 'Drama', 'War'],
         32976: ['Drama', 'Mystery', 'Romance', 'Thriller'], 33467: ['Drama', 'Mystery'],
         34583: ['Drama', 'Romance', 'War'], 35446: ['Comedy', 'Romance', 'War'],
         36775: ['Crime', 'Drama', 'Film-Noir', 'Mystery', 'Thriller'], 38650: ['Drama', 'Family', 'Fantasy'],
         40522: ['Drama'], 40897: ['Adventure', 'Drama', 'Western'], 41959: ['Film-Noir', 'Mystery', 'Thriller'],
         42192: ['Drama'], 42876: ['Crime', 'Drama', 'Mystery'], 43014: ['Drama', 'Film-Noir'], 44741: ['Drama'],
         45152: ['Comedy', 'Musical', 'Romance'], 46268: ['Adventure', 'Drama', 'Thriller'], 46438: ['Drama'],
         46912: ['Crime', 'Thriller'], 47296: ['Crime', 'Drama', 'Thriller'], 47396: ['Mystery', 'Thriller'],
         47478: ['Action', 'Adventure', 'Drama'], 48021: ['Crime', 'Drama', 'Thriller'], 48473: ['Drama'],
         48956: ['Drama'], 50083: ['Crime', 'Drama'], 50188: ['Drama', 'Musical', 'Family'],
         50212: ['Adventure', 'Drama', 'War'], 50825: ['Drama', 'War'], 50870: ['Drama', 'Musical', 'Romance'],
         50976: ['Drama', 'Fantasy', 'History', 'Thriller'], 50986: ['Drama', 'Romance'],
         51201: ['Crime', 'Drama', 'Mystery', 'Thriller'], 51792: ['Drama', 'Music'],
         52357: ['Mystery', 'Romance', 'Thriller'], 52572: ['Drama'], 52618: ['Adventure', 'Drama', 'History'],
         53125: ['Adventure', 'Mystery', 'Thriller'], 53198: ['Crime', 'Drama'], 53291: ['Comedy', 'Music', 'Romance'],
         53604: ['Comedy', 'Drama', 'Romance'], 54098: ['Drama', 'Romance', 'War'],
         54215: ['Horror', 'Mystery', 'Thriller'], 55031: ['Drama', 'War'], 55630: ['Action', 'Drama', 'Thriller'],
         56058: ['Action', 'Drama', 'Mystery'], 56172: ['Adventure', 'Biography', 'Drama', 'History', 'War'],
         56592: ['Crime', 'Drama'], 57012: ['Comedy'], 57115: ['Adventure', 'Drama', 'History', 'Thriller', 'War'],
         57565: ['Crime', 'Drama', 'Mystery', 'Thriller'], 57935: ['Drama', 'Romance'], 58946: ['Drama', 'War'],
         59246: ['Drama', 'Musical', 'Romance'], 59578: ['Western'], 60107: ['Biography', 'Drama', 'History'],
         60196: ['Western'], 60827: ['Drama', 'Thriller'], 61512: ['Crime', 'Drama'], 62622: ['Adventure', 'Sci-Fi'],
         63404: ['Comedy', 'Musical', 'Romance'], 64116: ['Western'], 66763: ['Drama', 'Musical'],
         66921: ['Crime', 'Drama', 'Sci-Fi'], 68646: ['Crime', 'Drama'], 70735: ['Comedy', 'Crime', 'Drama'],
         71315: ['Drama', 'Mystery', 'Thriller'], 71562: ['Crime', 'Drama'], 71853: ['Adventure', 'Comedy', 'Fantasy'],
         72684: ['Adventure', 'Drama', 'History', 'War'], 72783: ['Comedy', 'Drama', 'Romance'],
         72860: ['Action', 'Crime', 'Drama', 'Thriller'], 73486: ['Drama'],
         73707: ['Action', 'Adventure', 'Comedy', 'Drama', 'Musical', 'Thriller', 'Western'], 74958: ['Drama'],
         75148: ['Drama', 'Sport'], 75314: ['Crime', 'Drama'], 76759: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'],
         77416: ['Drama', 'War'], 77451: ['Action', 'Crime', 'Thriller'], 77711: ['Drama', 'Music'],
         78748: ['Horror', 'Sci-Fi'], 78788: ['Drama', 'Mystery', 'War'], 79221: ['Comedy', 'Romance'],
         79470: ['Comedy'], 79944: ['Drama', 'Sci-Fi'], 80678: ['Biography', 'Drama'],
         80684: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 81398: ['Biography', 'Drama', 'Sport'],
         81505: ['Drama', 'Horror'], 82096: ['Adventure', 'Drama', 'Thriller', 'War'], 82971: ['Action', 'Adventure'],
         83658: ['Action', 'Sci-Fi', 'Thriller'], 84787: ['Horror', 'Mystery', 'Sci-Fi'],
         85743: ['Comedy', 'Crime', 'Drama'], 86190: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'],
         86250: ['Crime', 'Drama'], 86879: ['Biography', 'Drama', 'History', 'Music'],
         87544: ['Animation', 'Adventure', 'Fantasy', 'Sci-Fi'], 87843: ['Crime', 'Drama'], 87884: ['Drama'],
         88763: ['Adventure', 'Comedy', 'Sci-Fi'], 89881: ['Action', 'Drama', 'War'],
         90605: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 91251: ['Drama', 'Thriller', 'War'],
         91763: ['Drama', 'War'], 92005: ['Adventure', 'Drama'], 93058: ['Drama', 'War'],
         93578: ['Action', 'Comedy', 'Drama', 'Family', 'Musical', 'Sci-Fi'], 93603: ['Crime', 'Drama'],
         95016: ['Action', 'Thriller'], 95327: ['Animation', 'Drama', 'War'], 95765: ['Drama', 'Romance'],
         96283: ['Animation', 'Family', 'Fantasy'], 97165: ['Comedy', 'Drama'],
         97223: ['Comedy', 'Crime', 'Drama', 'Fantasy'], 97576: ['Action', 'Adventure'],
         99685: ['Biography', 'Crime', 'Drama'], 101649: ['Action', 'Crime', 'Drama'],
         102926: ['Crime', 'Drama', 'Thriller'], 103064: ['Action', 'Sci-Fi'],
         104561: ['Comedy', 'Drama', 'Romance', 'Sport'], 105236: ['Crime', 'Drama', 'Thriller'],
         105271: ['Drama', 'Romance', 'Thriller'], 105575: ['Drama'], 105695: ['Drama', 'Western'],
         107207: ['Biography', 'Crime', 'Drama'], 107290: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'],
         108052: ['Biography', 'Drama', 'History'], 109117: ['Action', 'Comedy', 'Romance'],
         109830: ['Drama', 'Romance'], 110357: ['Animation', 'Adventure', 'Drama', 'Family', 'Musical'],
         110413: ['Action', 'Crime', 'Drama', 'Thriller'], 110912: ['Crime', 'Drama'], 111161: ['Drama'],
         112471: ['Drama', 'Romance'], 112553: ['Drama', 'Romance'], 112573: ['Biography', 'Drama', 'History', 'War'],
         112641: ['Crime', 'Drama'], 112870: ['Drama', 'Romance'], 113247: ['Crime', 'Drama'],
         113277: ['Crime', 'Drama', 'Thriller'], 114369: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         114709: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 114814: ['Crime', 'Mystery', 'Thriller'],
         116231: ['Crime', 'Drama', 'Thriller'], 116282: ['Crime', 'Drama', 'Thriller'],
         116630: ['Action', 'Drama', 'Thriller'], 117951: ['Drama'], 118694: ['Drama', 'Romance'],
         118715: ['Comedy', 'Crime', 'Sport'], 118751: ['Action', 'Drama', 'History', 'Thriller', 'War'],
         118799: ['Comedy', 'Drama', 'Romance', 'War'], 118849: ['Drama', 'Family', 'Sport'],
         119217: ['Drama', 'Romance'], 119385: ['Biography', 'Drama'],
         119488: ['Crime', 'Drama', 'Mystery', 'Thriller'], 119698: ['Animation', 'Action', 'Adventure', 'Fantasy'],
         120382: ['Comedy', 'Drama'], 120586: ['Drama'], 120689: ['Crime', 'Drama', 'Fantasy', 'Mystery'],
         120735: ['Action', 'Comedy', 'Crime'], 120737: ['Action', 'Adventure', 'Drama', 'Fantasy'],
         120815: ['Drama', 'War'], 133093: ['Action', 'Sci-Fi'], 137523: ['Drama'],
         139876: ['Action', 'Crime', 'Drama'], 167260: ['Action', 'Adventure', 'Drama', 'Fantasy'],
         167261: ['Action', 'Adventure', 'Drama', 'Fantasy'], 167404: ['Drama', 'Mystery', 'Thriller'],
         169102: ['Drama', 'Musical', 'Sport'], 169547: ['Drama'], 172495: ['Action', 'Adventure', 'Drama'],
         180093: ['Drama'], 195231: ['Action', 'Crime', 'Drama', 'Thriller'], 196069: ['Adventure', 'Drama', 'Romance'],
         198781: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 200087: ['Action', 'Drama'],
         208092: ['Comedy', 'Crime'], 209144: ['Mystery', 'Thriller'], 211915: ['Comedy', 'Romance'],
         213969: ['Action', 'Comedy', 'Drama', 'Romance'], 214915: ['Comedy', 'Horror', 'Music', 'Mystery', 'Thriller'],
         220656: ['Action', 'Drama', 'Thriller'], 220832: ['Action', 'Crime', 'Drama', 'Thriller'],
         222012: ['Crime', 'Drama', 'History'], 237376: ['Action', 'Drama'], 242256: ['Drama', 'Musical', 'Romance'],
         242519: ['Action', 'Comedy', 'Crime', 'Drama'],
         245429: ['Animation', 'Adventure', 'Family', 'Fantasy', 'Mystery'], 245712: ['Drama', 'Thriller'],
         253474: ['Biography', 'Drama', 'Music', 'War'], 264464: ['Biography', 'Crime', 'Drama'],
         266543: ['Animation', 'Adventure', 'Comedy', 'Family'], 266697: ['Action', 'Crime', 'Drama', 'Thriller'],
         268978: ['Biography', 'Drama'], 291376: ['Action', 'Drama', 'Thriller'],
         292490: ['Comedy', 'Drama', 'Romance'], 296574: ['Action', 'Crime', 'Drama', 'Thriller'],
         312859: ['Action', 'Drama', 'War'], 317248: ['Crime', 'Drama'],
         319736: ['Action', 'Biography', 'Drama', 'History'], 323013: ['Action', 'Drama', 'Romance', 'War'],
         338013: ['Drama', 'Romance', 'Sci-Fi'], 347149: ['Animation', 'Adventure', 'Family', 'Fantasy'],
         347304: ['Comedy', 'Drama', 'Musical', 'Romance'], 353969: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         361748: ['Adventure', 'Drama', 'War'], 363163: ['Biography', 'Drama', 'History', 'War'],
         364569: ['Action', 'Drama', 'Mystery', 'Thriller'], 366840: ['Action', 'Romance', 'Sport'], 367110: ['Drama'],
         367495: ['Adventure', 'Comedy', 'Drama'], 372784: ['Action', 'Adventure'],
         373856: ['Action', 'Crime', 'Drama'], 374887: ['Comedy', 'Drama'], 375611: ['Drama'],
         375878: ['Action', 'Crime', 'Drama', 'Thriller'], 376076: ['Action', 'Drama'],
         376127: ['Action', 'Drama', 'Thriller'], 379370: ['Crime', 'Drama', 'Thriller'], 381681: ['Drama', 'Romance'],
         395169: ['Biography', 'Drama', 'History', 'War'], 400234: ['Action', 'Crime', 'Drama', 'History'],
         402014: ['Action', 'Crime', 'Drama', 'Thriller'], 405094: ['Drama', 'Mystery', 'Thriller'],
         405159: ['Drama', 'Sport'], 405508: ['Comedy', 'Crime', 'Drama'], 407887: ['Crime', 'Drama', 'Thriller'],
         420332: ['Drama', 'Family', 'Musical', 'Romance'], 431619: ['Action', 'Drama', 'Romance'],
         434409: ['Action', 'Drama', 'Sci-Fi', 'Thriller'],
         435761: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 453729: ['Drama', 'Sport'],
         455829: ['Action', 'Crime', 'Thriller'], 456144: ['Comedy', 'Drama', 'Romance'],
         457430: ['Drama', 'Fantasy', 'War'], 466460: ['Comedy', 'Crime', 'Drama'],
         468569: ['Action', 'Crime', 'Drama', 'Thriller'], 469494: ['Drama'], 471571: ['Action', 'Thriller'],
         476735: ['Drama', 'Family'], 477348: ['Crime', 'Drama', 'Thriller'],
         482571: ['Drama', 'Mystery', 'Sci-Fi', 'Thriller'], 488414: ['Action', 'Crime', 'Drama', 'Thriller'],
         499375: ['Drama'], 758758: ['Adventure', 'Biography', 'Drama'], 816258: ['Action', 'Crime', 'Thriller'],
         816692: ['Adventure', 'Drama', 'Sci-Fi'], 824316: ['Drama'], 843326: ['Comedy', 'Drama', 'Romance'],
         871510: ['Drama', 'Family', 'Sport'], 892769: ['Animation', 'Action', 'Adventure', 'Family', 'Fantasy'],
         910970: ['Animation', 'Adventure', 'Family', 'Romance', 'Sci-Fi'],
         978762: ['Animation', 'Comedy', 'Drama', 'Family'], 986264: ['Drama', 'Family'],
         993846: ['Biography', 'Crime', 'Drama'], 10189514: ['Drama'],
         10214826: ['Comedy', 'Crime', 'Mystery', 'Thriller'], 10272386: ['Drama'],
         1028532: ['Biography', 'Drama', 'Family'], 10324144: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         1049413: ['Animation', 'Adventure', 'Comedy', 'Family'], 1077248: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         1093370: ['Comedy', 'Drama', 'Romance'], 1130884: ['Mystery', 'Thriller'], 11581174: ['Action', 'Drama'],
         1180583: ['Drama', 'Romance'], 1187043: ['Comedy', 'Drama'], 1188996: ['Drama'],
         1201607: ['Adventure', 'Drama', 'Fantasy', 'Mystery'], 1205489: ['Drama'], 1230165: ['Drama', 'Music'],
         12361178: ['Crime', 'Drama', 'Thriller'], 1255953: ['Drama', 'Mystery', 'War'],
         1261047: ['Crime', 'Drama', 'Thriller'], 1266583: ['Drama'],
         1280558: ['Action', 'Crime', 'Drama', 'Mystery', 'Thriller'], 1288638: ['Comedy', 'Drama'],
         1291584: ['Action', 'Drama', 'Sport'], 1292703: ['Action', 'Comedy', 'Crime', 'Drama'],
         1305806: ['Drama', 'Mystery', 'Romance', 'Thriller'], 1327035: ['Drama', 'Romance'],
         1345836: ['Action', 'Adventure'], 1375666: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'],
         1392190: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 1392214: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         1417299: ['Action', 'Crime', 'Drama', 'Mystery', 'Thriller'], 1562872: ['Comedy', 'Drama'],
         1620933: ['Action', 'Biography', 'Crime', 'Sport', 'Thriller'], 1639426: ['Drama'],
         1649431: ['Action', 'Drama'], 1675434: ['Biography', 'Comedy', 'Drama'], 1773764: ['Drama'],
         1821480: ['Mystery', 'Thriller'], 1832382: ['Drama'], 1853728: ['Drama', 'Western'],
         1895587: ['Biography', 'Crime', 'Drama'], 1907761: ['Comedy', 'Drama', 'Family'],
         1950186: ['Action', 'Biography', 'Drama', 'Sport'],
         1954470: ['Action', 'Comedy', 'Crime', 'Drama', 'Thriller'],
         1979320: ['Action', 'Biography', 'Drama', 'Sport'], 2024544: ['Biography', 'Drama', 'History'],
         2082197: ['Comedy', 'Drama', 'Romance'],
         2096673: ['Animation', 'Adventure', 'Comedy', 'Drama', 'Family', 'Fantasy'], 2106476: ['Drama'],
         2119532: ['Biography', 'Drama', 'History', 'War'], 2181831: ['Biography', 'Drama'],
         2181931: ['Comedy', 'Drama', 'Family'], 2218988: ['Comedy', 'Drama'],
         2267998: ['Drama', 'Mystery', 'Thriller'], 2278388: ['Adventure', 'Comedy', 'Crime'],
         2283748: ['Comedy', 'Drama', 'Fantasy'], 2317337: ['Comedy', 'Romance'],
         2338151: ['Comedy', 'Drama', 'Musical', 'Sci-Fi'], 2350496: ['Drama', 'Romance'],
         2356180: ['Biography', 'Drama', 'Sport'], 2358592: ['Drama', 'Sci-Fi', 'Thriller'],
         2377938: ['Crime', 'Drama', 'Thriller'],
         2380307: ['Animation', 'Adventure', 'Family', 'Fantasy', 'Music', 'Mystery'],
         2395469: ['Drama', 'Music', 'Romance'], 2564144: ['Comedy', 'Drama'], 2582802: ['Drama', 'Music'],
         2585562: ['Horror', 'Thriller'], 2631186: ['Action', 'Drama'],
         2877108: ['Comedy', 'Crime', 'Drama', 'Fantasy'],
         2948372: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy', 'Music'], 2991224: ['Drama', 'War'],
         3011894: ['Comedy', 'Drama', 'Thriller'], 3124456: ['Mystery', 'Thriller'], 3170832: ['Drama', 'Thriller'],
         3315342: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 3322420: ['Adventure', 'Comedy', 'Drama'],
         3390572: ['Action', 'Crime', 'Drama', 'Thriller'], 3394420: ['Crime', 'Drama', 'Thriller'],
         3417422: ['Crime', 'Drama', 'Thriller'], 3449292: ['Adventure', 'Biography', 'Drama'],
         3569782: ['Action', 'Crime', 'Drama', 'Thriller'], 3614516: ['Comedy', 'Drama'],
         3668162: ['Comedy', 'Drama', 'Romance'], 3822396: ['Action', 'Comedy', 'Drama'],
         3848892: ['Action', 'Thriller'], 3863552: ['Action', 'Adventure', 'Comedy', 'Drama'],
         3973410: ['Comedy', 'Drama'], 4016934: ['Drama', 'Romance', 'Thriller'],
         4154756: ['Action', 'Adventure', 'Sci-Fi'], 4154796: ['Action', 'Adventure', 'Drama', 'Sci-Fi'],
         4169250: ['Biography', 'Drama', 'Sport'], 4387040: ['Drama', 'History'], 4429128: ['Drama', 'Thriller'],
         4430212: ['Crime', 'Drama', 'Mystery', 'Thriller'], 4432480: ['Mystery', 'Thriller'],
         4434004: ['Action', 'Crime', 'Drama'], 4633694: ['Animation', 'Action', 'Adventure', 'Family', 'Sci-Fi'],
         4635372: ['Drama'], 4679210: ['Comedy', 'Drama', 'Romance'],
         4729430: ['Animation', 'Adventure', 'Comedy', 'Family'], 4849438: ['Action', 'Drama'],
         4851630: ['Comedy', 'Drama', 'Thriller'], 4934950: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         4987556: ['Action', 'Crime', 'Thriller'], 4991384: ['Crime', 'Drama', 'Thriller'],
         5005684: ['Drama', 'Family'], 5027774: ['Comedy', 'Crime', 'Drama'],
         5074352: ['Action', 'Biography', 'Drama', 'Sport'], 5082014: ['Adventure', 'Drama', 'Romance', 'Thriller'],
         5121000: ['Biography', 'Drama'], 5311514: ['Animation', 'Drama', 'Fantasy', 'Romance'],
         5311546: ['Drama', 'Family'], 5312232: ['Drama', 'Romance'],
         5323662: ['Animation', 'Drama', 'Family', 'Romance'], 5571734: ['Drama', 'Thriller'],
         5764096: ['Comedy', 'Drama'], 5824826: ['Comedy', 'Drama', 'Romance'], 5867800: ['Drama'],
         5959980: ['Action', 'Crime', 'Drama', 'Thriller'], 6108090: ['Drama', 'Music'],
         6148156: ['Action', 'Crime', 'Drama', 'Thriller'], 6167894: ['Action', 'Comedy', 'Thriller'],
         6315524: ['Action', 'Drama', 'Thriller'], 6380520: ['Action', 'Crime', 'Mystery', 'Thriller'],
         6751668: ['Comedy', 'Drama', 'Thriller'], 6966692: ['Biography', 'Comedy', 'Drama', 'Music'],
         7019842: ['Drama', 'Romance'], 7019942: ['Comedy', 'Crime', 'Drama', 'Thriller'],
         7060344: ['Action', 'Crime', 'Thriller'], 7060460: ['Action', 'Crime', 'Thriller'],
         7098658: ['Action', 'Drama', 'Thriller'], 7180544: ['Action', 'Drama', 'Sport'], 7218518: ['Comedy', 'Drama'],
         7286456: ['Crime', 'Drama', 'Thriller'], 7294534: ['Action', 'Drama', 'Romance'], 7392212: ['Action', 'Drama'],
         7465992: ['Biography', 'Drama'], 7485048: ['Biography', 'Drama'], 7725596: ['Comedy', 'Drama'],
         7738784: ['Drama'], 7758160: ['Action', 'Thriller'],
         7822438: ['Action', 'Crime', 'Drama', 'Mystery', 'Thriller'], 7838252: ['Action', 'Drama'],
         8108198: ['Crime', 'Drama', 'Music', 'Mystery', 'Thriller'], 8108200: ['Action', 'Crime', 'Drama'],
         8110330: ['Comedy', 'Drama', 'Romance'], 8130968: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         8144834: ['Crime', 'Drama', 'Mystery', 'Thriller'], 8176054: ['Drama'],
         8239946: ['Drama', 'Fantasy', 'Horror', 'Thriller'], 8267604: ['Drama'], 8291224: ['Action', 'Drama', 'War'],
         8413338: ['Comedy', 'Drama', 'Romance'], 8503618: ['Biography', 'Drama', 'History', 'Musical'],
         8579674: ['Drama', 'Thriller', 'War'], 8613070: ['Drama', 'Romance'], 8948790: ['Drama', 'Sport'],
         9052870: ['Comedy', 'Drama'], 9477520: ['Action', 'Drama'], 9900782: ['Action', 'Thriller'],
         15097216: ["Crime", "Drama"], 1160419: ["Action", "Adventure", "Drama", "Sci-Fi"]}
    s={111161: ['Drama'], 68646: ['Crime', 'Drama'], 71562: ['Crime', 'Drama'], 468569: ['Action', 'Crime', 'Drama', 'Thriller'], 50083: ['Crime', 'Drama'], 108052: ['Biography', 'Drama', 'History'], 167260: ['Action', 'Adventure', 'Drama', 'Fantasy'], 110912: ['Crime', 'Drama'], 60196: ['Adventure', 'Western'], 120737: ['Action', 'Adventure', 'Drama', 'Fantasy'], 137523: ['Drama'], 109830: ['Drama', 'Romance'], 1375666: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 167261: ['Action', 'Adventure', 'Drama', 'Fantasy'], 80684: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 133093: ['Action', 'Sci-Fi'], 99685: ['Biography', 'Crime', 'Drama'], 73486: ['Drama'], 47478: ['Action', 'Adventure', 'Drama'], 114369: ['Crime', 'Drama', 'Mystery', 'Thriller'], 102926: ['Crime', 'Drama', 'Thriller'], 317248: ['Crime', 'Drama'], 118799: ['Comedy', 'Drama', 'Romance', 'War'], 38650: ['Drama', 'Family', 'Fantasy'], 76759: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 120815: ['Drama', 'War'], 816692: ['Adventure', 'Drama', 'Sci-Fi'], 245429: ['Animation', 'Adventure', 'Family', 'Fantasy', 'Mystery'], 120689: ['Crime', 'Drama', 'Fantasy', 'Mystery'], 6751668: ['Comedy', 'Drama', 'Thriller'], 110413: ['Action', 'Crime', 'Drama', 'Thriller'], 56058: ['Action', 'Drama', 'Mystery'], 253474: ['Biography', 'Drama', 'Music', 'War'], 103064: ['Action', 'Sci-Fi'], 114814: ['Crime', 'Drama', 'Mystery', 'Thriller'], 88763: ['Adventure', 'Comedy', 'Sci-Fi'], 54215: ['Horror', 'Mystery', 'Thriller'], 110357: ['Animation', 'Adventure', 'Drama', 'Family', 'Musical'], 27977: ['Comedy', 'Drama', 'Family', 'Romance'], 120586: ['Drama'], 95327: ['Animation', 'Drama', 'War'], 21749: ['Comedy', 'Drama', 'Romance'], 2582802: ['Drama', 'Music'], 172495: ['Action', 'Adventure', 'Drama'], 407887: ['Action', 'Crime', 'Drama', 'Thriller'], 1675434: ['Biography', 'Comedy', 'Drama'], 482571: ['Drama', 'Mystery', 'Sci-Fi', 'Thriller'], 34583: ['Drama', 'Romance', 'War'], 64116: ['Western'], 47396: ['Mystery', 'Thriller'], 95765: ['Drama', 'Romance'], 78748: ['Horror', 'Sci-Fi'], 78788: ['Drama', 'Mystery', 'War'], 209144: ['Mystery', 'Thriller'], 82971: ['Action', 'Adventure'], 32553: ['Comedy', 'Drama', 'War'], 405094: ['Drama', 'Mystery', 'Thriller'], 1853728: ['Drama', 'Western'], 50825: ['Drama', 'War'], 43014: ['Drama', 'Film-Noir'], 910970: ['Animation', 'Adventure', 'Family', 'Sci-Fi'], 4154756: ['Action', 'Adventure', 'Sci-Fi'], 51201: ['Crime', 'Drama', 'Mystery', 'Thriller'], 81505: ['Drama', 'Horror'], 4633694: ['Animation', 'Action', 'Adventure', 'Comedy', 'Family', 'Fantasy', 'Sci-Fi'], 57012: ['Comedy', 'War'], 119698: ['Animation', 'Action', 'Adventure', 'Fantasy'], 364569: ['Action', 'Drama', 'Mystery', 'Thriller'], 7286456: ['Crime', 'Drama', 'Thriller'], 5311514: ['Animation', 'Drama', 'Fantasy', 'Romance'], 1345836: ['Action', 'Crime'], 2380307: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy', 'Music', 'Mystery'], 90605: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 87843: ['Crime', 'Drama'], 4154796: ['Action', 'Adventure', 'Drama', 'Sci-Fi'], 8267604: ['Drama'], 82096: ['Adventure', 'Drama', 'Thriller', 'War'], 57565: ['Crime', 'Drama', 'Mystery', 'Thriller'], 1187043: ['Comedy', 'Drama'], 169547: ['Drama'], 114709: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 86879: ['Biography', 'Drama', 'Music'], 112573: ['Biography', 'Drama', 'History', 'War'], 8503618: ['Biography', 'Drama', 'History', 'Musical'], 361748: ['Adventure', 'Drama', 'War'], 119217: ['Drama', 'Romance'], 86190: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 62622: ['Adventure', 'Sci-Fi'], 105236: ['Crime', 'Drama', 'Thriller'], 22100: ['Crime', 'Mystery', 'Thriller'], 52357: ['Mystery', 'Romance', 'Thriller'], 986264: ['Drama', 'Family'], 91251: ['Drama', 'Thriller', 'War'], 33467: ['Drama', 'Mystery'], 2106476: ['Drama'], 180093: ['Drama'], 45152: ['Comedy', 'Musical', 'Romance'], 53125: ['Adventure', 'Mystery', 'Thriller'], 338013: ['Drama', 'Romance', 'Sci-Fi'], 40522: ['Drama'], 44741: ['Drama'], 56172: ['Adventure', 'Biography', 'Drama', 'War'], 12349: ['Comedy', 'Drama', 'Family'], 93058: ['Drama', 'War'], 5074352: ['Action', 'Biography', 'Drama', 'Sport'], 53604: ['Comedy', 'Drama', 'Romance'], 10272386: ['Drama', 'Mystery'], 1255953: ['Drama', 'Mystery', 'War'], 17136: ['Drama', 'Sci-Fi'], 36775: ['Crime', 'Drama', 'Film-Noir', 'Mystery', 'Thriller'], 66921: ['Crime', 'Drama', 'Sci-Fi'], 75314: ['Crime', 'Drama'], 48473: ['Drama'], 1832382: ['Drama'], 70735: ['Comedy', 'Crime', 'Drama'], 86250: ['Crime', 'Drama'], 208092: ['Comedy', 'Crime'], 8579674: ['Action', 'Drama', 'War'], 211915: ['Comedy', 'Romance'], 56592: ['Crime', 'Drama'], 435761: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 59578: ['Western'], 15097216: ['Crime', 'Drama'], 1049413: ['Animation', 'Adventure', 'Comedy', 'Drama', 'Family'], 97576: ['Action', 'Adventure'], 113277: ['Action', 'Crime', 'Drama'], 119488: ['Crime', 'Drama', 'Mystery', 'Thriller'], 55630: ['Action', 'Drama', 'Thriller'], 89881: ['Action', 'Drama', 'War'], 95016: ['Action', 'Thriller'], 42876: ['Crime', 'Drama', 'Mystery'], 6966692: ['Biography', 'Comedy', 'Drama', 'Music'], 363163: ['Biography', 'Drama', 'History', 'War'], 71853: ['Adventure', 'Comedy', 'Fantasy'], 42192: ['Drama'], 53291: ['Comedy', 'Music', 'Romance'], 372784: ['Action', 'Adventure'], 105695: ['Drama', 'Western'], 118849: ['Drama', 'Family', 'Sport'], 347149: ['Animation', 'Adventure', 'Family', 'Fantasy'], 993846: ['Biography', 'Comedy', 'Crime', 'Drama'], 55031: ['Drama', 'War'], 57115: ['Adventure', 'Drama', 'History', 'Thriller', 'War'], 112641: ['Crime', 'Drama'], 469494: ['Drama'], 40897: ['Adventure', 'Drama', 'Western'], 457430: ['Drama', 'Fantasy', 'War'], 268978: ['Biography', 'Drama'], 1305806: ['Drama', 'Mystery', 'Romance', 'Thriller'], 81398: ['Biography', 'Drama', 'Sport'], 71411: ['Adventure', 'Biography', 'Drama'], 71315: ['Drama', 'Mystery', 'Thriller'], 96283: ['Animation', 'Comedy', 'Family', 'Fantasy'], 120735: ['Action', 'Comedy', 'Crime'], 1130884: ['Mystery', 'Thriller'], 15864: ['Adventure', 'Comedy', 'Drama', 'Western'], 477348: ['Crime', 'Drama', 'Thriller'], 46912: ['Crime', 'Thriller'], 50976: ['Drama', 'Fantasy'], 84787: ['Horror', 'Mystery', 'Sci-Fi'], 5027774: ['Comedy', 'Crime', 'Drama'], 1160419: ['Action', 'Adventure', 'Drama', 'Sci-Fi'], 80678: ['Biography', 'Drama'], 167404: ['Drama', 'Mystery', 'Thriller'], 4729430: ['Animation', 'Adventure', 'Comedy', 'Family'], 50986: ['Drama', 'Romance'], 41959: ['Film-Noir', 'Mystery', 'Thriller'], 107290: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 120382: ['Comedy', 'Drama'], 434409: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 353969: ['Crime', 'Drama', 'Mystery', 'Thriller'], 83658: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 117951: ['Drama'], 2096673: ['Animation', 'Adventure', 'Comedy', 'Drama', 'Family', 'Fantasy', 'Sci-Fi'], 50212: ['Adventure', 'Drama', 'War'], 116282: ['Crime', 'Thriller'], 1291584: ['Action', 'Drama', 'Sport'], 266543: ['Animation', 'Adventure', 'Comedy', 'Family'], 266697: ['Action', 'Crime', 'Drama', 'Thriller'], 31381: ['Drama', 'History', 'Romance', 'War'], 47296: ['Crime', 'Drama', 'Thriller'], 46438: ['Drama'], 476735: ['Drama', 'Family'], 3011894: ['Comedy', 'Drama', 'Thriller'], 79944: ['Drama', 'Sci-Fi'], 65234: ['Crime', 'Drama', 'History', 'Thriller'], 77416: ['Drama', 'War'], 1392214: ['Crime', 'Drama', 'Mystery', 'Thriller'], 2278388: ['Adventure', 'Comedy', 'Crime'], 17925: ['Action', 'Adventure', 'Comedy', 'Drama', 'War'], 1205489: ['Drama'], 15324: ['Action', 'Comedy', 'Romance'], 60827: ['Drama', 'Thriller'], 112471: ['Drama', 'Romance'], 978762: ['Animation', 'Comedy', 'Drama', 'Family'], 264464: ['Biography', 'Crime', 'Drama'], 31679: ['Comedy', 'Drama'], 107207: ['Biography', 'Crime', 'Drama'], 3170832: ['Drama', 'Thriller'], 72684: ['Adventure', 'Drama', 'History', 'War'], 2267998: ['Drama', 'Mystery', 'Thriller'], 2119532: ['Biography', 'Drama', 'History', 'War'], 19254: ['Biography', 'Drama', 'History'], 8108198: ['Crime', 'Drama', 'Music', 'Mystery', 'Thriller'], 1950186: ['Action', 'Biography', 'Drama', 'Sport'], 2024544: ['Biography', 'Drama', 'History'], 35446: ['Comedy', 'Romance', 'War'], 118715: ['Comedy', 'Crime', 'Sport'], 77711: ['Drama', 'Music'], 892769: ['Animation', 'Action', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 97165: ['Comedy', 'Drama'], 1392190: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 52618: ['Adventure', 'Drama', 'History'], 1201607: ['Adventure', 'Fantasy', 'Mystery'], 405159: ['Drama', 'Sport'], 46268: ['Adventure', 'Drama', 'Thriller'], 7019842: ['Drama', 'Romance'], 4016934: ['Drama', 'Romance', 'Thriller'], 92005: ['Adventure', 'Drama'], 74958: ['Drama'], 3315342: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 61512: ['Crime', 'Drama'], 1954470: ['Action', 'Comedy', 'Crime', 'Drama', 'Thriller'], 1028532: ['Biography', 'Drama', 'Family'], 113247: ['Crime', 'Drama'], 53198: ['Crime', 'Drama'], 91763: ['Drama', 'War'], 5323662: ['Animation', 'Drama'], 1895587: ['Biography', 'Crime', 'Drama'], 198781: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 32976: ['Drama', 'Mystery', 'Romance', 'Thriller'], 79470: ['Comedy'], 395169: ['Biography', 'Drama', 'History', 'War'], 116231: ['Crime', 'Drama', 'Thriller'], 118694: ['Drama', 'Romance'], 1979320: ['Action', 'Biography', 'Drama', 'Sport'], 758758: ['Adventure', 'Biography', 'Drama'], 245712: ['Drama', 'Thriller'], 75148: ['Drama', 'Sport'], 87544: ['Animation', 'Adventure', 'Sci-Fi'], 60107: ['Biography', 'Drama', 'History'], 25316: ['Comedy', 'Romance'], 381681: ['Drama', 'Romance'], 83922: ['Drama'], 169858: ['Animation', 'Action', 'Drama', 'Fantasy', 'Sci-Fi'], 58946: ['Drama', 'War'], 50783: ['Drama'], 93779: ['Adventure', 'Family', 'Fantasy', 'Romance'], 87884: ['Drama'], 111495: ['Drama', 'Mystery', 'Romance']}
    k={1: ['Action', 'Adventure', 'Comedy', 'Drama', 'Sci-Fi'], 5: ['Action', 'Drama', 'Mystery', 'Sci-Fi'], 6: ['Action', 'Adventure', 'Comedy', 'Drama', 'Sci-Fi'], 7: ['Action', 'Drama', 'Mystery', 'Supernatural'], 8: ['Adventure', 'Fantasy', 'Supernatural'], 15: ['Action', 'Comedy', 'Sports'], 16: ['Comedy', 'Drama', 'Romance', 'Slice of Life'], 18: ['Action', 'Drama', 'Sports'], 19: ['Drama', 'Horror', 'Mystery', 'Suspense'], 22: ['Action', 'Comedy', 'Sports'], 23: ['Action', 'Sports'], 24: ['Comedy', 'Romance'], 26: ['Action', 'Drama', 'Sci-Fi'], 27: ['Action', 'Supernatural'], 28: ['Comedy', 'Gourmet'], 29: ['Action', 'Drama', 'Sci-Fi'], 30: ['Action', 'Avant Garde', 'Drama', 'Sci-Fi'], 32: ['Avant Garde', 'Drama', 'Sci-Fi'], 33: ['Action', 'Adventure', 'Drama', 'Fantasy', 'Horror', 'Supernatural'], 43: ['Action', 'Sci-Fi'], 44: ['Action', 'Drama', 'Romance'], 45: ['Action', 'Adventure', 'Comedy', 'Romance'], 46: [''], 47: ['Action', 'Adventure', 'Horror', 'Sci-Fi', 'Supernatural'], 48: ['Adventure', 'Fantasy', 'Mystery', 'Sci-Fi'], 49: ['Comedy', 'Romance', 'Supernatural'], 50: ['Comedy', 'Romance', 'Supernatural'], 51: ['Action', 'Drama', 'Romance', 'Supernatural'], 52: ['Comedy', 'Drama', 'Sci-Fi', 'Sports'], 54: ['Action', 'Drama', 'Sci-Fi'], 55: ['Action', 'Adventure', 'Fantasy', 'Horror', 'Sci-Fi'], 57: ['Comedy', 'Drama', 'Slice of Life'], 58: ['Adventure', 'Drama', 'Horror', 'Romance', 'Sci-Fi'], 59: ['Comedy', 'Drama', 'Romance', 'Sci-Fi', 'Ecchi'], 60: ['Action', 'Romance', 'Supernatural'], 62: ['Drama', 'Romance'], 64: ['Action', 'Comedy', 'Drama'], 65: ['Action', 'Comedy', 'Drama'], 66: ['Comedy', 'Slice of Life'], 67: ['Action', 'Adventure', 'Fantasy', 'Romance', 'Supernatural'], 68: ['Adventure', 'Comedy', 'Sci-Fi'], 69: ['Action', 'Fantasy', 'Sci-Fi'], 71: ['Action', 'Comedy', 'Sci-Fi'], 72: ['Action', 'Comedy'], 73: [''], 74: [''], 75: ['Action', 'Drama', 'Sci-Fi'], 76: ['Action', 'Comedy', 'Drama'], 79: ['Comedy', 'Drama', 'Fantasy', 'Romance', 'Ecchi'], 80: [''], 81: ['Adventure', 'Drama', 'Romance', 'Sci-Fi'], 82: ['Drama', 'Sci-Fi'], 83: ['Drama', 'Romance', 'Sci-Fi'], 84: ['Adventure', 'Drama', 'Romance', 'Sci-Fi'], 85: ['Drama', 'Romance', 'Sci-Fi'], 86: ['Comedy', 'Drama', 'Sci-Fi'], 88: ['Drama', 'Sci-Fi'], 89: ['Drama', 'Sci-Fi'], 91: ['Action', 'Drama', 'Sci-Fi'], 92: ['Adventure', 'Drama', 'Sci-Fi'], 94: ['Action', 'Drama', 'Romance', 'Sci-Fi'], 95: ['Action', 'Adventure', 'Drama', 'Romance', 'Sci-Fi'], 96: ['Adventure', 'Comedy', 'Drama', 'Romance', 'Sci-Fi', 'Sports'], 97: ['Action', 'Adventure', 'Sci-Fi'], 98: ['Action', 'Comedy', 'Drama', 'Fantasy', 'Girls Love', 'Romance'], 99: ['Comedy', 'Drama', 'Fantasy'], 100: ['Comedy', 'Drama', 'Fantasy', 'Romance'], 101: ['Drama', 'Romance', 'Slice of Life', 'Supernatural'], 104: ['Adventure', 'Comedy', 'Drama', 'Horror', 'Romance', 'Supernatural'], 105: ['Comedy', 'Romance', 'Slice of Life'], 106: ['Drama', 'Romance'], 107: ['Adventure', 'Comedy', 'Fantasy', 'Sci-Fi'], 108: ['Adventure', 'Comedy', 'Fantasy'], 110: ['Action', 'Comedy', 'Drama', 'Gourmet'], 111: ['Adventure', 'Comedy', 'Sci-Fi'], 114: [''], 115: ['Adventure', 'Comedy', 'Fantasy'], 117: ['Adventure', 'Comedy', 'Fantasy', 'Romance'], 118: ['Adventure', 'Comedy', 'Fantasy'], 119: ['Comedy', 'Drama', 'Romance', 'Slice of Life'], 120: ['Comedy', 'Drama', 'Romance', 'Slice of Life', 'Supernatural'], 121: ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy'], 122: ['Comedy', 'Drama', 'Romance', 'Supernatural'], 123: ['Adventure', 'Comedy', 'Drama', 'Fantasy', 'Romance'], 124: ['Adventure', 'Drama', 'Fantasy', 'Romance'], 126: ['Comedy', 'Drama', 'Romance'], 127: ['Action', 'Comedy', 'Fantasy', 'Sci-Fi'], 128: ['Action', 'Drama', 'Sci-Fi'], 129: ['Action', 'Adventure', 'Comedy', 'Drama', 'Supernatural'], 130: ['Action', 'Adventure', 'Comedy', 'Drama', 'Supernatural'], 131: ['Action', 'Adventure', 'Comedy', 'Drama', 'Supernatural'], 134: ['Action', 'Drama', 'Sci-Fi'], 135: ['Comedy', 'Supernatural'], 136: ['Action', 'Adventure', 'Fantasy'], 137: ['Action', 'Adventure'], 138: ['Action', 'Adventure', 'Fantasy'], 139: ['Action', 'Adventure', 'Fantasy'], 141: [''], 142: ['Adventure', 'Comedy', 'Drama', 'Fantasy', 'Mystery', 'Romance'], 143: ['Drama', 'Girls Love', 'Romance', 'Supernatural'], 144: ['Drama', 'Romance', 'Slice of Life', 'Supernatural'], 145: ['Comedy', 'Drama', 'Romance', 'Slice of Life'], 147: ['Drama', 'Romance', 'Slice of Life'], 148: ['Drama', 'Romance', 'Slice of Life'], 150: ['Action', 'Drama', 'Horror', 'Mystery', 'Supernatural'], 151: ['Action', 'Comedy', 'Girls Love', 'Sci-Fi', 'Ecchi'], 152: ['Action', 'Sci-Fi'], 153: ['Action', 'Adventure', 'Fantasy', 'Supernatural'], 154: ['Action', 'Adventure', 'Comedy', 'Supernatural'], 155: ['Action', 'Drama', 'Fantasy', 'Horror', 'Sci-Fi', 'Supernatural'], 156: ['Action', 'Drama', 'Fantasy', 'Romance'], 157: ['Comedy', 'Fantasy', 'Romance', 'Supernatural', 'Ecchi'], 160: ['Adventure', 'Drama', 'Fantasy', 'Sci-Fi'], 161: ['Action', 'Comedy'], 162: ['Comedy', 'Fantasy', 'Romance'], 163: ['Adventure', 'Comedy', 'Fantasy'], 164: ['Action', 'Adventure', 'Fantasy'], 166: [''], 167: ['Adventure', 'Comedy', 'Drama', 'Fantasy', 'Sci-Fi'], 168: ['Action', 'Adventure', 'Drama', 'Sci-Fi'], 169: ['Action', 'Horror', 'Mystery', 'Romance', 'Supernatural'], 170: ['Comedy', 'Drama', 'Sports'], 171: ['Adventure', 'Drama', 'Fantasy'], 173: ['Comedy', 'Drama', 'Mystery', 'Supernatural'], 174: ['Action', 'Comedy', 'Ecchi'], 177: ['Action', 'Adventure', 'Fantasy', 'Romance', 'Supernatural'], 178: ['Comedy', 'Romance'], 179: ['Comedy', 'Romance'], 181: ['Action', 'Sci-Fi', 'Ecchi'], 182: ['Adventure', 'Fantasy', 'Romance'], 183: [''], 184: ['Action', 'Sci-Fi'], 185: ['Action', 'Drama', 'Sports'], 186: ['Action', 'Drama', 'Sports'], 187: ['Action', 'Drama', 'Romance', 'Sports'], 189: ['Comedy', 'Romance', 'Slice of Life', 'Ecchi'], 190: ['Comedy', 'Drama', 'Romance', 'Ecchi'], 191: ['Comedy', 'Romance', 'Slice of Life'], 193: ['Comedy', 'Drama', 'Romance', 'Ecchi'], 194: ['Adventure', 'Sci-Fi'], 198: ['Action', 'Mystery'], 199: ['Adventure', 'Drama', 'Supernatural'], 202: ['Action', 'Adventure', 'Drama', 'Fantasy', 'Mystery', 'Sci-Fi'], 205: ['Action', 'Adventure', 'Comedy'], 206: ['Action', 'Adventure', 'Drama', 'Fantasy', 'Romance'], 207: ['Action', 'Adventure', 'Fantasy', 'Supernatural'], 208: ['Action', 'Adventure', 'Mystery', 'Sci-Fi'], 209: ['Action', 'Adventure', 'Comedy', 'Drama', 'Sci-Fi'], 210: ['Comedy', 'Fantasy', 'Slice of Life'], 211: [''], 212: ['Action', 'Adventure', 'Comedy', 'Sci-Fi'], 217: ['Comedy', 'Drama', 'Romance', 'Hentai'], 219: ['Action', 'Comedy', 'Drama', 'Sci-Fi'], 222: ['Action', 'Adventure', 'Comedy', 'Mystery', 'Sci-Fi'], 223: ['Adventure', 'Comedy', 'Fantasy'], 226: ['Action', 'Drama', 'Horror', 'Romance', 'Supernatural'], 227: ['Action', 'Avant Garde', 'Comedy', 'Sci-Fi'], 228: ['Horror', 'Mystery', 'Supernatural'], 230: ['Action', 'Comedy'], 232: ['Adventure', 'Comedy', 'Drama', 'Fantasy', 'Romance'], 233: ['Comedy', 'Sci-Fi'], 234: ['Adventure', 'Sports'], 235: ['Adventure', 'Comedy', 'Mystery'], 236: ['Adventure', 'Comedy', 'Drama', 'Sci-Fi', 'Supernatural'], 237: ['Adventure', 'Drama', 'Romance', 'Sci-Fi'], 239: ['Drama', 'Mystery', 'Sci-Fi', 'Supernatural', 'Suspense'], 240: ['Comedy', 'Slice of Life'], 242: ['Comedy', 'Drama', 'Slice of Life'], 245: ['Comedy', 'Drama', 'Slice of Life'], 246: ['Adventure', 'Comedy', 'Fantasy', 'Romance'], 247: ['Fantasy', 'Supernatural'], 248: ['Comedy', 'Romance', 'Ecchi'], 249: ['Action', 'Adventure', 'Comedy', 'Fantasy', 'Romance', 'Supernatural']}
    if type=='tv series':
         a = []
         for i in mids:
              print(i)
              a = a + s[int(i)]
         a.sort()
         b = {}
         for i in a:
              if (i in b.keys()):
                   b.update({i: b[i] + 1})
              else:
                   b.update({i: 1})
         a = []
         for i in b.keys():
              a.append([i, b[i]])
         a.sort(key=lambda x: x[1], reverse=True)
         res = []
         for i in s.keys():
              if (a[0][0] in s[i] and i not in mids):
                   res.append(str(i))
         return res
    if type == 'anime':
         a = []
         for i in mids:
              print(i)
              a = a + k[int(i)]
         a.sort()
         b = {}
         for i in a:
              if (i in b.keys()):
                   b.update({i: b[i] + 1})
              else:
                   b.update({i: 1})
         a = []
         for i in b.keys():
              a.append([i, b[i]])
         a.sort(key=lambda x: x[1], reverse=True)
         res = []
         for i in k.keys():
              if (a[0][0] in k[i] and i not in mids):
                   res.append(str(i))
         return res
    if type == 'manga':
         a = []
         for i in mids:
              print(i)
              a = a + v[int(i)]
         a.sort()
         b = {}
         for i in a:
              if (i in b.keys()):
                   b.update({i: b[i] + 1})
              else:
                   b.update({i: 1})
         a = []
         for i in b.keys():
              a.append([i, b[i]])
         a.sort(key=lambda x: x[1], reverse=True)
         res = []
         for i in v.keys():
              if (a[0][0] in v[i] and i not in mids):
                   res.append(str(i))
         return res
    else:
         a=[]
         for i in mids:
             print(i)
             a=a+m[int(i)]
         a.sort()
         b={}
         for i in a:
             if(i in b.keys()):
                 b.update({i:b[i]+1})
             else:
                 b.update({i:1})
         a=[]
         for i in b.keys():
             a.append([i,b[i]])
         a.sort(key=lambda x: x[1],reverse=True)
         res=[]
         for i in m.keys():
             if(a[0][0] in m[i] and i not in mids):
                 res.append(str(i))
         return res
m = {15324: ['Action', 'Comedy', 'Romance'], 15864: ['Adventure', 'Comedy', 'Drama', 'Western'],
         17136: ['Drama', 'Sci-Fi'], 17925: ['Action', 'Adventure', 'Comedy', 'Drama', 'War'],
         19254: ['Biography', 'Drama', 'History'], 21749: ['Comedy', 'Drama', 'Romance'],
         22100: ['Crime', 'Mystery', 'Thriller'], 25316: ['Comedy', 'Romance'],
         27977: ['Comedy', 'Drama', 'Family', 'Romance'], 31381: ['Drama', 'History', 'Romance', 'War'],
         31679: ['Comedy', 'Drama'], 32553: ['Comedy', 'Drama', 'War'],
         32976: ['Drama', 'Mystery', 'Romance', 'Thriller'], 33467: ['Drama', 'Mystery'],
         34583: ['Drama', 'Romance', 'War'], 35446: ['Comedy', 'Romance', 'War'],
         36775: ['Crime', 'Drama', 'Film-Noir', 'Mystery', 'Thriller'], 38650: ['Drama', 'Family', 'Fantasy'],
         40522: ['Drama'], 40897: ['Adventure', 'Drama', 'Western'], 41959: ['Film-Noir', 'Mystery', 'Thriller'],
         42192: ['Drama'], 42876: ['Crime', 'Drama', 'Mystery'], 43014: ['Drama', 'Film-Noir'], 44741: ['Drama'],
         45152: ['Comedy', 'Musical', 'Romance'], 46268: ['Adventure', 'Drama', 'Thriller'], 46438: ['Drama'],
         46912: ['Crime', 'Thriller'], 47296: ['Crime', 'Drama', 'Thriller'], 47396: ['Mystery', 'Thriller'],
         47478: ['Action', 'Adventure', 'Drama'], 48021: ['Crime', 'Drama', 'Thriller'], 48473: ['Drama'],
         48956: ['Drama'], 50083: ['Crime', 'Drama'], 50188: ['Drama', 'Musical', 'Family'],
         50212: ['Adventure', 'Drama', 'War'], 50825: ['Drama', 'War'], 50870: ['Drama', 'Musical', 'Romance'],
         50976: ['Drama', 'Fantasy', 'History', 'Thriller'], 50986: ['Drama', 'Romance'],
         51201: ['Crime', 'Drama', 'Mystery', 'Thriller'], 51792: ['Drama', 'Music'],
         52357: ['Mystery', 'Romance', 'Thriller'], 52572: ['Drama'], 52618: ['Adventure', 'Drama', 'History'],
         53125: ['Adventure', 'Mystery', 'Thriller'], 53198: ['Crime', 'Drama'], 53291: ['Comedy', 'Music', 'Romance'],
         53604: ['Comedy', 'Drama', 'Romance'], 54098: ['Drama', 'Romance', 'War'],
         54215: ['Horror', 'Mystery', 'Thriller'], 55031: ['Drama', 'War'], 55630: ['Action', 'Drama', 'Thriller'],
         56058: ['Action', 'Drama', 'Mystery'], 56172: ['Adventure', 'Biography', 'Drama', 'History', 'War'],
         56592: ['Crime', 'Drama'], 57012: ['Comedy'], 57115: ['Adventure', 'Drama', 'History', 'Thriller', 'War'],
         57565: ['Crime', 'Drama', 'Mystery', 'Thriller'], 57935: ['Drama', 'Romance'], 58946: ['Drama', 'War'],
         59246: ['Drama', 'Musical', 'Romance'], 59578: ['Western'], 60107: ['Biography', 'Drama', 'History'],
         60196: ['Western'], 60827: ['Drama', 'Thriller'], 61512: ['Crime', 'Drama'], 62622: ['Adventure', 'Sci-Fi'],
         63404: ['Comedy', 'Musical', 'Romance'], 64116: ['Western'], 66763: ['Drama', 'Musical'],
         66921: ['Crime', 'Drama', 'Sci-Fi'], 68646: ['Crime', 'Drama'], 70735: ['Comedy', 'Crime', 'Drama'],
         71315: ['Drama', 'Mystery', 'Thriller'], 71562: ['Crime', 'Drama'], 71853: ['Adventure', 'Comedy', 'Fantasy'],
         72684: ['Adventure', 'Drama', 'History', 'War'], 72783: ['Comedy', 'Drama', 'Romance'],
         72860: ['Action', 'Crime', 'Drama', 'Thriller'], 73486: ['Drama'],
         73707: ['Action', 'Adventure', 'Comedy', 'Drama', 'Musical', 'Thriller', 'Western'], 74958: ['Drama'],
         75148: ['Drama', 'Sport'], 75314: ['Crime', 'Drama'], 76759: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'],
         77416: ['Drama', 'War'], 77451: ['Action', 'Crime', 'Thriller'], 77711: ['Drama', 'Music'],
         78748: ['Horror', 'Sci-Fi'], 78788: ['Drama', 'Mystery', 'War'], 79221: ['Comedy', 'Romance'],
         79470: ['Comedy'], 79944: ['Drama', 'Sci-Fi'], 80678: ['Biography', 'Drama'],
         80684: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 81398: ['Biography', 'Drama', 'Sport'],
         81505: ['Drama', 'Horror'], 82096: ['Adventure', 'Drama', 'Thriller', 'War'], 82971: ['Action', 'Adventure'],
         83658: ['Action', 'Sci-Fi', 'Thriller'], 84787: ['Horror', 'Mystery', 'Sci-Fi'],
         85743: ['Comedy', 'Crime', 'Drama'], 86190: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'],
         86250: ['Crime', 'Drama'], 86879: ['Biography', 'Drama', 'History', 'Music'],
         87544: ['Animation', 'Adventure', 'Fantasy', 'Sci-Fi'], 87843: ['Crime', 'Drama'], 87884: ['Drama'],
         88763: ['Adventure', 'Comedy', 'Sci-Fi'], 89881: ['Action', 'Drama', 'War'],
         90605: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 91251: ['Drama', 'Thriller', 'War'],
         91763: ['Drama', 'War'], 92005: ['Adventure', 'Drama'], 93058: ['Drama', 'War'],
         93578: ['Action', 'Comedy', 'Drama', 'Family', 'Musical', 'Sci-Fi'], 93603: ['Crime', 'Drama'],
         95016: ['Action', 'Thriller'], 95327: ['Animation', 'Drama', 'War'], 95765: ['Drama', 'Romance'],
         96283: ['Animation', 'Family', 'Fantasy'], 97165: ['Comedy', 'Drama'],
         97223: ['Comedy', 'Crime', 'Drama', 'Fantasy'], 97576: ['Action', 'Adventure'],
         99685: ['Biography', 'Crime', 'Drama'], 101649: ['Action', 'Crime', 'Drama'],
         102926: ['Crime', 'Drama', 'Thriller'], 103064: ['Action', 'Sci-Fi'],
         104561: ['Comedy', 'Drama', 'Romance', 'Sport'], 105236: ['Crime', 'Drama', 'Thriller'],
         105271: ['Drama', 'Romance', 'Thriller'], 105575: ['Drama'], 105695: ['Drama', 'Western'],
         107207: ['Biography', 'Crime', 'Drama'], 107290: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'],
         108052: ['Biography', 'Drama', 'History'], 109117: ['Action', 'Comedy', 'Romance'],
         109830: ['Drama', 'Romance'], 110357: ['Animation', 'Adventure', 'Drama', 'Family', 'Musical'],
         110413: ['Action', 'Crime', 'Drama', 'Thriller'], 110912: ['Crime', 'Drama'], 111161: ['Drama'],
         112471: ['Drama', 'Romance'], 112553: ['Drama', 'Romance'], 112573: ['Biography', 'Drama', 'History', 'War'],
         112641: ['Crime', 'Drama'], 112870: ['Drama', 'Romance'], 113247: ['Crime', 'Drama'],
         113277: ['Crime', 'Drama', 'Thriller'], 114369: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         114709: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 114814: ['Crime', 'Mystery', 'Thriller'],
         116231: ['Crime', 'Drama', 'Thriller'], 116282: ['Crime', 'Drama', 'Thriller'],
         116630: ['Action', 'Drama', 'Thriller'], 117951: ['Drama'], 118694: ['Drama', 'Romance'],
         118715: ['Comedy', 'Crime', 'Sport'], 118751: ['Action', 'Drama', 'History', 'Thriller', 'War'],
         118799: ['Comedy', 'Drama', 'Romance', 'War'], 118849: ['Drama', 'Family', 'Sport'],
         119217: ['Drama', 'Romance'], 119385: ['Biography', 'Drama'],
         119488: ['Crime', 'Drama', 'Mystery', 'Thriller'], 119698: ['Animation', 'Action', 'Adventure', 'Fantasy'],
         120382: ['Comedy', 'Drama'], 120586: ['Drama'], 120689: ['Crime', 'Drama', 'Fantasy', 'Mystery'],
         120735: ['Action', 'Comedy', 'Crime'], 120737: ['Action', 'Adventure', 'Drama', 'Fantasy'],
         120815: ['Drama', 'War'], 133093: ['Action', 'Sci-Fi'], 137523: ['Drama'],
         139876: ['Action', 'Crime', 'Drama'], 167260: ['Action', 'Adventure', 'Drama', 'Fantasy'],
         167261: ['Action', 'Adventure', 'Drama', 'Fantasy'], 167404: ['Drama', 'Mystery', 'Thriller'],
         169102: ['Drama', 'Musical', 'Sport'], 169547: ['Drama'], 172495: ['Action', 'Adventure', 'Drama'],
         180093: ['Drama'], 195231: ['Action', 'Crime', 'Drama', 'Thriller'], 196069: ['Adventure', 'Drama', 'Romance'],
         198781: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 200087: ['Action', 'Drama'],
         208092: ['Comedy', 'Crime'], 209144: ['Mystery', 'Thriller'], 211915: ['Comedy', 'Romance'],
         213969: ['Action', 'Comedy', 'Drama', 'Romance'], 214915: ['Comedy', 'Horror', 'Music', 'Mystery', 'Thriller'],
         220656: ['Action', 'Drama', 'Thriller'], 220832: ['Action', 'Crime', 'Drama', 'Thriller'],
         222012: ['Crime', 'Drama', 'History'], 237376: ['Action', 'Drama'], 242256: ['Drama', 'Musical', 'Romance'],
         242519: ['Action', 'Comedy', 'Crime', 'Drama'],
         245429: ['Animation', 'Adventure', 'Family', 'Fantasy', 'Mystery'], 245712: ['Drama', 'Thriller'],
         253474: ['Biography', 'Drama', 'Music', 'War'], 264464: ['Biography', 'Crime', 'Drama'],
         266543: ['Animation', 'Adventure', 'Comedy', 'Family'], 266697: ['Action', 'Crime', 'Drama', 'Thriller'],
         268978: ['Biography', 'Drama'], 291376: ['Action', 'Drama', 'Thriller'],
         292490: ['Comedy', 'Drama', 'Romance'], 296574: ['Action', 'Crime', 'Drama', 'Thriller'],
         312859: ['Action', 'Drama', 'War'], 317248: ['Crime', 'Drama'],
         319736: ['Action', 'Biography', 'Drama', 'History'], 323013: ['Action', 'Drama', 'Romance', 'War'],
         338013: ['Drama', 'Romance', 'Sci-Fi'], 347149: ['Animation', 'Adventure', 'Family', 'Fantasy'],
         347304: ['Comedy', 'Drama', 'Musical', 'Romance'], 353969: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         361748: ['Adventure', 'Drama', 'War'], 363163: ['Biography', 'Drama', 'History', 'War'],
         364569: ['Action', 'Drama', 'Mystery', 'Thriller'], 366840: ['Action', 'Romance', 'Sport'], 367110: ['Drama'],
         367495: ['Adventure', 'Comedy', 'Drama'], 372784: ['Action', 'Adventure'],
         373856: ['Action', 'Crime', 'Drama'], 374887: ['Comedy', 'Drama'], 375611: ['Drama'],
         375878: ['Action', 'Crime', 'Drama', 'Thriller'], 376076: ['Action', 'Drama'],
         376127: ['Action', 'Drama', 'Thriller'], 379370: ['Crime', 'Drama', 'Thriller'], 381681: ['Drama', 'Romance'],
         395169: ['Biography', 'Drama', 'History', 'War'], 400234: ['Action', 'Crime', 'Drama', 'History'],
         402014: ['Action', 'Crime', 'Drama', 'Thriller'], 405094: ['Drama', 'Mystery', 'Thriller'],
         405159: ['Drama', 'Sport'], 405508: ['Comedy', 'Crime', 'Drama'], 407887: ['Crime', 'Drama', 'Thriller'],
         420332: ['Drama', 'Family', 'Musical', 'Romance'], 431619: ['Action', 'Drama', 'Romance'],
         434409: ['Action', 'Drama', 'Sci-Fi', 'Thriller'],
         435761: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 453729: ['Drama', 'Sport'],
         455829: ['Action', 'Crime', 'Thriller'], 456144: ['Comedy', 'Drama', 'Romance'],
         457430: ['Drama', 'Fantasy', 'War'], 466460: ['Comedy', 'Crime', 'Drama'],
         468569: ['Action', 'Crime', 'Drama', 'Thriller'], 469494: ['Drama'], 471571: ['Action', 'Thriller'],
         476735: ['Drama', 'Family'], 477348: ['Crime', 'Drama', 'Thriller'],
         482571: ['Drama', 'Mystery', 'Sci-Fi', 'Thriller'], 488414: ['Action', 'Crime', 'Drama', 'Thriller'],
         499375: ['Drama'], 758758: ['Adventure', 'Biography', 'Drama'], 816258: ['Action', 'Crime', 'Thriller'],
         816692: ['Adventure', 'Drama', 'Sci-Fi'], 824316: ['Drama'], 843326: ['Comedy', 'Drama', 'Romance'],
         871510: ['Drama', 'Family', 'Sport'], 892769: ['Animation', 'Action', 'Adventure', 'Family', 'Fantasy'],
         910970: ['Animation', 'Adventure', 'Family', 'Romance', 'Sci-Fi'],
         978762: ['Animation', 'Comedy', 'Drama', 'Family'], 986264: ['Drama', 'Family'],
         993846: ['Biography', 'Crime', 'Drama'], 10189514: ['Drama'],
         10214826: ['Comedy', 'Crime', 'Mystery', 'Thriller'], 10272386: ['Drama'],
         1028532: ['Biography', 'Drama', 'Family'], 10324144: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         1049413: ['Animation', 'Adventure', 'Comedy', 'Family'], 1077248: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         1093370: ['Comedy', 'Drama', 'Romance'], 1130884: ['Mystery', 'Thriller'], 11581174: ['Action', 'Drama'],
         1180583: ['Drama', 'Romance'], 1187043: ['Comedy', 'Drama'], 1188996: ['Drama'],
         1201607: ['Adventure', 'Drama', 'Fantasy', 'Mystery'], 1205489: ['Drama'], 1230165: ['Drama', 'Music'],
         12361178: ['Crime', 'Drama', 'Thriller'], 1255953: ['Drama', 'Mystery', 'War'],
         1261047: ['Crime', 'Drama', 'Thriller'], 1266583: ['Drama'],
         1280558: ['Action', 'Crime', 'Drama', 'Mystery', 'Thriller'], 1288638: ['Comedy', 'Drama'],
         1291584: ['Action', 'Drama', 'Sport'], 1292703: ['Action', 'Comedy', 'Crime', 'Drama'],
         1305806: ['Drama', 'Mystery', 'Romance', 'Thriller'], 1327035: ['Drama', 'Romance'],
         1345836: ['Action', 'Adventure'], 1375666: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'],
         1392190: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 1392214: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         1417299: ['Action', 'Crime', 'Drama', 'Mystery', 'Thriller'], 1562872: ['Comedy', 'Drama'],
         1620933: ['Action', 'Biography', 'Crime', 'Sport', 'Thriller'], 1639426: ['Drama'],
         1649431: ['Action', 'Drama'], 1675434: ['Biography', 'Comedy', 'Drama'], 1773764: ['Drama'],
         1821480: ['Mystery', 'Thriller'], 1832382: ['Drama'], 1853728: ['Drama', 'Western'],
         1895587: ['Biography', 'Crime', 'Drama'], 1907761: ['Comedy', 'Drama', 'Family'],
         1950186: ['Action', 'Biography', 'Drama', 'Sport'],
         1954470: ['Action', 'Comedy', 'Crime', 'Drama', 'Thriller'],
         1979320: ['Action', 'Biography', 'Drama', 'Sport'], 2024544: ['Biography', 'Drama', 'History'],
         2082197: ['Comedy', 'Drama', 'Romance'],
         2096673: ['Animation', 'Adventure', 'Comedy', 'Drama', 'Family', 'Fantasy'], 2106476: ['Drama'],
         2119532: ['Biography', 'Drama', 'History', 'War'], 2181831: ['Biography', 'Drama'],
         2181931: ['Comedy', 'Drama', 'Family'], 2218988: ['Comedy', 'Drama'],
         2267998: ['Drama', 'Mystery', 'Thriller'], 2278388: ['Adventure', 'Comedy', 'Crime'],
         2283748: ['Comedy', 'Drama', 'Fantasy'], 2317337: ['Comedy', 'Romance'],
         2338151: ['Comedy', 'Drama', 'Musical', 'Sci-Fi'], 2350496: ['Drama', 'Romance'],
         2356180: ['Biography', 'Drama', 'Sport'], 2358592: ['Drama', 'Sci-Fi', 'Thriller'],
         2377938: ['Crime', 'Drama', 'Thriller'],
         2380307: ['Animation', 'Adventure', 'Family', 'Fantasy', 'Music', 'Mystery'],
         2395469: ['Drama', 'Music', 'Romance'], 2564144: ['Comedy', 'Drama'], 2582802: ['Drama', 'Music'],
         2585562: ['Horror', 'Thriller'], 2631186: ['Action', 'Drama'],
         2877108: ['Comedy', 'Crime', 'Drama', 'Fantasy'],
         2948372: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy', 'Music'], 2991224: ['Drama', 'War'],
         3011894: ['Comedy', 'Drama', 'Thriller'], 3124456: ['Mystery', 'Thriller'], 3170832: ['Drama', 'Thriller'],
         3315342: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 3322420: ['Adventure', 'Comedy', 'Drama'],
         3390572: ['Action', 'Crime', 'Drama', 'Thriller'], 3394420: ['Crime', 'Drama', 'Thriller'],
         3417422: ['Crime', 'Drama', 'Thriller'], 3449292: ['Adventure', 'Biography', 'Drama'],
         3569782: ['Action', 'Crime', 'Drama', 'Thriller'], 3614516: ['Comedy', 'Drama'],
         3668162: ['Comedy', 'Drama', 'Romance'], 3822396: ['Action', 'Comedy', 'Drama'],
         3848892: ['Action', 'Thriller'], 3863552: ['Action', 'Adventure', 'Comedy', 'Drama'],
         3973410: ['Comedy', 'Drama'], 4016934: ['Drama', 'Romance', 'Thriller'],
         4154756: ['Action', 'Adventure', 'Sci-Fi'], 4154796: ['Action', 'Adventure', 'Drama', 'Sci-Fi'],
         4169250: ['Biography', 'Drama', 'Sport'], 4387040: ['Drama', 'History'], 4429128: ['Drama', 'Thriller'],
         4430212: ['Crime', 'Drama', 'Mystery', 'Thriller'], 4432480: ['Mystery', 'Thriller'],
         4434004: ['Action', 'Crime', 'Drama'], 4633694: ['Animation', 'Action', 'Adventure', 'Family', 'Sci-Fi'],
         4635372: ['Drama'], 4679210: ['Comedy', 'Drama', 'Romance'],
         4729430: ['Animation', 'Adventure', 'Comedy', 'Family'], 4849438: ['Action', 'Drama'],
         4851630: ['Comedy', 'Drama', 'Thriller'], 4934950: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         4987556: ['Action', 'Crime', 'Thriller'], 4991384: ['Crime', 'Drama', 'Thriller'],
         5005684: ['Drama', 'Family'], 5027774: ['Comedy', 'Crime', 'Drama'],
         5074352: ['Action', 'Biography', 'Drama', 'Sport'], 5082014: ['Adventure', 'Drama', 'Romance', 'Thriller'],
         5121000: ['Biography', 'Drama'], 5311514: ['Animation', 'Drama', 'Fantasy', 'Romance'],
         5311546: ['Drama', 'Family'], 5312232: ['Drama', 'Romance'],
         5323662: ['Animation', 'Drama', 'Family', 'Romance'], 5571734: ['Drama', 'Thriller'],
         5764096: ['Comedy', 'Drama'], 5824826: ['Comedy', 'Drama', 'Romance'], 5867800: ['Drama'],
         5959980: ['Action', 'Crime', 'Drama', 'Thriller'], 6108090: ['Drama', 'Music'],
         6148156: ['Action', 'Crime', 'Drama', 'Thriller'], 6167894: ['Action', 'Comedy', 'Thriller'],
         6315524: ['Action', 'Drama', 'Thriller'], 6380520: ['Action', 'Crime', 'Mystery', 'Thriller'],
         6751668: ['Comedy', 'Drama', 'Thriller'], 6966692: ['Biography', 'Comedy', 'Drama', 'Music'],
         7019842: ['Drama', 'Romance'], 7019942: ['Comedy', 'Crime', 'Drama', 'Thriller'],
         7060344: ['Action', 'Crime', 'Thriller'], 7060460: ['Action', 'Crime', 'Thriller'],
         7098658: ['Action', 'Drama', 'Thriller'], 7180544: ['Action', 'Drama', 'Sport'], 7218518: ['Comedy', 'Drama'],
         7286456: ['Crime', 'Drama', 'Thriller'], 7294534: ['Action', 'Drama', 'Romance'], 7392212: ['Action', 'Drama'],
         7465992: ['Biography', 'Drama'], 7485048: ['Biography', 'Drama'], 7725596: ['Comedy', 'Drama'],
         7738784: ['Drama'], 7758160: ['Action', 'Thriller'],
         7822438: ['Action', 'Crime', 'Drama', 'Mystery', 'Thriller'], 7838252: ['Action', 'Drama'],
         8108198: ['Crime', 'Drama', 'Music', 'Mystery', 'Thriller'], 8108200: ['Action', 'Crime', 'Drama'],
         8110330: ['Comedy', 'Drama', 'Romance'], 8130968: ['Crime', 'Drama', 'Mystery', 'Thriller'],
         8144834: ['Crime', 'Drama', 'Mystery', 'Thriller'], 8176054: ['Drama'],
         8239946: ['Drama', 'Fantasy', 'Horror', 'Thriller'], 8267604: ['Drama'], 8291224: ['Action', 'Drama', 'War'],
         8413338: ['Comedy', 'Drama', 'Romance'], 8503618: ['Biography', 'Drama', 'History', 'Musical'],
         8579674: ['Drama', 'Thriller', 'War'], 8613070: ['Drama', 'Romance'], 8948790: ['Drama', 'Sport'],
         9052870: ['Comedy', 'Drama'], 9477520: ['Action', 'Drama'], 9900782: ['Action', 'Thriller'],
         15097216: ["Crime", "Drama"], 1160419: ["Action", "Adventure", "Drama", "Sci-Fi"]}
a={111161: ['Drama'], 68646: ['Crime', 'Drama'], 71562: ['Crime', 'Drama'], 468569: ['Action', 'Crime', 'Drama', 'Thriller'], 50083: ['Crime', 'Drama'], 108052: ['Biography', 'Drama', 'History'], 167260: ['Action', 'Adventure', 'Drama', 'Fantasy'], 110912: ['Crime', 'Drama'], 60196: ['Adventure', 'Western'], 120737: ['Action', 'Adventure', 'Drama', 'Fantasy'], 137523: ['Drama'], 109830: ['Drama', 'Romance'], 1375666: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 167261: ['Action', 'Adventure', 'Drama', 'Fantasy'], 80684: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 133093: ['Action', 'Sci-Fi'], 99685: ['Biography', 'Crime', 'Drama'], 73486: ['Drama'], 47478: ['Action', 'Adventure', 'Drama'], 114369: ['Crime', 'Drama', 'Mystery', 'Thriller'], 102926: ['Crime', 'Drama', 'Thriller'], 317248: ['Crime', 'Drama'], 118799: ['Comedy', 'Drama', 'Romance', 'War'], 38650: ['Drama', 'Family', 'Fantasy'], 76759: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 120815: ['Drama', 'War'], 816692: ['Adventure', 'Drama', 'Sci-Fi'], 245429: ['Animation', 'Adventure', 'Family', 'Fantasy', 'Mystery'], 120689: ['Crime', 'Drama', 'Fantasy', 'Mystery'], 6751668: ['Comedy', 'Drama', 'Thriller'], 110413: ['Action', 'Crime', 'Drama', 'Thriller'], 56058: ['Action', 'Drama', 'Mystery'], 253474: ['Biography', 'Drama', 'Music', 'War'], 103064: ['Action', 'Sci-Fi'], 114814: ['Crime', 'Drama', 'Mystery', 'Thriller'], 88763: ['Adventure', 'Comedy', 'Sci-Fi'], 54215: ['Horror', 'Mystery', 'Thriller'], 110357: ['Animation', 'Adventure', 'Drama', 'Family', 'Musical'], 27977: ['Comedy', 'Drama', 'Family', 'Romance'], 120586: ['Drama'], 95327: ['Animation', 'Drama', 'War'], 21749: ['Comedy', 'Drama', 'Romance'], 2582802: ['Drama', 'Music'], 172495: ['Action', 'Adventure', 'Drama'], 407887: ['Action', 'Crime', 'Drama', 'Thriller'], 1675434: ['Biography', 'Comedy', 'Drama'], 482571: ['Drama', 'Mystery', 'Sci-Fi', 'Thriller'], 34583: ['Drama', 'Romance', 'War'], 64116: ['Western'], 47396: ['Mystery', 'Thriller'], 95765: ['Drama', 'Romance'], 78748: ['Horror', 'Sci-Fi'], 78788: ['Drama', 'Mystery', 'War'], 209144: ['Mystery', 'Thriller'], 82971: ['Action', 'Adventure'], 32553: ['Comedy', 'Drama', 'War'], 405094: ['Drama', 'Mystery', 'Thriller'], 1853728: ['Drama', 'Western'], 50825: ['Drama', 'War'], 43014: ['Drama', 'Film-Noir'], 910970: ['Animation', 'Adventure', 'Family', 'Sci-Fi'], 4154756: ['Action', 'Adventure', 'Sci-Fi'], 51201: ['Crime', 'Drama', 'Mystery', 'Thriller'], 81505: ['Drama', 'Horror'], 4633694: ['Animation', 'Action', 'Adventure', 'Comedy', 'Family', 'Fantasy', 'Sci-Fi'], 57012: ['Comedy', 'War'], 119698: ['Animation', 'Action', 'Adventure', 'Fantasy'], 364569: ['Action', 'Drama', 'Mystery', 'Thriller'], 7286456: ['Crime', 'Drama', 'Thriller'], 5311514: ['Animation', 'Drama', 'Fantasy', 'Romance'], 1345836: ['Action', 'Crime'], 2380307: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy', 'Music', 'Mystery'], 90605: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 87843: ['Crime', 'Drama'], 4154796: ['Action', 'Adventure', 'Drama', 'Sci-Fi'], 8267604: ['Drama'], 82096: ['Adventure', 'Drama', 'Thriller', 'War'], 57565: ['Crime', 'Drama', 'Mystery', 'Thriller'], 1187043: ['Comedy', 'Drama'], 169547: ['Drama'], 114709: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 86879: ['Biography', 'Drama', 'Music'], 112573: ['Biography', 'Drama', 'History', 'War'], 8503618: ['Biography', 'Drama', 'History', 'Musical'], 361748: ['Adventure', 'Drama', 'War'], 119217: ['Drama', 'Romance'], 86190: ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 62622: ['Adventure', 'Sci-Fi'], 105236: ['Crime', 'Drama', 'Thriller'], 22100: ['Crime', 'Mystery', 'Thriller'], 52357: ['Mystery', 'Romance', 'Thriller'], 986264: ['Drama', 'Family'], 91251: ['Drama', 'Thriller', 'War'], 33467: ['Drama', 'Mystery'], 2106476: ['Drama'], 180093: ['Drama'], 45152: ['Comedy', 'Musical', 'Romance'], 53125: ['Adventure', 'Mystery', 'Thriller'], 338013: ['Drama', 'Romance', 'Sci-Fi'], 40522: ['Drama'], 44741: ['Drama'], 56172: ['Adventure', 'Biography', 'Drama', 'War'], 12349: ['Comedy', 'Drama', 'Family'], 93058: ['Drama', 'War'], 5074352: ['Action', 'Biography', 'Drama', 'Sport'], 53604: ['Comedy', 'Drama', 'Romance'], 10272386: ['Drama', 'Mystery'], 1255953: ['Drama', 'Mystery', 'War'], 17136: ['Drama', 'Sci-Fi'], 36775: ['Crime', 'Drama', 'Film-Noir', 'Mystery', 'Thriller'], 66921: ['Crime', 'Drama', 'Sci-Fi'], 75314: ['Crime', 'Drama'], 48473: ['Drama'], 1832382: ['Drama'], 70735: ['Comedy', 'Crime', 'Drama'], 86250: ['Crime', 'Drama'], 208092: ['Comedy', 'Crime'], 8579674: ['Action', 'Drama', 'War'], 211915: ['Comedy', 'Romance'], 56592: ['Crime', 'Drama'], 435761: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 59578: ['Western'], 15097216: ['Crime', 'Drama'], 1049413: ['Animation', 'Adventure', 'Comedy', 'Drama', 'Family'], 97576: ['Action', 'Adventure'], 113277: ['Action', 'Crime', 'Drama'], 119488: ['Crime', 'Drama', 'Mystery', 'Thriller'], 55630: ['Action', 'Drama', 'Thriller'], 89881: ['Action', 'Drama', 'War'], 95016: ['Action', 'Thriller'], 42876: ['Crime', 'Drama', 'Mystery'], 6966692: ['Biography', 'Comedy', 'Drama', 'Music'], 363163: ['Biography', 'Drama', 'History', 'War'], 71853: ['Adventure', 'Comedy', 'Fantasy'], 42192: ['Drama'], 53291: ['Comedy', 'Music', 'Romance'], 372784: ['Action', 'Adventure'], 105695: ['Drama', 'Western'], 118849: ['Drama', 'Family', 'Sport'], 347149: ['Animation', 'Adventure', 'Family', 'Fantasy'], 993846: ['Biography', 'Comedy', 'Crime', 'Drama'], 55031: ['Drama', 'War'], 57115: ['Adventure', 'Drama', 'History', 'Thriller', 'War'], 112641: ['Crime', 'Drama'], 469494: ['Drama'], 40897: ['Adventure', 'Drama', 'Western'], 457430: ['Drama', 'Fantasy', 'War'], 268978: ['Biography', 'Drama'], 1305806: ['Drama', 'Mystery', 'Romance', 'Thriller'], 81398: ['Biography', 'Drama', 'Sport'], 71411: ['Adventure', 'Biography', 'Drama'], 71315: ['Drama', 'Mystery', 'Thriller'], 96283: ['Animation', 'Comedy', 'Family', 'Fantasy'], 120735: ['Action', 'Comedy', 'Crime'], 1130884: ['Mystery', 'Thriller'], 15864: ['Adventure', 'Comedy', 'Drama', 'Western'], 477348: ['Crime', 'Drama', 'Thriller'], 46912: ['Crime', 'Thriller'], 50976: ['Drama', 'Fantasy'], 84787: ['Horror', 'Mystery', 'Sci-Fi'], 5027774: ['Comedy', 'Crime', 'Drama'], 1160419: ['Action', 'Adventure', 'Drama', 'Sci-Fi'], 80678: ['Biography', 'Drama'], 167404: ['Drama', 'Mystery', 'Thriller'], 4729430: ['Animation', 'Adventure', 'Comedy', 'Family'], 50986: ['Drama', 'Romance'], 41959: ['Film-Noir', 'Mystery', 'Thriller'], 107290: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 120382: ['Comedy', 'Drama'], 434409: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 353969: ['Crime', 'Drama', 'Mystery', 'Thriller'], 83658: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 117951: ['Drama'], 2096673: ['Animation', 'Adventure', 'Comedy', 'Drama', 'Family', 'Fantasy', 'Sci-Fi'], 50212: ['Adventure', 'Drama', 'War'], 116282: ['Crime', 'Thriller'], 1291584: ['Action', 'Drama', 'Sport'], 266543: ['Animation', 'Adventure', 'Comedy', 'Family'], 266697: ['Action', 'Crime', 'Drama', 'Thriller'], 31381: ['Drama', 'History', 'Romance', 'War'], 47296: ['Crime', 'Drama', 'Thriller'], 46438: ['Drama'], 476735: ['Drama', 'Family'], 3011894: ['Comedy', 'Drama', 'Thriller'], 79944: ['Drama', 'Sci-Fi'], 65234: ['Crime', 'Drama', 'History', 'Thriller'], 77416: ['Drama', 'War'], 1392214: ['Crime', 'Drama', 'Mystery', 'Thriller'], 2278388: ['Adventure', 'Comedy', 'Crime'], 17925: ['Action', 'Adventure', 'Comedy', 'Drama', 'War'], 1205489: ['Drama'], 15324: ['Action', 'Comedy', 'Romance'], 60827: ['Drama', 'Thriller'], 112471: ['Drama', 'Romance'], 978762: ['Animation', 'Comedy', 'Drama', 'Family'], 264464: ['Biography', 'Crime', 'Drama'], 31679: ['Comedy', 'Drama'], 107207: ['Biography', 'Crime', 'Drama'], 3170832: ['Drama', 'Thriller'], 72684: ['Adventure', 'Drama', 'History', 'War'], 2267998: ['Drama', 'Mystery', 'Thriller'], 2119532: ['Biography', 'Drama', 'History', 'War'], 19254: ['Biography', 'Drama', 'History'], 8108198: ['Crime', 'Drama', 'Music', 'Mystery', 'Thriller'], 1950186: ['Action', 'Biography', 'Drama', 'Sport'], 2024544: ['Biography', 'Drama', 'History'], 35446: ['Comedy', 'Romance', 'War'], 118715: ['Comedy', 'Crime', 'Sport'], 77711: ['Drama', 'Music'], 892769: ['Animation', 'Action', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 97165: ['Comedy', 'Drama'], 1392190: ['Action', 'Adventure', 'Sci-Fi', 'Thriller'], 52618: ['Adventure', 'Drama', 'History'], 1201607: ['Adventure', 'Fantasy', 'Mystery'], 405159: ['Drama', 'Sport'], 46268: ['Adventure', 'Drama', 'Thriller'], 7019842: ['Drama', 'Romance'], 4016934: ['Drama', 'Romance', 'Thriller'], 92005: ['Adventure', 'Drama'], 74958: ['Drama'], 3315342: ['Action', 'Drama', 'Sci-Fi', 'Thriller'], 61512: ['Crime', 'Drama'], 1954470: ['Action', 'Comedy', 'Crime', 'Drama', 'Thriller'], 1028532: ['Biography', 'Drama', 'Family'], 113247: ['Crime', 'Drama'], 53198: ['Crime', 'Drama'], 91763: ['Drama', 'War'], 5323662: ['Animation', 'Drama'], 1895587: ['Biography', 'Crime', 'Drama'], 198781: ['Animation', 'Adventure', 'Comedy', 'Family', 'Fantasy'], 32976: ['Drama', 'Mystery', 'Romance', 'Thriller'], 79470: ['Comedy'], 395169: ['Biography', 'Drama', 'History', 'War'], 116231: ['Crime', 'Drama', 'Thriller'], 118694: ['Drama', 'Romance'], 1979320: ['Action', 'Biography', 'Drama', 'Sport'], 758758: ['Adventure', 'Biography', 'Drama'], 245712: ['Drama', 'Thriller'], 75148: ['Drama', 'Sport'], 87544: ['Animation', 'Adventure', 'Sci-Fi'], 60107: ['Biography', 'Drama', 'History'], 25316: ['Comedy', 'Romance'], 381681: ['Drama', 'Romance'], 83922: ['Drama'], 169858: ['Animation', 'Action', 'Drama', 'Fantasy', 'Sci-Fi'], 58946: ['Drama', 'War'], 50783: ['Drama'], 93779: ['Adventure', 'Family', 'Fantasy', 'Romance'], 87884: ['Drama'], 111495: ['Drama', 'Mystery', 'Romance']}
# for i in m.keys():
#      print(i)
#      print(m[i])
#      print(a[i])
import csv
with open('tv.csv','r') as file:
     r=csv.reader(file)
     d={}
     c=0
     for i in r:
          if(c==0):
               c+=1
          else:
               print(i[0])
               d.update({int(i[0]):i[5].strip('][').replace('"','').split(', ')})
     print(d)
